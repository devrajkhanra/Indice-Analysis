# modules/data_aggregator.py

import pandas as pd

def calculate_change_percentage(open_price, close_price):
    return ((close_price - open_price) / open_price) * 100

def aggregate_data(filtered_data):
    # Create an empty DataFrame to store the aggregated data
    aggregated_data_df = pd.DataFrame(columns=['Index Name', 'Index Date', 'Open Index Value', 'High Index Value', 'Low Index Value', 'Closing Index Value', 'Volume', 'Change(%)'])

    # Convert the required columns to appropriate data types
    filtered_data = filtered_data.copy()
    filtered_data['Open Index Value'] = filtered_data['Open Index Value'].astype(float)
    filtered_data['High Index Value'] = filtered_data['High Index Value'].astype(float)
    filtered_data['Low Index Value'] = filtered_data['Low Index Value'].astype(float)
    filtered_data['Closing Index Value'] = filtered_data['Closing Index Value'].astype(float)
    filtered_data['Volume'] = filtered_data['Volume'].astype(int)

    # Group the filtered data by 'Index Name'
    grouped_data = filtered_data.groupby('Index Name')

    for index_name, index_group in grouped_data:
        # Append the data of each Index Name for the whole week to the aggregated DataFrame
        aggregated_data_df = pd.concat([aggregated_data_df, index_group])

    # Calculate the change percentage for the entire week
    # aggregated_data_df['Change Percentage'] = calculate_change_percentage(aggregated_data_df['Open Index Value'], aggregated_data_df['Closing Index Value'])

    # Calculate the date range for each week
    start_date = aggregated_data_df['Index Date'].iloc[0]
    end_date = aggregated_data_df['Index Date'].iloc[-1]
    aggregated_data_df['Date Range'] = f"{start_date} - {end_date}"

    # Reset the index of the DataFrame
    aggregated_data_df.reset_index(drop=True, inplace=True)

    # Drop unnecessary columns and reorder the columns
    # aggregated_data_df = aggregated_data_df.drop(['Open Index Value', 'High Index Value', 'Low Index Value', 'Closing Index Value'], axis=1)
    aggregated_data_df = aggregated_data_df[['Index Name', 'Date Range', 'Open Index Value', 'High Index Value', 'Low Index Value', 'Closing Index Value', 'Volume', 'Change(%)']]
    

    return aggregated_data_df
