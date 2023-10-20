import pandas as pd

# Load historical price data and events from CSV files
def load_data(price_file, events_file):
    price_data = pd.read_csv(price_file)
    price_data['Date'] = pd.to_datetime(price_data['Date'])
    price_data.set_index('Date', inplace=True)

    events_data = pd.read_csv(events_file)
    events_data['Date'] = pd.to_datetime(events_data['Date'])
    events_data.set_index('Date', inplace=True)

    return price_data, events_data

# Event-driven trading strategy
def event_driven_strategy(price_data, events_data):
    signals = pd.DataFrame(index=price_data.index)
    signals['Signal'] = 0  # 0 represents no action

    for date, row in events_data.iterrows():
        event_date = date

        if event_date in price_data.index:
            # Buy signal on the event date
            signals.loc[event_date, 'Signal'] = 1
            # Sell signal on the day after the event
            if event_date + pd.DateOffset(days=1) in price_data.index:
                signals.loc[event_date + pd.DateOffset(days=1), 'Signal'] = -1

    return signals

if __name__ == '__main__':
    # Parameters
    price_csv_file = 'historical_price_data.csv'
    events_csv_file = 'events_data.csv'

    # Load data
    price_data, events_data = load_data(price_csv_file, events_csv_file)

    # Generate trading signals
    signals = event_driven_strategy(price_data, events_data)

    # Save signals to a CSV file
    signals.to_csv('event_signals.csv')
