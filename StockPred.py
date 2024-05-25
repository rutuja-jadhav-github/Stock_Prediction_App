from datetime import date
import streamlit as st
import yfinance as yf


from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objs as go 

import pandas as pd

START = "2014-01-01"
TODAY = date.today().strftime("%Y-%m-%d")



#building the stock prediction app

st.title("Stock Prediction App")
st.subheader('by Rutuja Jadhav')
st.text('About')
st.text('This app was created as a Portfolio project to predict the stock prices from a given selection of tickers. You can read more about this project on the README file available on my Git Hub here - https://github.com/rutuja-jadhav-github/Stock_Prediction_App/blob/main/README.md. If you like this work, please leave me a star on the GitHub repository :) To learn more about building data apps for your portfolio check out @patloeber on You Tube.')


stocks = ('AAPL','GOOG','MSFT','GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:',1,5)

period = n_years * 365 #this will be used later as the period for which we want to predict the stock price


#load_data accepts a selected stock and returns a pandas df of the stock from yfinance.
def load_data(ticker):
    data = yf.download(ticker, START, TODAY) #downloads ticker data based on stock selected from start date until today in a pandas dataframe.
    data.reset_index(inplace=True)
    return data


data_load_state = st.text("Load data...")
data = load_data(selected_stock) #calling load_data to pass the selected stock
data_load_state.text("Loading data...done!")


#Display the pulled dataframe with latest values
st.subheader('Raw Data')
st.write(data.tail())


#Plottin the data from start date till today for open and close price
def plot_raw_data():
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close', line=dict(color='red')))
    fig.layout.update(title_text = 'Time Series Data (till present day)', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    graph_instruction = st.text('Drag the ends of the slider to zoom in on a specific period')


plot_raw_data()

#Forecasting

df_train = data[['Date','Close']]
df_train = df_train.rename(columns = {'Date':"ds","Close":"y"}) #renaming cols because prophet expects this in a certain format

m = Prophet() #calling the class constructor for instantiating a new Prophet model object. Any settings to the forecasting procedure are passed into the constructor. 

m.fit(df_train) #fit method fits the historic training data and starts training similar to sklearn

future = m.make_future_dataframe(periods= period)
#takes the model object and a number of periods to forecast and produces a df with column 'ds' containing future dates as rows.

forecast = m.predict(future) #The predict method will assign each row in future df a predicted value which it names yhat. 

#Display the forecast data
st.subheader('Forecast data')
st.write(forecast.tail())

#Plot the forecast data in plotly chart
st.write('Forecast data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast components')
fig2 = m.plot_components(forecast)
st.write(fig2)#not a plotly chart so we dont need to write plotly_chart


