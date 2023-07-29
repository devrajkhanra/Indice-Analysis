import pandas as pd


def analyze_data(week1, week2):
    candle_pattern = ""
    # Create a new DataFrame to store the analysis results
    analysis_results = pd.DataFrame(
        columns=['Index Name', 'Vol Change(Times)', 'Change %', 'Candle Pattern'])

    # Get unique Index Names from both weeks
    unique_index_names = set(week1['Index Name'].unique()).union(
        week2['Index Name'].unique())

    for index_name in unique_index_names:
        # Filter data for the current Index Name from both weeks
        week1_data = week1[week1['Index Name'] == index_name]
        week2_data = week2[week2['Index Name'] == index_name]

        # Calculate volume change times for week2 over week1
        volume_change_times = week2_data['Volume'].sum(
        ) / week1_data['Volume'].sum()

        # Calculate change percentage for week2 over week1
        week1_open = week1_data['Open Index Value'].iloc[0]
        week1_close = week1_data['Closing Index Value'].iloc[-1]
        change_percentage = (
            (week2_data['Closing Index Value'].iloc[-1] - week1_open) / week1_open) * 100

        # Analyze candle pattern
        if week2_data['Open Index Value'].iloc[0] < week2_data['Closing Index Value'].iloc[-1]:
            if week2_data['High Index Value'].max() > week1_data['High Index Value'].iloc[0] and \
               week2_data['Low Index Value'].min() > week1_data['Low Index Value'].iloc[0] and \
               week2_data['Closing Index Value'].iloc[-1] > week1_data['High Index Value'].iloc[0]:
                candle_pattern = "HH"
            elif week2_data['High Index Value'].max() > week1_data['High Index Value'].iloc[0] and \
                    week2_data['Low Index Value'].min() > week1_data['Low Index Value'].iloc[0] and \
                    week2_data['Closing Index Value'].iloc[-1] < week1_data['High Index Value'].iloc[0]:
                candle_pattern = "HR"
            elif week2_data['High Index Value'].max() > week1_data['High Index Value'].iloc[0] and \
                    week2_data['Low Index Value'].min() < week1_data['Low Index Value'].iloc[0]:
                candle_pattern = "HV+"
            elif week2_data['High Index Value'].max() < week1_data['High Index Value'].iloc[0] and \
                    week2_data['Low Index Value'].min() > week1_data['Low Index Value'].iloc[0]:
                candle_pattern = "I+"

        elif week2_data['Open Index Value'].iloc[0] > week2_data['Closing Index Value'].iloc[-1]:
            if week2_data['High Index Value'].max() < week1_data['High Index Value'].iloc[0] and \
               week2_data['Low Index Value'].min() < week1_data['Low Index Value'].iloc[0] and \
               week2_data['Closing Index Value'].iloc[-1] < week1_data['Low Index Value'].iloc[0]:
                candle_pattern = "LL"
            elif week2_data['High Index Value'].max() < week1_data['High Index Value'].iloc[0] and \
                    week2_data['Low Index Value'].min() < week1_data['Low Index Value'].iloc[0] and \
                    week2_data['Closing Index Value'].iloc[-1] > week1_data['Low Index Value'].iloc[0]:
                candle_pattern = "LS"
            elif week2_data['High Index Value'].max() > week1_data['High Index Value'].iloc[0] and \
                    week2_data['Low Index Value'].min() < week1_data['Low Index Value'].iloc[0]:
                candle_pattern = "HV-"
            elif week2_data['High Index Value'].max() < week1_data['High Index Value'].iloc[0] and \
                    week2_data['Low Index Value'].min() > week1_data['Low Index Value'].iloc[0]:
                candle_pattern = "I-"
        

        # Append the analysis results to the DataFrame
        data = {
            'Index Name': [index_name],
            'Vol Change(Times)': [round(volume_change_times, 2)],
            'Change %': [round(change_percentage, 2)],
            'Candle Pattern': [candle_pattern]
        }
        new_row = pd.DataFrame(data)
        analysis_results = pd.concat(
            [analysis_results, new_row], ignore_index=True)

    return analysis_results
