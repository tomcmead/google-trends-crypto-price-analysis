import crypto_trend_analysis.coin_price as CP
import unittest

class TestCoinPrice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Coin price testing starting...")

    def testCoinPriceDate(self):
        ci = CP.CoinPrice()
        coin_price = ci.coinPrices("solana", "2022-01-09-10", "2022-01-10-10")

        for i in coin_price:
            self.assertIsNotNone(i)

        avg_price_increase = ci.avgPriceInc(coin_price)        
        print("Coin Price Increase: {:.4f}%".format(avg_price_increase))     
        self.assertIsNotNone(avg_price_increase)

    def testCoinPriceHour(self):
        ci = CP.CoinPrice()
        coin_price = ci.coinPrices("solana", hours=24)

        for i in coin_price:
            self.assertIsNotNone(i)

        avg_price_increase = ci.avgPriceInc(coin_price)        
        print("Coin Price Increase: {:.4f}%".format(avg_price_increase))     
        self.assertIsNotNone(avg_price_increase)


    def testCoinPrices(self):
        cp = CP.CoinPrice()
        coin_prices = cp.coinsPriceIncrease(['bitcoin','terra-luna'], -100)

        print(f"{coin_prices}")
        self.assertIsNotNone(coin_prices)

if __name__ == "__main__":
    unittest.main()
