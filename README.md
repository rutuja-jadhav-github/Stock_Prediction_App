# Stock_Prediction_App
<img width="388" alt="Screenshot 2024-05-25 at 22 14 56" src="https://github.com/rutuja-jadhav-github/Stock_Prediction_App/assets/160432263/c6f1bda1-8509-4277-9e3e-8cb868c51db4">

[link](https://stockpredictionapp-rj.streamlit.app)

# Context

# Choice of Approach - ARIMA vs Prophet vs LSTM-based RNN
Based on my research and analysis of different forecasting methods, I decided to use the Meta's Prophet algorithm over ARIMA and LSTM RNN. for predicting stock prices.I opted for Prophet due to its robustness in handling seasonality and holidays, automatic outlier detection, ease of use, and interpretability. While ARIMA and LSTM have their strengths, Prophet's flexibility with missing data and user-friendly nature make it a more suitable choice for the dynamic and often irregular patterns in stock price data. 

Simple and interpretable.
Effective for univariate stationary time series.
Cons:

Requires stationary data and complex parameter tuning.
Limited flexibility for handling seasonality and trends.
-
Captures long-term dependencies and non-linear relationships.
Handles seasonality and trends automatically.

# Requirements

Cons:

Computationally intensive and requires large data sets.
Difficult to interpret (black-box nature).



