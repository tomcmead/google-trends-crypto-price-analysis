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
        coin_price = cp.coinPrice("solana", "2022-01-09-10", "2022-01-10-10")
        for price in coin_price:
            self.assertIsNotNone(price)

        ci = CI.CoinInterest()
        coin_interest = ci.coinInterest("solana", "2022-01-09-10", "2022-01-10-10")
        for interest in coin_interest:
            self.assertIsNotNone(interest)

        ca = CA.CoinAnalysis()     
        self.assertIsNone(ca.graphPriceInterest(coin_price, coin_interest))
    

if __name__ == "__main__":
    unittest.main()
