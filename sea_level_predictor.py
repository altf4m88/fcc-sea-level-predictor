import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', figsize=(12, 6))

    plt.title('Sea Level')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    plt.tight_layout()

    # Create first line of best fit
    from scipy.stats import linregress

    linear_regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_new = np.arange(df['Year'].min(), 2051)

    y_new = linear_regression.slope * x_new + linear_regression.intercept


    # Create second line of best fit
    data_post_2000 = df[df['Year'] >= 2000]

    x_post_2000 = data_post_2000['Year']
    y_post_2000 = data_post_2000['CSIRO Adjusted Sea Level']

    linregress_2000 = linregress(x_post_2000, y_post_2000)

    x_new_2000 = np.arange(2000, 2051)
    y_new_2000 = linregress_2000.slope * x_new_2000 + linregress_2000.intercept

    # Add labels and title
    plt.plot(x_new, y_new, color='red', label='Line of Best Fit (1880-2050)')
    plt.plot(x_new_2000, y_new_2000, color='blue', label='Line of Best Fit (2000-2050)')

    plt.legend()

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()