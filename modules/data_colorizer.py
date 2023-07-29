import pandas as pd
import seaborn as sns

def colorize_data(analysis_results):
    # Sort the DataFrame by 'Change Percentage' in descending order
    analysis_results.sort_values(by='Change %', ascending=False, inplace=True)

    # Apply the color functions to the 'Change %' and 'Volume Change (Times)' columns
    analysis_results_styled = analysis_results\
    .style\
    .background_gradient(subset =['Change %'],cmap='viridis', low=.5, high=0 )

    # Set the background color for headers
    header_style = {
        'selector': 'thead',
        'props': [('background-color', 'darkblue'), ('color', 'lightgrey')]
    }

    # Apply the styles to the DataFrame
    analysis_results_styled = analysis_results_styled.set_table_styles([header_style])

    return analysis_results_styled
