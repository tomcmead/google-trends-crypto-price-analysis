import pytrends.request
import statistics
import random, time

class CoinInterest:
    """ Computes Google trends percentage intrest of coin  within selected timeframe. 
    Stores historical data in pandas data frame, and computes start and end avg interest. """
    trends_api = None

    def __init__(self):
        self.trends_api = pytrends.request.TrendReq()

    def formatDate(self, from_time, to_time):
            """ Convert datetime type to string format required for Google trends """
            start_time_split = from_time.split("-")
            start_time = f"{start_time_split[0]}-{start_time_split[1]}-{start_time_split[2]}T{start_time_split[3]}"
            end_time_split = to_time.split("-")
            end_time = f"{end_time_split[0]}-{end_time_split[1]}-{end_time_split[2]}T{end_time_split[3]}"
            return f"{start_time} {end_time}"

    def avgInterestChange(self, df_interest):
        """ Returns average interest change start and end price of coin interest of dateframe arguement """
        start_avg_interest = 0
        end_avg_interest = 0
        
        num_rows = len(df_interest.index)-1
        start_avg_interest = statistics.mean([df_interest.iat[0,0], df_interest.iat[1,0], df_interest.iat[2,0], 
                                                   df_interest.iat[3,0], df_interest.iat[4,0]])
        end_avg_interest = statistics.mean([df_interest.iat[num_rows,0], df_interest.iat[num_rows-1,0]])

        return end_avg_interest - start_avg_interest

    def coinInterest(self, coin, from_time=None, to_time=None, hours=4):   
        """ Compute Google trends coin interest as pandas dataframe for given timeframe """
        if from_time!=None and to_time!=None:
            time_fr = self.formatDate(from_time, to_time)
        else:
            if(hours==1):
                time_fr = "now 1-H"
            elif(hours==4):
                time_fr = "now 4-H"
            elif(hours==24):
                time_fr = "now 1-d"

        api_request = True
        attempts = 1

        while(api_request):
            try:
                self.trends_api.build_payload(kw_list=[str(coin)], cat=0, timeframe=time_fr, geo='', gprop='')
                df_interest = self.trends_api.interest_over_time()
                api_request = False
            except Exception as e:
                print(f"Error: {e.args}")
                time.sleep(15 ** attempts + random.uniform(0, 3600))
                attempts += 1

        try:
            df_interest.drop(df_interest.columns[[1]], axis=1, inplace=True)
            return df_interest
        except Exception as e:
            print(f"Error: {e.args}")
            
        return