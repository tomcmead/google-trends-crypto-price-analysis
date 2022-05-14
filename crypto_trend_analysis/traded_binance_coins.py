import binance.client
import random, time

class TradedBinanceCoins:
    """ Computes all tradable coins on the Binance platorm, stores each CoinGecko ID, symbol and name. """
    
    def tradableBinanceTickers(self):
        """ Computes all tradeable coins on the Binance platform """

        api_key = "xxx"
        api_secret = "xxx"
        api_request = True
        attempts = 0

        while(api_request):
            try:
                client = binance.client.Client(api_key, api_secret)
                exchange_info = client.get_exchange_info()
                api_request = False
            except Exception as e:
                print(f"Error: {e.args}")
                time.sleep(3600 ** attempts + random.uniform(0, 3600))
                attempts += 1

        binance_ticker_pairs = []    

        for s in exchange_info['symbols']: 
            flag_3 = False
            flag_4 = False

            for i in range (3,6):
                if(s['symbol'][i:]=="ETH" or s['symbol'][i:]=="BTC" or s['symbol'][i:]=="BNB"):
                    flag_3 = True
                if(s['symbol'][i:]=="USDT" or s['symbol'][i:]=="BUSD"):
                    flag_4 = True 

            if(flag_3):
                binance_ticker_pairs.append(s['symbol'][:-3]) 
            elif(flag_4):
                binance_ticker_pairs.append(s['symbol'][:-4]) 
                
        binance_tickers = list(dict.fromkeys(binance_ticker_pairs))
        binance_tickers.sort()

        return binance_tickers


    def tickerToNames(self, coingecko_api, tickers):
        """ Returns CoinGecko ID, symbol and name from each coin symbol passed """
        
        coin_info = []
        coin_names = []
        tickers_lower = []
        
        for i in tickers:
            tickers_lower.append(i.lower())

        for x in coingecko_api.get_coins_list():
            if(x.get('symbol') in tickers_lower):
                coin_info.append(x)

        for x in tickers_lower:  
            for y in coin_info:
                if(y["symbol"] == x):
                    coin_names.append(y)

        return coin_names