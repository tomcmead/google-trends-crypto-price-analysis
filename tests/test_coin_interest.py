import crypto_trend_analysis.coin_interest as CI
import unittest

class TestCoinInterest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Coin interest testing starting...")

    def testCoinInterest(self):
        ci = CI.CoinInterest()
        interest = ci.coinInterest("Bitcoin")
        ci.avgInterest(interest)

        for i in interest:
            self.assertIsNotNone(i)
        
        start_interest, end_interest = ci.getAvgInterest()
        print("Start Google Trends Interest = {:.4f}%".format(start_interest))
        print("End Google Trends Interest = {:.4f}%".format(end_interest))
        
        self.assertIsNotNone(start_interest)
        self.assertIsNotNone(end_interest)


if __name__ == "__main__":
    unittest.main()
