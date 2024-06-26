# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from AlgorithmImports import *

class EmptyMinute400EquityBenchmark(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2015, 9, 1)
        self.set_end_date(2015, 12, 1)

        for symbol in Symbols().equity.all()[:400]:
            self.add_security(SecurityType.EQUITY, symbol)
    
    def on_data(self, data):
        pass
    
class Symbols(object):
    
    def __init__(self):
        self.equity = self.Equity()
    
    class Equity(object):       
        def all(self):
            return [
                    "SPY",
                    "AAPL",
                    "FB",
                    "VXX",
                    "VRX",
                    "NFLX",
                    "UVXY",
                    "QQQ",
                    "IWM",
                    "BABA",
                    "GILD",
                    "XIV",
                    "XOM",
                    "CVX",
                    "MSFT",
                    "GE",
                    "SLB",
                    "JPM",
                    "XLE",
                    "DIS",
                    "AMZN",
                    "TWTR",
                    "PFE",
                    "C",
                    "BAC",
                    "ABBV",
                    "JNJ",
                    "HAL",
                    "XLV",
                    "INTC",
                    "WFC",
                    "V",
                    "YHOO",
                    "COP",
                    "MYL",
                    "AGN",
                    "WMT",
                    "KMI",
                    "MRK",
                    "TSLA",
                    "GDX",
                    "LLY",
                    "FCX",
                    "CAT",
                    "CELG",
                    "QCOM",
                    "MCD",
                    "CMCSA",
                    "XOP",
                    "CVS",
                    "AMGN",
                    "DOW",
                    "AAL",
                    "APC",
                    "SUNE",
                    "MU",
                    "VLO",
                    "SBUX",
                    "WMB",
                    "PG",
                    "EOG",
                    "DVN",
                    "BMY",
                    "APA",
                    "UNH",
                    "EEM",
                    "IBM",
                    "NKE",
                    "T",
                    "HD",
                    "UNP",
                    "DAL",
                    "ENDP",
                    "CSCO",
                    "OXY",
                    "MRO",
                    "MDT",
                    "TXN",
                    "WLL",
                    "ORCL",
                    "GOOGL",
                    "UAL",
                    "WYNN",
                    "MS",
                    "HZNP",
                    "BIIB",
                    "VZ",
                    "GM",
                    "NBL",
                    "TWX",
                    "SWKS",
                    "JD",
                    "HCA",
                    "AVGO",
                    "YUM",
                    "KO",
                    "GOOG",
                    "GS",
                    "PEP",
                    "AIG",
                    "EMC",
                    "BIDU",
                    "CLR",
                    "PYPL",
                    "LVS",
                    "SWN",
                    "AXP",
                    "ATVI",
                    "RRC",
                    "WBA",
                    "MPC",
                    "NXPI",
                    "ETE",
                    "NOV",
                    "FOXA",
                    "SNDK",
                    "DIA",
                    "UTX",
                    "DD",
                    "WDC",
                    "AA",
                    "M",
                    "FXI",
                    "RIG",
                    "MA",
                    "DUST",
                    "TGT",
                    "AET",
                    "EBAY",
                    "LUV",
                    "EFA",
                    "BRK.B",
                    "BA",
                    "MET",
                    "LYB",
                    "SVXY",
                    "UWTI",
                    "HON",
                    "HPQ",
                    "OAS",
                    "ABT",
                    "MO",
                    "ESRX",
                    "TEVA",
                    "STX",
                    "IBB",
                    "F",
                    "CBS",
                    "TLT",
                    "PM",
                    "ESV",
                    "NE",
                    "PSX",
                    "SCHW",
                    "MON",
                    "HES",
                    "GPRO",
                    "TVIX",
                    "MNK",
                    "NVDA",
                    "NFX",
                    "USO",
                    "NUGT",
                    "EWZ",
                    "LOW",
                    "UA",
                    "TNA",
                    "XLY",
                    "MMM",
                    "PXD",
                    "VIAB",
                    "MDLZ",
                    "NEM",
                    "USB",
                    "MUR",
                    "ETN",
                    "FEYE",
                    "PTEN",
                    "OIH",
                    "UPS",
                    "CHK",
                    "DHR",
                    "RAI",
                    "TQQQ",
                    "CCL",
                    "BRCM",
                    "DG",
                    "JBLU",
                    "CRM",
                    "ADBE",
                    "COG",
                    "PBR",
                    "HP",
                    "BHI",
                    "BK",
                    "TJX",
                    "DE",
                    "COF",
                    "INCY",
                    "DHI",
                    "ABC",
                    "XLI",
                    "ZTS",
                    "BP",
                    "IYR",
                    "PNC",
                    "CNX",
                    "XLF",
                    "LRCX",
                    "GG",
                    "RDS.A",
                    "WFM",
                    "TSO",
                    "ANTM",
                    "KSS",
                    "EA",
                    "PRU",
                    "RAD",
                    "WFT",
                    "XBI",
                    "THC",
                    "VWO",
                    "CTSH",
                    "ABX",
                    "VMW",
                    "CSX",
                    "ACN",
                    "EMR",
                    "SE",
                    "MJN",
                    "SKX",
                    "ACE",
                    "P",
                    "CMI",
                    "CL",
                    "CAH",
                    "EXC",
                    "DUK",
                    "AMAT",
                    "AEM",
                    "FTI",
                    "STT",
                    "ILMN",
                    "HOG",
                    "KR",
                    "EXPE",
                    "VRTX",
                    "IVV",
                    "CAM",
                    "GPS",
                    "MCK",
                    "ADSK",
                    "CMCSK",
                    "HTZ",
                    "MGM",
                    "DLTR",
                    "STI",
                    "CYH",
                    "MOS",
                    "CNQ",
                    "GLW",
                    "KEY",
                    "KORS",
                    "SIRI",
                    "EPD",
                    "SU",
                    "DFS",
                    "TMO",
                    "TAP",
                    "HST",
                    "NBR",
                    "EQT",
                    "XLU",
                    "BSX",
                    "COST",
                    "CTRP",
                    "HFC",
                    "VNQ",
                    "TRV",
                    "POT",
                    "CERN",
                    "LLTC",
                    "DO",
                    "ADI",
                    "BAX",
                    "AMT",
                    "URI",
                    "UCO",
                    "ECA",
                    "MAS",
                    "ALL",
                    "PCAR",
                    "VIPS",
                    "ATW",
                    "SPXU",
                    "LNKD",
                    "X",
                    "TSM",
                    "SO",
                    "BBT",
                    "SYF",
                    "VFC",
                    "CXO",
                    "IR",
                    "PWR",
                    "GLD",
                    "LNG",
                    "ETP",
                    "JNPR",
                    "MAT",
                    "KLAC",
                    "XLK",
                    "TRIP",
                    "AEP",
                    "VTR",
                    "ROST",
                    "RDC",
                    "CF",
                    "FAS",
                    "HCN",
                    "AR",
                    "SM",
                    "WPX",
                    "D",
                    "HOT",
                    "PRGO",
                    "ALXN",
                    "CNC",
                    "VALE",
                    "JCP",
                    "GDXJ",
                    "OKE",
                    "ADM",
                    "JOY",
                    "TSN",
                    "MAR",
                    "KHC",
                    "NSC",
                    "CMA",
                    "COH",
                    "GMCR",
                    "FL",
                    "FITB",
                    "BHP",
                    "JWN",
                    "DNR",
                    "PBF",
                    "XLNX"]
