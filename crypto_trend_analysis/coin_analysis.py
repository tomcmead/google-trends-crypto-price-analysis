import pandas as pd
import matplotlib.pyplot as plt

class CoinAnalysis:
    def graphPriceInterest(self, df_price, df_interest):
        df_price.join(df_interest)

        # create figure and axis objects with subplots()
        fig, ax1 = plt.subplots(figsize=(8,6))
        ax1.plot(df_price, color="red")
        ax1.set_xlabel("Time",fontsize=14)
        ax1.set_ylabel("Price ($)",color="red",fontsize=14)

        # twin object for two different y-axis on the sample plot
        ax2=ax1.twinx()
        # make a plot with different y-axis using second axis object
        ax2.plot(df_interest,color="blue")
        ax2.set_ylabel("Interest (%)",color="blue",fontsize=14)
        plt.show()

        plt.get_current_fig_manager().full_screen_toggle()
        plt.close()

    