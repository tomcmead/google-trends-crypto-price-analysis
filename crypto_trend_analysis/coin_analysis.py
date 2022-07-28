import pandas as pd
import matplotlib.pyplot as plt
import crypto_trend_analysis.coin_price as CP
import crypto_trend_analysis.coin_interest as CI
import crypto_trend_analysis.traded_binance_coins as BC

class CoinAnalysis:

    def __init__(self):
        # object instantiation
        self.bc = BC.TradedBinanceCoins()
        self.cp = CP.CoinPrice()
        self.ci = CI.CoinInterest()

    def graphPriceInterest(self, df_price, df_interest):
        df_price.join(df_interest)

        # create figure and axis objects with subplots()
        fig, ax1 = plt.subplots(figsize=(8,6))
        ax1.plot(df_price, color="red")
        ax1.set_xlabel("Time",fontsize=14)
        ax1.set_ylabel("Price ($)",color="red",fontsize=14)

        # twin object for two different y-axis on the sample plot
        ax2=ax1.twinx()
        # make a plot with different y-axis using second axis object
        ax2.plot(df_interest,color="blue")
        ax2.set_ylabel("Interest (%)",color="blue",fontsize=14)
        plt.show()

        plt.get_current_fig_manager().full_screen_toggle()
        plt.close()

        return

    def trendingCoins(self):
        
        # get all tradable coins on binance
        tickers = self.bc.tradableBinanceTickers()
        coins = self.bc.tickerToNames(tickers)
        
        # get list of coin names and coingecko id
        coin_names = []
        coin_ids = []

        for coin in coins:
            coin_names.append(coin['name'])
            coin_ids.append(coin['id'])

        # get coins with 5% price increase in past hour
        increasing_coins = self.cp.coinsPriceIncrease(coin_ids, 5)

        # for coins with price increase find if coin is trending
        coins = []
        for coin in increasing_coins:
            df_interest = self.ci.coinInterest(coin, hours=4)
            try:
                if self.ci.avgInterestChange(df_interest) > 25:
                    coins.append(coin['name']) 
            except Exception as e:
                print(f"Error: {e.args}")
        
        return coins
            
