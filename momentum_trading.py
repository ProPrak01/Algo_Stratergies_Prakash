#momentum trading

import pandas as pd

# Load historical price data from a CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

# Momentum trading strategy
def momentum_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0  # 0 represents no action

    # Calculate short-term and long-term moving averages
    data['Short_MA'] = data['Price'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Price'].rolling(window=long_window).mean()

    for i in range(long_window, len(data)):
        if data['Short_MA'][i] > data['Long_MA'][i] and data['Short_MA'][i - 1] <= data['Long_MA'][i - 1]:
            signals['Signal'][i] = 1  # Buy signal
        elif data['Short_MA'][i] < data['Long_MA'][i] and data['Short_MA'][i - 1] >= data['Long_MA'][i - 1]:
            signals['Signal'][i] = -1  # Sell signal

    return signals

if __name__ == '__main__':
    # Parameters
    csv_file = 'historical_data.csv'
    short_window = 50  # Short-term moving average window
    long_window = 200  # Long-term moving average window

    # Load data
    data = load_data(csv_file)

    # Generate trading signals
    signals = momentum_strategy(data, short_window, long_window)

    # Save signals to a CSV file
    signals.to_csv('signals.csv')
