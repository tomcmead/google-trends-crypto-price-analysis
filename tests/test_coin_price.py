import crypto_trend_analysis.coin_price as CP
import unittest

class TestCoinInterest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Coin price testing starting...")

    def testCoinPriceDate(self):
        ci = CP.CoinPrice()
        coin_price = ci.coinPrice("solana","2022-01-09-10", "2022-01-10-10")

        for i in coin_price:
            self.assertIsNotNone(i)

        avg_price_increase = ci.avgPriceInc(coin_price)        
        print("Coin Price Increase: {:.4f}%".format(avg_price_increase))     
        self.assertIsNotNone(avg_price_increase)

    def testCoinPriceHour(self):
        ci = CP.CoinPrice()
        coin_price = ci.coinPrice("solana", None, None, 24)

        for i in coin_price:
            self.assertIsNotNone(i)

        avg_price_increase = ci.avgPriceInc(coin_price)        
        print("Coin Price Increase: {:.4f}%".format(avg_price_increase))     
        self.assertIsNotNone(avg_price_increase)

if __name__ == "__main__":
    unittest.main()
