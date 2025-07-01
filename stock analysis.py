import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Stock Price Visualizer", layout="wide")


st.title("📈 Stock Price Visualization App")


st.sidebar.header("User Input Features")


ticker = st.sidebar.text_input("Stock Ticker (e.g. AAPL, MSFT, TSLA):", value="AAPL").upper()


start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))


ma_window = st.sidebar.slider("Moving Average Window (days)", min_value=5, max_value=50, value=20)


st.write(f"### Showing data for: {ticker} from {start_date} to {end_date}")
data_load_state = st.text('Loading data...')
stock_data = yf.download(ticker, start=start_date, end=end_date)
data_load_state.text('Loading data...done!')


if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(stock_data)


st.subheader("Summary Statistics")
st.write(stock_data.describe())


stock_data['MA'] = stock_data['Close'].rolling(window=ma_window).mean()


st.subheader("Closing Price with Moving Average")
sns.set(style="darkgrid")
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['MA'], label=f'{ma_window}-Day MA', linestyle='--')
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title(f"{ticker} Closing Price and {ma_window}-Day Moving Average")
plt.legend()
st.pyplot(plt)
