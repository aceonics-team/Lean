/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace QuantConnect.Report
{
    /// <summary>
    /// Removes null values in the <see cref="Result"/> object's x,y values so that
    /// deserialization can occur without exceptions.
    /// </summary>
    /// <typeparam name="T">Result type to deserialize into</typeparam>
    public class NullResultValueTypeJsonConverter<T> : JsonConverter
        where T : Result
    {
        private JsonSerializerSettings _settings;

        /// <summary>
        /// Initialize a new instance of <see cref="NullResultValueTypeJsonConverter{T}"/>
        /// </summary>
        public NullResultValueTypeJsonConverter()
        {
            _settings = new JsonSerializerSettings
            {
                Converters = new List<JsonConverter> { new OrderTypeNormalizingJsonConverter() },
                FloatParseHandling = FloatParseHandling.Decimal
            };
        }

        /// <summary>
        /// Determine if this converter can convert a given type
        /// </summary>
        /// <param name="objectType">Object type to convert</param>
        /// <returns>Always true</returns>
        public override bool CanConvert(Type objectType)
        {
            return objectType.IsAssignableTo(typeof(T));
        }

        /// <summary>
        /// Read Json for conversion
        /// </summary>
        /// <returns>Resulting object</returns>
        public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            var token = JToken.ReadFrom(reader);
            if (token.Type == JTokenType.Null)
            {
                return null;
            }

            foreach (JProperty property in GetProperty(token, "Charts").Children())
            {
                foreach (JProperty seriesProperty in GetProperty(property.Value, "Series"))
                {
                    var newValues = new List<JToken>();
                    foreach (var entry in GetProperty(seriesProperty.Value, "Values"))
                    {
                        if (entry is JObject jobj &&
                            (jobj["x"] == null || jobj["x"].Value<long?>() == null ||
                             jobj["y"] == null || jobj["y"].Value<decimal?>() == null))
                        {
                            // null chart point
                            continue;
                        }

                        if (entry is JArray jArray && jArray.Any(jToken => jToken.Type == JTokenType.Null))
                        {
                            // null candlestick
                            continue;
                        }

                        newValues.Add(entry);
                    }

                    var chart = GetProperty(token, "Charts")[property.Name];
                    var series = GetProperty(chart, "Series")[seriesProperty.Name];
                    if (series["Values"] != null)
                    {
                        series["Values"] = JArray.FromObject(newValues);
                    }
                    else if (series["values"] != null)
                    {
                        series["values"] = JArray.FromObject(newValues);
                    }
                }
            }

            // Deserialize with OrderJsonConverter, otherwise it will fail. We convert the token back
            // to its JSON representation and use the `JsonConvert.DeserializeObject<T>(...)` method instead
            // of using `token.ToObject<T>()` since it can be provided a JsonConverter in its arguments.
            return JsonConvert.DeserializeObject<T>(token.ToString(), _settings);
        }

        /// <summary>
        /// Write Json; Not implemented
        /// </summary>
        public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
        {
            throw new NotImplementedException();
        }

        private static JToken GetProperty(JToken jToken, string name)
        {
            return jToken[name] ?? jToken[name.ToLower()];
        }
    }
}
