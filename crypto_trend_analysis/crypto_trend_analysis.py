import crypto_trend_analysis.coin_analysis as CA
import smtplib
import time

def send_notif(coin):
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()     # Encryption
    smtp.ehlo()

    smtp.login("***", "***")

    subject = 'Crypto Coin Available'
    body = 'Coin Trending: ' + coin + '.';

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail("***", '***', msg) 

def crypto_trend_analysis():
    ca = CA.CoinAnalysis()

    while(True):
        coins = ca.trendingCoins()
        if len(coins):
            for coin in coins:
                send_notif(coin)
        time.sleep(30)


if __name__ == "__main__":
    crypto_trend_analysis()
