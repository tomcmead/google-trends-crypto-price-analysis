import crypto_trend_analysis.coin_price as CP
import unittest

class TestCoinPrice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Coin price testing starting...")
    
    def testCoinPrices(self):
        cp = CP.CoinPrice()
        coin_prices = cp.coinPrices(['bitcoin','terra-luna'], -100)

        print(f"{coin_prices}")
        self.assertIsNotNone(coin_prices)

if __name__ == "__main__":
    unittest.main()
