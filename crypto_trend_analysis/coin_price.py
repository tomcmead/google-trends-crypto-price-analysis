import pandas as pd
import pycoingecko
import datetime
import random, time

class CoinPrice:
    """ Computes average price at start and end of selected timeframe and percentage price increase.
    Stores historical data in pandas data frame. """
    coingecko_api = None

    def __init__(self):
        self.coingecko_api = pycoingecko.CoinGeckoAPI()

    def dateToSec(self, date):
        """ Converts date to seconds since epoch """
        date_split = date.split("-")
        date_secs = datetime.datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]), int(date_split[3]), 0).timestamp()
        return date_secs        

    def avgPriceInc(self, price_data):
        """ Computes the average start and end price of coin price within timeframe """
        start_price_avg = 0
        end_price_avg = 0

        for i in range(5):
            start_price_avg += price_data.get("Price")[i]
            end_price_avg += price_data.get("Price")[-1-i]

        start_price_avg /= 5
        end_price_avg /= 5

        return ((end_price_avg - start_price_avg) / start_price_avg) * 100


    def coinPrices(self, coin_id, from_time=None, to_time=None, hours=4):
        """ Stores historical coin price data within given time range """
        api_request = True
        attempts = 0

        # Repeat attempts to coingecko api until request success returned
        while(api_request):
            try:
                if(from_time!=None and to_time!=None):
                    start_time = self.dateToSec(from_time)
                    end_time = self.dateToSec(to_time)
                    price_data = self.coingecko_api.get_coin_market_chart_range_by_id(id=coin_id,vs_currency='usd',from_timestamp=str(start_time),to_timestamp=str(end_time))
                else:
                    days = hours/24
                    price_data = self.coingecko_api.get_coin_market_chart_by_id(id=coin_id,vs_currency='usd',days=str(days))
                api_request = False
            except Exception as e:
                print(f"Error: {e.args}")
                time.sleep(3600 ** attempts + random.uniform(0, 3600))
                attempts += 1
        
        # Return pandas dataframe for prices column only
        try:
            x,y = zip(*sorted(price_data.get("prices")))
            df_price = pd.DataFrame(y, [datetime.datetime.fromtimestamp(int(str(i)[:-3])) for i in x], columns=['Price'])
            return df_price
        except Exception as e:
            print(f"Error: {e.args}")

        return


    def coinsPriceIncrease(self, coin_ids, percent_increase_mark):
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