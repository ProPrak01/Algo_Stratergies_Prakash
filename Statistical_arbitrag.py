import pandas as pd

# Load historical price data for two related assets from CSV files
def load_data(asset1_file, asset2_file):
    asset1_data = pd.read_csv(asset1_file)
    asset1_data['Date'] = pd.to_datetime(asset1_data['Date'])
    asset1_data.set_index('Date', inplace=True)

    asset2_data = pd.read_csv(asset2_file)
    asset2_data['Date'] = pd.to_datetime(asset2_data['Date'])
    asset2_data.set_index('Date', inplace=True)

    return asset1_data, asset2_data

# Statistical arbitrage trading strategy
def statistical_arbitrage_strategy(asset1_data, asset2_data, zscore_threshold):
    signals = pd.DataFrame(index=asset1_data.index)
    signals['Signal'] = 0  # 0 represents no action

    # Calculate the spread between the two assets
    spread = asset1_data['Price'] - asset2_data['Price']

    # Calculate the z-score of the spread
    zscore = (spread - spread.mean()) / spread.std()

    for i in range(1, len(asset1_data)):
        if zscore[i] > zscore_threshold:
            signals['Signal'][i] = -1  # Short asset1 and long asset2
        elif zscore[i] < -zscore_threshold:
            signals['Signal'][i] = 1  # Long asset1 and short asset2

    return signals

if __name__ == '__main__':
    # Parameters
    asset1_csv_file = 'asset1_price_data.csv'
    asset2_csv_file = 'asset2_price_data.csv'
    zscore_threshold = 2.0  # Entry/exit threshold for the z-score

    # Load data for the two assets
    asset1_data, asset2_data = load_data(asset1_csv_file, asset2_csv_file)

    # Generate trading signals
    signals = statistical_arbitrage_strategy(asset1_data, asset2_data, zscore_threshold)

    # Save signals to a CSV file
    signals.to_csv('stat_arb_signals.csv')
