#mean reversion


import pandas as pd

# Load historical price data from a CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

# Mean reversion trading strategy
def mean_reversion_strategy(data, window, buy_threshold, sell_threshold):
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0  # 0 represents no action

    # Calculate rolling mean and standard deviation
    rolling_mean = data['Price'].rolling(window=window).mean()
    rolling_std = data['Price'].rolling(window=window).std()

    for i in range(window, len(data)):
        if data['Price'][i] < rolling_mean[i] - sell_threshold * rolling_std[i]:
            signals['Signal'][i] = 1  # Buy signal
        elif data['Price'][i] > rolling_mean[i] + buy_threshold * rolling_std[i]:
            signals['Signal'][i] = -1  # Sell signal
        else:
            signals['Signal'][i] = 0  # Hold signal

    return signals

if __name__ == '__main__':
    # Parameters
    csv_file = 'historical_data.csv'
    window = 20  # Rolling window for mean and standard deviation
    buy_threshold = 1.0  # Buy when price is above mean + buy_threshold * std
    sell_threshold = 1.0  # Sell when price is below mean - sell_threshold * std

    # Load data
    data = load_data(csv_file)

    # Generate trading signals
    signals = mean_reversion_strategy(data, window, buy_threshold, sell_threshold)

    # Save signals to a CSV file
    signals.to_csv('signals.csv')
