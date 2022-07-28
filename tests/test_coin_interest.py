import crypto_trend_analysis.coin_interest as CI
import unittest

class TestCoinInterest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Coin interest testing starting...")

    def testCoinInterestHour(self):
        ci = CI.CoinInterest()
        df_interest = ci.coinInterest("Bitcoin", hours=1) 
        for coin_interest in df_interest: 
            self.assertIsNotNone(coin_interest)

    def testCoinInterestDate(self):
        ci = CI.CoinInterest()
        df_interest = ci.coinInterest("Bitcoin", from_time="2022-01-09-10", to_time="2022-01-10-10")   
        for coin_interest in df_interest: 
            self.assertIsNotNone(coin_interest)


if __name__ == "__main__":
    unittest.main()
