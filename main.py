# main.py

import pandas as pd
from modules import user_input_date, previous_week_dates, previous_to_previous_week_dates, file_checker, file_reader, data_aggregator, data_analysis, data_colorizer


def process_week_dates(week_dates):
    print("\nChecking files for dates:")
    folder_name = "Data/Indice"

    index_names = [
        "Nifty 50",
        "Nifty Next 50",
        "Nifty Midcap 50",
        "Nifty Auto",
        "Nifty Bank",
        "Nifty Energy",
        "Nifty Financial Services",
        "Nifty FMCG",
        "Nifty IT",
        "Nifty Media",
        "Nifty Metal",
        "Nifty MNC",
        "Nifty Pharma",
        "Nifty PSU Bank",
        "Nifty Realty",
        "Nifty India Consumption",
        "Nifty Commodities",
        "Nifty Infrastructure",
        "Nifty PSE",
        "Nifty Services Sector",
        "Nifty CPSE",
        "Nifty Private Bank",
        "Nifty Oil & Gas",
        "Nifty Healthcare Index",
        "Nifty Consumer Durables"
    ]

    week_finalDf = pd.DataFrame(columns=['Index Name', 'Date Range', 'Open Index Value', 'High Index Value', 'Low Index Value', 'Closing Index Value', 'Volume', 'Change Percentage'])

    for indexName in index_names:
        print(f"\nProcessing data for {indexName}")

        # Create an empty dataframe to store the filtered data for the week
        aggregated_data = None

        for date in week_dates:
            file_pattern = f"ind_close_all_{date}.csv"
            matched_files = file_checker.find_files_on_desktop(
                folder_name, file_pattern)

            if matched_files:
                for file_path in matched_files:
                    # print(file_path)

                    # Read the file using the file_reader module
                    data = file_reader.read_file(file_path)

                    if data is not None:
                        # Filter rows for the current Index Name and current date
                        filtered_data = data[(data['Index Name'] == indexName)]

                        if not filtered_data.empty:
                            if aggregated_data is None:
                                # Initialize the aggregated_data dataframe with the first filtered data
                                aggregated_data = filtered_data.copy()
                            else:
                                # Append the filtered data to the aggregated_data dataframe
                                aggregated_data = pd.concat(
                                    [aggregated_data, filtered_data])

        if aggregated_data is not None:
            # Perform the aggregation operations for the whole week for the current Index Name
            aggregated_data = data_aggregator.aggregate_data(aggregated_data)
            
            data = []
            data.append(aggregated_data['Index Name'].iloc[0])
            data.append(aggregated_data['Date Range'].iloc[0])
            data.append(aggregated_data['Open Index Value'].iloc[0])
            data.append(aggregated_data['High Index Value'].max())
            data.append(aggregated_data['Low Index Value'].min())
            data.append(aggregated_data['Closing Index Value'].iloc[-1])
            data.append(aggregated_data['Volume'].max())
            data.append(((aggregated_data['Closing Index Value'].iloc[-1] - aggregated_data['Open Index Value'].iloc[0]) / aggregated_data['Open Index Value'].iloc[0]) * 100)
            

            newDf = pd.DataFrame(columns=['Index Name', 'Date Range', 'Open Index Value', 'High Index Value', 'Low Index Value', 'Closing Index Value', 'Volume', 'Change Percentage'], data=[data])
            week_finalDf = pd.concat([week_finalDf, newDf])

        else:
            print(f"No data found for {indexName} for the specified week.")

    return week_finalDf


def main():
    # Get user input for a date
    user_input = input("Enter a date in the format ddmmyyyy: ")
    user_date = user_input_date.get_user_input_date(user_input)
    range = []

    if user_date is not None:
        # Get previous to previous week dates
        prev_to_prev_week_dates = previous_to_previous_week_dates.get_previous_to_previous_week_dates(
            user_date)
        range.append(prev_to_prev_week_dates[0])
        # print("\nPrevious to previous week dates:")
        for date in prev_to_prev_week_dates:
            # print(date)
            pass

        # Get previous week dates
        prev_week_dates = previous_week_dates.get_previous_week_dates(
            user_date)
        range.append(prev_week_dates[-1])
        # print("Previous week dates:")
        for date in prev_week_dates:
            # print(date)
            pass

        # Process files for the first week
        week1 = process_week_dates(prev_to_prev_week_dates)
        

        # Process files for the second week
        week2 = process_week_dates(prev_week_dates)

        # Perform data analysis
        analysis_results = data_analysis.analyze_data(week1, week2)
        colored_results = data_colorizer.colorize_data(analysis_results)
        
        colored_results.to_excel(f'C:/Users/Pogo/Desktop/Output/Weekly Breakout/WB_ind_{str(range[0])} to {str(range[1])}.xlsx', index=False)
        


if __name__ == "__main__":
    main()
