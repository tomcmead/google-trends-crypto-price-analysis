import crypto_trend_analysis.traded_binance_coins as BC
import pycoingecko 
import unittest

class TestTradedBinanceCoins(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Tradable Binance coins testing starting...")

    def testGetTickers(self):
        bc = BC.TradedBinanceCoins()
        cg = pycoingecko.CoinGeckoAPI()
        tickers = bc.tradableBinanceTickers()
        coins = bc.tickerToNames(cg, tickers)
        for coin in coins:
            self.assertIsNotNone(coin)

if __name__ == "__main__":
    unittest.main()
