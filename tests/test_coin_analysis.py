import crypto_trend_analysis.coin_price as CP
import crypto_trend_analysis.coin_interest as CI
import crypto_trend_analysis.coin_analysis as CA
import unittest

class TestCoinCoinAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Coin analysis testing starting...")

    def testGraphPriceInterest(self):
        cp = CP.CoinPrice()
        df_coin_prices = cp.coinPrices("solana", hours=1)
        for coin_price in df_coin_prices:
            self.assertIsNotNone(coin_price)

        ci = CI.CoinInterest()
        df_coin_interest = ci.coinInterest("solana", hours=1)
        for coin_interest in df_coin_interest:
            self.assertIsNotNone(coin_interest)

        ca = CA.CoinAnalysis()     
        self.assertIsNone(ca.graphPriceInterest(df_coin_prices, df_coin_interest))

    def testTrendingCoins(self):
        ca = CA.CoinAnalysis()
    
        ca.trendingCoins()

    

if __name__ == "__main__":
    unittest.main()
