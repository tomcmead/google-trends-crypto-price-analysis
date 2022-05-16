import crypto_trend_analysis.traded_binance_coins as BC
import unittest

class TestTradedBinanceCoins(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Tradable Binance coins testing starting...")

    def testGetTickers(self):
        bc = BC.TradedBinanceCoins()

        tickers = bc.tradableBinanceTickers()
        coins = bc.tickerToNames(tickers)
        
        for coin in coins:
            print(coin)
            self.assertIsNotNone(coin)
        

if __name__ == "__main__":
    unittest.main()
