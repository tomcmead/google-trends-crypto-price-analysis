import pandas as pd
import pycoingecko

class CoinPrice:
    """ Computes average price at start and end of selected timeframe and percentage price increase.
    Stores historical data in pandas data frame. """
    coingecko_api = None

    def __init__(self):
        self.coingecko_api = pycoingecko.CoinGeckoAPI()

    def coinPrices(self, coin_ids, percent_increase_mark):
        """ Stores historical coin price data within given time range """
        coins_data = self.coingecko_api.get_coins_markets("usd", ids=coin_ids, price_change_percentage='1h')
        coins_price_increased = []
        
        for coin_data in coins_data:
            try:
                if(coin_data['price_change_percentage_1h_in_currency'] >= percent_increase_mark):
                    coins_price_increased.append(coin_data['name'])
            except Exception as e:
                print(f"Error: {e.args}")
            
        return coins_price_increased