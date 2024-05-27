# Stock_Prediction_App

App link - https://stockpredictionapp-rj.streamlit.app/ 

Please open the link in a new tab - it may take a while to load. Apologies , Streamlit servers! In the meantime, you can read more about the app below. If it doesn't load, please drop me a line on my email or Linked In. Thanks:)

<img width="1273" alt="Screenshot 2024-05-27 at 15 42 31" src="https://github.com/rutuja-jadhav-github/Stock_Prediction_App/assets/160432263/250fa52d-35b7-4219-820f-3605f732d207">

<img width="1170" alt="Screenshot 2024-05-27 at 15 44 40" src="https://github.com/rutuja-jadhav-github/Stock_Prediction_App/assets/160432263/079c41b1-00d7-410f-8baa-8a5521b61cdc">

<img width="1253" alt="Screenshot 2024-05-27 at 15 45 30" src="https://github.com/rutuja-jadhav-github/Stock_Prediction_App/assets/160432263/bfd903a1-461b-415f-b81b-dfe52c0a97bb">


## Context
This app offers users the ability to predicted future stock prices for a selected stock. The app is built in Python using various widgets from Streamlit's library to design the front end. At the back end, the app uses Meta's Prophet framework to train the model based on past data of the chosen ticker and predict the corresponding stock prices for upto 5 years in the future.


## Choice of Approach - ARIMA vs Prophet vs LSTM-based RNN
After researching and analysing different forecasting methods, I shortlisted three which seemed most suitable for this use case - ARIMA, LSTM RNN and Prophet by Meta. Given that this was supposed to be a simple portfolio project, I decided to use Meta's Prophet algorithm over ARIMA and LSTM RNN for predicting stock prices.I opted for Prophet due to its robustness in handling seasonality and holidays, automatic outlier detection, ease of use, and interpretability (see sources linked in credits below). While ARIMA and LSTM have their strengths, Prophet's flexibility with missing data and user-friendly nature make it a more suitable choice for the dynamic and often irregular patterns in stock price data. 

ARIMA seemed to offer highest interpretiablity and was fit for purpuse with its efficacy in univariate anlysis. However, it required complex parameter tuning and offered limited flexibility for handling seasonality.
LSTM based RNN would have captured long-term dependencies and patterns in the data making it suitable for complex analysis for both univariate and multivariate forecasting. It would have also handled the seasonality aspect. Hwoever, using it for this project seemed computationlly intensive and seemed challenging in terms of parameter tuning and interpretiblity.
Therefore, Prophet seemed like a better fit for this use case given its ability to handle multiple seasonality patterns and holidays, interpretable components, and flexible with missing data. As caution, projects using Prophet should be wary about its assumption of additivity (default settings which can be configured for multiplicative effects in some cases). 


## Requirements
Python Libraries:
yfinance==0.2.40
plotly==5.22.0
prophet==1.1.5
streamlit==1.35.0
pandas==2.2.2


## Future Scope
While the app offers functional utility, from a research and improvement perspective, it would be ideal to rebuild it using other approaches and benchmark with efficiency metrics such as RMSE or MAPE to confirm if the Prophet algorithm indeed was the best fit for this use case.


## Credits 
https://www.sciencedirect.com/science/article/abs/pii/S0301421522003226#:~:text=In%20contrast%2C%20Fb%20Prophet%20performs,than%20CEA%20and%20Fb%20Prophet.

https://neptune.ai/blog/arima-vs-prophet-vs-lstm

Patrick Loeber on YouTube

https://facebook.github.io/prophet/docs/quick_start.html#:~:text=If%20you%20want%20to%20see,ll%20see%20those%20here%2C%20too.







