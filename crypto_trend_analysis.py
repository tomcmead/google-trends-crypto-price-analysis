import crypto_trend_analysis.coin_analysis as CA
import smtplib
import time
import datetime

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
    coins_found = {}

    while(True):
        coins = ca.trendingCoins()
        print(f'Trending Coins: {coins}')
        
        for coin in coins:
            if coins_found[coin] == None:
                coins_found[coin] = time.time()            
                send_notif(coin)

        for coin in coins_found:
            if coins_found[coin] - time.time() > 3600:
                coins_found[coin].pop()

        time.sleep(30)


if __name__ == "__main__":
    crypto_trend_analysis()
