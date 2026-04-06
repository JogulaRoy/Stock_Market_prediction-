import yfinance  as yf 
import pandas as pd 

#yfinance allows you to download stock data from yahoo finance
#pandas allows you to clean the messy data and organize it for further 

#download the data for the stock you want to analyze 
def download_data(stock_symbol,start,end):
    print(f"downloading data of {stock_symbol} from {start} to {end}")
    data=yf.download(stock_symbol,start=start,end=end)
    return data
#clean data 
def clean_data(data):
   print("cleaning the downloaded data")
   print(data.isnull().sum())
   #here the isnull() function counts the no. of missing values and sum() function gives the total value 
   #after finding the missing values , we need to drop the null values 
   #na - not available values--- this dropna functiopn drops the not available values
   data=data.dropna()
   '''after dropping the null vlues , reset the index ofthe dataframe with default 0,1,2... values 
   the function used is reset_inde(inplace=True)
   here inplace=True means that the changes will be made in the original dataframe and not a copy of it
   '''
   data=data.reset_index()
   #make sure the date is in datetime format 
   data['Date']=pd.to_datetime(data['Date'])
   #sort values of date
   data= data.sort_values('Date')
   return data 
def save_data(data,filename):
    data.to_csv(filename,index=False)
    print(f"cleaned data is saved to the path {filename}")
if __name__=="__main__":    
    stock_symbol=input("enter the stock symbol like GOOG, AAPL, MSFT: ")
    start=input("enter the start date in the format YYYY-MM-DD: ")
    end=input("enter the end date in the format YYYY-MM-DD: ")
    raw_data=download_data(stock_symbol,start,end)
    cleaned_data=clean_data(raw_data)
    save_data(cleaned_data,"../data/cleaned_stock_data.csv")