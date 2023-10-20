import pandas as pd

# Load historical price data for the underlying asset from a CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

# Covered call options strategy
def covered_call_strategy(underlying_data, strike_price, call_option_premium):
    signals = pd.DataFrame(index=underlying_data.index)
    signals['Signal'] = 0  # 0 represents no action

    for date, row in underlying_data.iterrows():
        current_price = row['Price']

        if current_price >= strike_price:
            signals.loc[date, 'Signal'] = -1  # Sell a call option
            signals.loc[date, 'Call Option Premium'] = call_option_premium

    return signals

if __name__ == '__main__':
    # Parameters
    underlying_csv_file = 'underlying_asset_data.csv'
    strike_price = 120  # Strike price of the call option
    call_option_premium = 5.0  # Premium received from selling the call option

    # Load data for the underlying asset
    underlying_data = load_data(underlying_csv_file)

    # Generate trading signals
    signals = covered_call_strategy(underlying_data, strike_price, call_option_premium)

    # Save signals to a CSV file
    signals.to_csv('options_signals.csv')
