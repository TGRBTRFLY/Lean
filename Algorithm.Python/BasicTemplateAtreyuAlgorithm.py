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

### <summary>
### Basic template algorithm for the Atreyu brokerage
### </summary>
### <meta name="tag" content="using data" />
### <meta name="tag" content="using quantconnect" />
### <meta name="tag" content="trading and orders" />
class BasicTemplateAtreyuAlgorithm(QCAlgorithm):
    '''Basic template algorithm simply initializes the date range and cash'''

    def Initialize(self):
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''

        self.SetStartDate(2013,10, 7)  #Set Start Date
        self.SetEndDate(2013,10,11)    #Set End Date
        self.SetCash(100000)           #Set Strategy Cash

        self.SetBrokerageModel(BrokerageName.Atreyu)
        self.AddEquity("SPY", Resolution.Minute)

        self.DefaultOrderProperties = AtreyuOrderProperties()
        # Can specify the default exchange to execute an order on.
        # If not specified will default to the primary exchange
        self.DefaultOrderProperties.Exchange = Exchange.BATS
        # Currently only support order for the day
        self.DefaultOrderProperties.TimeInForce = TimeInForce.Day

    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.

        Arguments:
            data: Slice object keyed by symbol containing the stock data
        '''
        if not self.Portfolio.Invested:
            # will set 25% of our buying power with a market order that will be routed to exchange set in the default order properties (BATS)
            self.SetHoldings("SPY", 0.25)
            # will increase our SPY holdings to 50% of our buying power with a market order that will be routed to ARCA

            orderProperties = AtreyuOrderProperties()
            orderProperties.Exchange = Exchange.ARCA
            self.SetHoldings("SPY", 0.50, orderProperties = orderProperties)

            self.Debug("Purchased SPY!")
