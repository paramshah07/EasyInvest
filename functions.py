#Imports
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from dotenv import find_dotenv
import numpy as np
import datetime as dt
import seaborn as sns
from pathlib import Path
from finquant.portfolio import build_portfolio

import panel as pn
pn.extension('plotly')
import plotly.express as px
import hvplot.pandas

#%matplotlib inline
import sys
sys.path.append(".")
from IPython.display import IFrame
import ipywidgets as widgets
import time
class Functionalities:
    def __init__(self,title):
        self.name = title            # Public
        self.eod_api_t_token = ""
        self.ticker = self.get_ticker()
    
    
    #Scoring Function
    def submitanswers(self):

        #Assigning the answers chosen to variables
        q01_ans = self.q01.value
        q02_ans = self.q02.value
        q03_ans = self.q03.value
        q04_ans = self.q04.value
        q05_ans = self.q05.value
        q06_ans = self.q06.value
        q07_ans = self.q07.value
        q08_ans = self.q08.value
        q09_ans = self.q09.value
        q10_ans = self.q10.value
        q11_ans = self.q11.value
        q12_ans = self.q12.value
        q13_ans = self.q13.value
        q14_ans = self.q14.value
        q15_ans = self.q15.value

        #Setting score variables to 0 
        risk_score = 0
        crypto_score = 0
        esg_score = 0
        dividend_score = 0
        tech_score = 0
        sp500_score = 0
        bonds_score = 0
        commodities_score = 0
        pharma_score = 0
        ai_score = 0
        aggresive_score = 0

        #RISK QUESTIONS

        #Question 1 Scoring
        if q01_ans == "Young with few financial burdens. Ready to accumulate wealth.":
            risk_score += 4
        if q01_ans == "Young family with some financial constraints. Preparing for the future.":
            risk_score +=3
        if q01_ans == "Mature family. You are in your peak earning years and financially stable.":
            risk_score +=2    
        if q01_ans == "Middle Aged with few financial burdens.":
            risk_score +=3  
        if q01_ans == "Preparing for retirement. Financially Stable and at end of working life.":    
            risk_score +=2    
        if q01_ans == "Retired. You rely on existing funds, investments or pension to maintain your lifestyle in retirement.":  
            risk_score +=2

        #Question 2 Scoring
        if q02_ans == "Not Secure":
            risk_score -= 2
            bonds_score += 2
        if q02_ans == "Somewhat Secure":
            risk_score += 0
        if q02_ans == "Secure":
            risk_score += 2    
        if q02_ans == "Very Secure":
            risk_score += 4
            crypto_score += 1
            aggresive_score += 2

        #Question 3 Scoring
        if q03_ans == "Sell all of the investments, you do not intend to take risks.":
            risk_score -= 2
            bonds_score += 2
        if q03_ans == "Sell a portion of your portfolio to cut your losses and reinvest into more secure investment assets":
            risk_score += 0
            bonds_score += 1
        if q03_ans == "Do nothing, wait it out.":
            risk_score += 2    
        if q03_ans == "Invest more funds to lower your average investment price.":
            risk_score += 3
            aggresive_score += 2 

        #Question 4 Scoring
        if q04_ans == "I would prefer investments with little or no fluctuation in value and have a low degree of risk":
            risk_score += 0
            bonds_score += 2
        if q04_ans == "I am happy to have a small proportion of the portfolio invested in assets that have a higher degree of risk in order to achieve a slightly higher return.":
            risk_score += 1
        if q04_ans == "I prefer to have a spread of investments in a balanced portfolio.":
            risk_score += 2
            sp500_score += 2
        if q04_ans == "I would select investments that have a higher degree of investment price fluctuation so that I can earn higher long term returns.":
            risk_score += 4
            aggresive_score += 2       

        #PREFERENCE QUESTIONS

        #Question 5 Scoring
        if q05_ans == "No Importance":
            commodities_score += 2
            esg_score -= 3
        if q05_ans == "Somewhat Important":
            esg_score += 1
        if q05_ans == "Important":
            esg_score += 2
        if q05_ans == "Extremely Important":
            commodities_score -= 1
            esg_score += 5

        #Question 6 Scoring
        if q06_ans == "Yes":
            esg_score += 2

        if q06_ans == "No":
            esg_score -= 3

        #Question 7 Scoring
        if q07_ans == "Not at all":
            crypto_score -= 1
        if q07_ans == "Somewhat":
            crypto_score += 1  
        if q07_ans == "Alot":
            crypto_score += 3

        #Question 8 Scoring
        if q08_ans == "Not at all":
            crypto_score -= 2
        if q08_ans == "Somewhat":
            crypto_score += 1  
        if q08_ans == "Alot":
            crypto_score += 3

        #Question 9 Scoring
        if q09_ans == "Portfolio Growth":
            crypto_score += 1
            esg_score += 1 
            tech_score += 1  
            sp500_score += 1  
            commodities_score += 1  
            pharma_score += 1  
            ai_score += 1  
            aggresive_score += 1        

        if q09_ans == "Increased Cashflow":
            dividend_score +=4


        #Question 10 Scoring
        if q10_ans == "Not Interested":
            crypto_score += 1
            risk_score +=1
        if q10_ans == "Somewhat Interested":
            sp500_score += 2
        if q10_ans == "Very Interested":
            sp500_score += 3
            tech_score += 1
            aggresive_score += 1 


        #Question 11 Scoring
        if q11_ans == "Not Interested":
            tech_score -= 1
        if q11_ans == "Somewhat Interested":
            tech_score += 2
            ai_score += 1
        if q11_ans == "Very Interested":
            tech_score += 4
            ai_score += 4

        #Question 12 Scoring
        if q12_ans == "Not Interested":
            sp500_score += 1
            crypto_score += 1
        if q12_ans == "Somewhat Interested":
            pharma_score += 2
        if q12_ans == "Very Interested":
            pharma_score += 4 
            esg_score += 1

        #Question 13 Scoring
        if q11_ans == "Not Interested":
            tech_score -= 1
            ai_score -= 2
            sp500_score += 1  
            commodities_score += 1  
        if q11_ans == "Somewhat Interested":
            tech_score += 1
            ai_score += 2
        if q11_ans == "Very Interested":
            tech_score += 2
            ai_score += 4

        #Question 14 Scoring
        if q05_ans == "Not Confident":
            sp_500_score -= 4
            crypto_score += 4
            commodities_score += 2  
        if q05_ans == "Somewhat Confident":
            commodities_score += 1  
            crypto_score += 1
        if q05_ans == "Very Confident":
            sp_500_score += 3
            crypto_score -= 2

        #Question 15 Scoring
        if q05_ans == "Long Term Growth":
            sp_500_score += 2
            tech_score +=1
            commodities_score += 2  
        if q05_ans == "Speedy Gains":
            risk_score += 3
            tech_score += 2
            ai_score += 2

        scores = {}
        scores['ESG'] = esg_score
        scores['Crypto'] = crypto_score
        scores['Dividend'] = dividend_score
        scores['Tech'] = tech_score
        scores['SP500'] = sp500_score
        scores['Bonds'] = bonds_score
        scores['Commodities'] = commodities_score
        scores['Pharma'] = pharma_score
        scores['AI'] = ai_score
        scores['Aggresive'] = aggresive_score

        user_cat = max(scores, key=scores.get)

        #max score for risk is 13
        if risk_score >= 7:
            user_risk = 'High' 
        if risk_score <=7:
            user_risk = 'low'

        return (user_cat)

    #User Risk Calc

    def user_risk_tol(self):
        #Assigning the answers chosen to variables
        q01_ans = self.q01.value
        q02_ans = self.q02.value
        q03_ans = self.q03.value
        q04_ans = self.q04.value
        q05_ans = self.q05.value
        q06_ans = self.q06.value
        q07_ans = self.q07.value
        q08_ans = self.q08.value
        q09_ans = self.q09.value
        q10_ans = self.q10.value
        q11_ans = self.q11.value
        q12_ans = self.q12.value
        q13_ans = self.q13.value
        q14_ans = self.q14.value
        q15_ans = self.q15.value

        #Setting score variables to 0 
        risk_score = 0
        crypto_score = 0
        esg_score = 0
        dividend_score = 0
        tech_score = 0
        sp500_score = 0
        bonds_score = 0
        commodities_score = 0
        pharma_score = 0
        ai_score = 0
        aggresive_score = 0

        #RISK QUESTIONS

        #Question 1 Scoring
        if q01_ans == "Young with few financial burdens. Ready to accumulate wealth.":
            risk_score += 4
        if q01_ans == "Young family with some financial constraints. Preparing for the future.":
            risk_score +=3
        if q01_ans == "Mature family. You are in your peak earning years and financially stable.":
            risk_score +=2    
        if q01_ans == "Middle Aged with few financial burdens.":
            risk_score +=3  
        if q01_ans == "Preparing for retirement. Financially Stable and at end of working life.":    
            risk_score +=2    
        if q01_ans == "Retired. You rely on existing funds, investments or pension to maintain your lifestyle in retirement.":  
            risk_score +=2

        #Question 2 Scoring
        if q02_ans == "Not Secure":
            risk_score -= 2
            bonds_score += 2
        if q02_ans == "Somewhat Secure":
            risk_score += 0
        if q02_ans == "Secure":
            risk_score += 2    
        if q02_ans == "Very Secure":
            risk_score += 4
            crypto_score += 1
            aggresive_score += 2

        #Question 3 Scoring
        if q03_ans == "Sell all of the investments, you do not intend to take risks.":
            risk_score -= 2
            bonds_score += 2
        if q03_ans == "Sell a portion of your portfolio to cut your losses and reinvest into more secure investment assets":
            risk_score += 0
            bonds_score += 1
        if q03_ans == "Do nothing, wait it out.":
            risk_score += 2    
        if q03_ans == "Invest more funds to lower your average investment price.":
            risk_score += 3
            aggresive_score += 2 

        #Question 4 Scoring
        if q04_ans == "I would prefer investments with little or no fluctuation in value and have a low degree of risk":
            risk_score += 0
            bonds_score += 2
        if q04_ans == "I am happy to have a small proportion of the portfolio invested in assets that have a higher degree of risk in order to achieve a slightly higher return.":
            risk_score += 1
        if q04_ans == "I prefer to have a spread of investments in a balanced portfolio.":
            risk_score += 2
            sp500_score += 2
        if q04_ans == "I would select investments that have a higher degree of investment price fluctuation so that I can earn higher long term returns.":
            risk_score += 4
            aggresive_score += 2       

        #PREFERENCE QUESTIONS

        #Question 5 Scoring
        if q05_ans == "No Importance":
            commodities_score += 2
            esg_score -= 3
        if q05_ans == "Somewhat Important":
            esg_score += 1
        if q05_ans == "Important":
            esg_score += 2
        if q05_ans == "Extremely Important":
            commodities_score -= 1
            esg_score += 5

        #Question 6 Scoring
        if q06_ans == "Yes":
            esg_score += 2

        if q06_ans == "No":
            esg_score -= 3

        #Question 7 Scoring
        if q07_ans == "Not at all":
            crypto_score -= 1
        if q07_ans == "Somewhat":
            crypto_score += 1  
        if q07_ans == "Alot":
            crypto_score += 3

        #Question 8 Scoring
        if q08_ans == "Not at all":
            crypto_score -= 2
        if q08_ans == "Somewhat":
            crypto_score += 1  
        if q08_ans == "Alot":
            crypto_score += 3

        #Question 9 Scoring
        if q09_ans == "Portfolio Growth":
            crypto_score += 1
            esg_score += 1 
            tech_score += 1  
            sp500_score += 1  
            commodities_score += 1  
            pharma_score += 1  
            ai_score += 1  
            aggresive_score += 1        

        if q09_ans == "Increased Cashflow":
            dividend_score +=4


        #Question 10 Scoring
        if q10_ans == "Not Interested":
            crypto_score += 1
            risk_score +=1
        if q10_ans == "Somewhat Interested":
            sp500_score += 2
        if q10_ans == "Very Interested":
            sp500_score += 3
            tech_score += 1
            aggresive_score += 1 


        #Question 11 Scoring
        if q11_ans == "Not Interested":
            tech_score -= 1
        if q11_ans == "Somewhat Interested":
            tech_score += 2
            ai_score += 1
        if q11_ans == "Very Interested":
            tech_score += 4
            ai_score += 4

        #Question 12 Scoring
        if q12_ans == "Not Interested":
            sp500_score += 1
            crypto_score += 1
        if q12_ans == "Somewhat Interested":
            pharma_score += 2
        if q12_ans == "Very Interested":
            pharma_score += 4 
            esg_score += 1

        #Question 13 Scoring
        if q11_ans == "Not Interested":
            tech_score -= 1
            ai_score -= 2
            sp500_score += 1  
            commodities_score += 1  
        if q11_ans == "Somewhat Interested":
            tech_score += 1
            ai_score += 2
        if q11_ans == "Very Interested":
            tech_score += 2
            ai_score += 4

        #Question 14 Scoring
        if q05_ans == "Not Confident":
            sp_500_score -= 4
            crypto_score += 4
            commodities_score += 2  
        if q05_ans == "Somewhat Confident":
            commodities_score += 1  
            crypto_score += 1
        if q05_ans == "Very Confident":
            sp_500_score += 3
            crypto_score -= 2

        #Question 15 Scoring
        if q05_ans == "Long Term Growth":
            sp_500_score += 2
            tech_score +=1
            commodities_score += 2  
        if q05_ans == "Speedy Gains":
            risk_score += 1
            tech_score += 2
            ai_score += 2

        #max score for risk is 13
        if risk_score >= 9:
            user_risk = 'High' 
        if risk_score <=9:
            user_risk = 'low'

        return (user_risk)

    #Displaying the Quiz
    def startquiz(self):
        
        #Defining Questions

        #Question 1
        self.q01 = widgets.RadioButtons(
            options=['Young with few financial burdens. Ready to accumulate wealth.', 'Young family with some financial constraints. Preparing for the future.', 'Mature family. You are in your peak earning years and financially stable.','Middle Aged with few financial burdens.', 'Preparing for retirement. Financially Stable and at end of working life.','Retired. You rely on existing funds, investments or pension to maintain your lifestyle in retirement.' ],
            layout={'width': 'max-content'}, 
            disabled=False)

        #Question 2
        self.q02 = widgets.RadioButtons(
            options=['Not Secure', 'Somewhat Secure', 'Secure','Very Secure'],
            layout={'width': 'max-content'}, 
            disabled=False)

        #Question 3
        self.q03 = widgets.RadioButtons(
            options=['Sell all of the investments, you do not intend to take risks.', 'Sell a portion of your portfolio to cut your losses and reinvest into more secure investment assets', 'Do nothing, wait it out.','Invest more funds to lower your average investment price.'],
            layout={'width': 'max-content'}, 
            disabled=False)

        #Question 4
        self.q04 = widgets.RadioButtons(
            options=['I would prefer investments with little or no fluctuation in value and have a low degree of risk', 'I am happy to have a small proportion of the portfolio invested in assets that have a higher degree of risk in order to achieve a slightly higher return.', 'I prefer to have a spread of investments in a balanced portfolio.','I would select investments that have a higher degree of investment price fluctuation so that I can earn higher long term returns.'],
            layout={'width': 'max-content'}, 
            disabled=False)

        #PREFERENCE QUESTIONS

        #Question 5
        self.q05 = widgets.ToggleButtons(
            options=['No Importance', 'Somewhat Important', 'Important', 'Extremely Important'],
            disabled=False,
            button_style='')

        #Question 6
        self.q06 = widgets.ToggleButtons(
            options=['Yes', 'No'],
            disabled=False,
            button_style='')

        #Question 7
        self.q07 = widgets.ToggleButtons(
            options=['Not at all','Somewhat', 'Alot'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 8
        self.q08 = widgets.ToggleButtons(
            options=['Not at all','Somewhat', 'Alot'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 9
        self.q09 = widgets.ToggleButtons(
            options=['Portfolio Growth','Increased Cashflow'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 10
        self.q10 = widgets.ToggleButtons(
            options=['Not Interested','Somewhat Interested','Very Interested'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 11
        self.q11 = widgets.ToggleButtons(
            options=['Not Interested','Somewhat Interested','Very Interested'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 12
        self.q12 = widgets.ToggleButtons(
            options=['Not Interested','Somewhat Interested','Very Interested'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 13
        self.q13 = widgets.ToggleButtons(
            options=['Not Interested','Somewhat Interested','Very Interested'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )

        #Question 14
        self.q14 = widgets.ToggleButtons(
            options=['Not Confident','Somewhat Confident','Very Confident'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )


        #Question 15
        self.q15 = widgets.ToggleButtons(
            options=['Long Term Growth','Speedy Gains'],
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     icons=['check'] * 3
        )
    
        check = widgets.Button(description="Save Answers") 
        calc = widgets.Button(description="Calculate") 
    
        #Question 1
        print("Which of the following best describes your current stage of life?")
        display(self.q01)
        print("   ")
        #Question 2
        print("How secure is your current and future income from sources such as salary, pensions or other investments?")
        display(self.q02)
        print("   ")
        #Question 3
        print("If due to market conditions your portfolio fell around 30% within a short period, say a month, would you:")
        display(self.q03)
        print("   ")
        #Question 4
        print("Which one of the following statements describes your feelings towards choosing an investment?")
        display(self.q04)
        print("   ")
        #Question 5
        print("How important is being invested in environmentally friendly companies to you?")
        display(self.q05)
        print("   ")
        #Question 6
        print("Do you believe in Climate Change?")
        display(self.q06)
        print("   ")
        #Question 7
        print("How much, if at all, have you read about popular cryptocurrencies?")
        display(self.q07)
        print("   ")
        #Question 8
        print("Do you believe cryptocurrency will be increasingly used everyday in the future?")
        display(self.q08)
        print("   ")
        #Question 9
        print("Are you more interested in portfolio growth or to increase in your cash flow?")
        display(self.q09)
        print("   ")
        #Question 10
        print("How interested are you in having a heavily weighted portfolio in large companies with consistent performance?")
        display(self.q10)
        print("   ")
        #Question 11
        print("How interested are you in technology companies?")
        display(self.q11)
        print("   ")
        #Question 12
        print("How interested are you in healthcare and pharmaceutical companies?")
        display(self.q12)
        print("   ")
        #Question 13
        print("Are you interested in Artificial Intelligence and Machine Learning Technologies?")
        display(self.q13)
        print("   ")
        #Question 14
        print("How confident are you with the future of our entire financial system?")
        display(self.q14)
        print("   ")
        #Question 15
        print("Are you looking for longterm consistent growth or speedy gains?")
        display(self.q15)
        print(" ")
        print("When ready please submit your answers by clicking save below")
        display(check)
        check.on_click(self.submitanswers() )
        print(" ")
        print("Once Saved press below button to calculate")
        display(calc)
        check.on_click(self.user_risk_tol())

        return
    
    def get_ticker(self):
        #ticker = "VTI.US"
        ticker = "FTEC" ## uncommenting this line would give user selected ticker 
        #return ticker
        return ticker

    # retrieve data from eodhistoricaldata
    def get_stock_data(self):
        # period =- d/w/m daily/weekly/monthly
        # from = and to = format is ‘YYYY-MM-DD’
        ticker = self.get_ticker()
        eod_stock_price_url = "https://eodhistoricaldata.com/api/eod/"+ticker+"?api_token="+eod_api_token+"&period=d&fmt=json"
        etf_stock_data = requests.get(eod_stock_price_url).json()
        #df = pd.json_normalize(etf_stock_data) ## this is not working in earlier versions of panda
        df_data = []
        for item in etf_stock_data:
            df_data.append([
                item['date'],
                item['open'],
                item['high'],
                item['low'],
                item['close'],
                item['volume']
                ])

        # Populate dataframe
        df = pd.DataFrame(df_data, columns=['date', 'open', 'high', 'low', 'close', 'volume']).set_index('date')
        df = df.head(10)

        return df

    # sunburst plot for stock prices data 
    def sunburts_ticker_analysis(self):
        ticker = "VTI.US" #get_ticker()
        ## Sunburst
        eod_api_token = "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
        eod_stock_price_url = "https://eodhistoricaldata.com/api/eod/"+ticker+"?api_token="+eod_api_token+"&period=d&fmt=json"
        etf_stock_data = requests.get(eod_stock_price_url).json()

        df_data = []
        for item in etf_stock_data:
            df_data.append([
                item['date'],
                item['open'],
                item['high'],
                item['low'],
                item['close'],
                item['volume']
                ])

        # Populate dataframe
        df = pd.DataFrame(df_data, columns=['date', 'open', 'high', 'low', 'close', 'volume']).set_index('date')
        df = df.head(10)
        df.reset_index()
        return px.sunburst(df, 
            path=["open","high","low","close","volume"], 
            values='close',
            color='close'
        )
        #fig.show()
    #sunburts_ticker_analysis()
    
    ### Set up some filters for EOD API calls
    def eod_url (self, url_ticker, url_filter, api_token):
        # Determine filter
        if url_filter == "none":
            ufilter = ""
        elif url_filter == "tech":
            ufilter = "&filter=Technicals"
        elif url_filter == "top1":
            ufilter = "&filter=ETF_Data::Top_1_Holdings"
        elif url_filter == "top10":
            ufilter = "&filter=ETF_Data::Top_10_Holdings"
        elif url_filter == "holdings":
            ufilter = "&filter=ETF_Data::Holdings"
        elif url_filter == "start":
            ufilter = "&filter=ETF_Data::Inception_Date" 
        elif url_filter == "gen_all":
            ufilter = "&filter=General::Code,General::Name,General::Type"
        elif url_filter == "gen":
            ufilter = "&filter=General"
        elif url_filter == "sec_wei":
            ufilter = "&filter=ETF_Data::Sector_Weights"
        elif url_filter == "world":
            ufilter = "&filter=ETF_Data::World_Regions"
        elif url_filter == "perf":
            ufilter = "&filter=ETF_Data::Performance"
        else:
            ufilter = ""

        # Build base URL
        url = "https://eodhistoricaldata.com/api/fundamentals/" + url_ticker + api_token + ufilter

        return url
    
    # Fetch ETF data
    def plotPieTop10Holdings(self):
        ticker = self.get_ticker()

        etf_t10_json = requests.get(self.eod_url(ticker,"top10",self.eod_api_token)).json()

        # Create list to populate dataframe
        etf_t10 = []
        etf_t10_ticks = []
        for i in etf_t10_json:
            # Build ticker list
            etf_t10_ticks.append([etf_t10_json[i]['Code']])

            # Build DF data
            etf_t10.append(
                [etf_t10_json[i]['Code'],
                 etf_t10_json[i]['Assets_%']])

        # Create dataframe
        etf_t10_df = pd.DataFrame(etf_t10, columns=['Ticker','Top10 Weight']).set_index('Ticker')

        # Plot (Matplotlib)
        #etf_t10_df.plot.pie(subplots=True, figsize=(8,12), shadow=True)

        # Plotly
        etf_t10_df_ly = etf_t10_df.reset_index()
        return px.pie(etf_t10_df_ly, values='Top10 Weight',
               names='Ticker', title='Top10 Holdings', width=800,
               height=600, color_discrete_sequence=px.colors.sequential.deep)#.show()

    #pie plot for sector and weights data 
    def plotPieSectorWeights(self):    
        # Fetch ETF data
        etf_sw_json = requests.get(self.eod_url(self.ticker,"sec_wei",self.eod_api_token)).json()

        # Create list to populate dataframe
        etf_secwei = []
        for sec, wei in etf_sw_json.items():
            etf_secwei.append(
                [sec,float(wei['Relative_to_Category'])]
            )

        # Populate dataframe
        etf_sw_df = pd.DataFrame(etf_secwei, columns=['Sector','Weight']).set_index('Sector')
        etf_sw_df

        # Plot (Matplotlib)
        #etf_sw_df.plot.pie(subplots=True, figsize=(8,12), shadow=True)

        # Plotly
        etf_sw_df_ly = etf_sw_df.reset_index()
        return px.pie(etf_sw_df_ly, values='Weight', names='Sector',
               title='Holdings by Sector', width=800,
               height=600, color_discrete_sequence=px.colors.sequential.dense)#.show()
    
    # plot based on regional weights 
    def plotWorldRegionalWeights(self):
        # Fetch ETF data
        ticker = self.get_ticker()
        etf_ww_json = requests.get(self.eod_url(ticker,"world",self.eod_api_token)).json()

        # Create list to populate dataframe
        etf_wwei = []
        for reg, wei in etf_ww_json.items():
            etf_wwei.append(
                [reg,float(wei['Relative_to_Category'])]
            )

        # Populate dataframe
        etf_ww_df = pd.DataFrame(etf_wwei, columns=['Region','Weight']).set_index('Region')
        etf_ww_df

        # Plot
        #etf_ww_df.plot.pie(subplots=True, figsize=(8,12), shadow=True)

        # Plotly
        etf_ww_df_ly = etf_ww_df.reset_index()
        return px.pie(etf_ww_df_ly, values='Weight', names='Region',
               title='Holdings by World Region', width=800,
               height=600, color_discrete_sequence=px.colors.sequential.matter)#.show()

    # bar plot for returns per period 
    def plotBarReturnsPerPeriod(self):
        etf_data = requests.get(self.eod_url(self.ticker,"perf",self.eod_api_token)).json()
        etf_data

        etf_d_df = pd.DataFrame()
        df_per = []
        df_ret = []

        # Loop through the earnings
        for ret in list(etf_data):
            if (   ret == "1y_Volatility" or ret == "3y_Volatility"
                or ret == "3y_ExpReturn" or ret == "3y_SharpRatio"):
                etf_data.pop(ret)
            else:
                df_per.append(ret)
                df_ret.append(float(etf_data[ret]))

        # Create dataframe
        etf_d_df['Period'] = df_per
        etf_d_df['% Return'] = df_ret
        etf_d_df.sort_index(inplace=True, ascending=False)

        # Plot
        #etf_d_df.hvplot.line(x='Period')

        # Plotly
        return px.bar(etf_d_df, x='Period', y='% Return',
                     title='ETF Returns per Period',
                     color='% Return', width=900, height=500
        )#.show()
    
    # plot eod data for top 10 tickers 
    def plotEodDataForTop10Ticker(self):
        ### Fetch end of day data for each Top10 Ticker and normalise the data
        #   Initialise vals
        date = []
        close = []
        all_list = []
        etf_t11_ticks = []
        ind_counter = 0
        counter = 0
        col_names = {}
        #alp_data_df = pd.DataFrame()
        #ticker = "VTI.US"
        ticker = "FTEC"
        etf_t10_json = requests.get(eod_url(ticker,"top10",eod_api_token)).json()

        # Create list to populate dataframe
        etf_t10 = []
        etf_t10_ticks = []
        for i in etf_t10_json:
            # Build ticker list
            etf_t10_ticks.append([etf_t10_json[i]['Code']])
        #   Do some cleanup for all tickers
        etf_t11_ticks.append(ticker)
        for tick in etf_t10_ticks:
            etf_t11_ticks.append(tick[0])

        eod_stock_price_url = "https://eodhistoricaldata.com/api/eod/"+ticker+"?api_token="+eod_api_token+"&period=d&fmt=json&from=2016-07-09&to=2021-07-09"
        etf_stock_data = requests.get(eod_stock_price_url).json()
        #df = pd.json_normalize(etf_stock_data) ## this is not working in earlier versions of panda
        df_data = []
        for item in etf_stock_data:
            df_data.append([
                item['date'],
                item['open'],
                item['high'],
                item['low'],
                item['close'],
                item['volume']
                ])

        # Populate dataframe
        df = pd.DataFrame(df_data, columns=['date', 'open', 'high', 'low', 'close', 'volume']).set_index('date')
        df = df.head(10)

        # Loop through ETF + top10 tickers, build lists and DataFrame
        for tick in etf_t11_ticks:
            # Initialise for loop
            date = []
            close = []

        return px.line(df, title="Daily Prices - ETF vs Top10 Constituents", height=500, width=1000)#.show()
