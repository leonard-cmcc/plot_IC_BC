

                                                                         ###############################################################################
                                                                         ##                        Lecce 06/11/2024                                   ##
                                                                         ##         extract and plot temperature at the inland open boundary          ##
                                                                         ##                                                                           ##
                                                                         ###############################################################################
# import libraries needed
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
# import traceback  #useful to track error
import pdb # import the python debugger
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Load the xlsx file and prepare the data
filename = '/home/olabileonard/BOLOGNA/PhD/Research/SHYFEM/init_bound_conditions/runoff_temp_station/temperature_pontolagoscuro_January.xlsx'
runoff = pd.read_excel(filename, skiprows=[1])
runoff.index = pd.to_datetime(runoff['Unnamed: 0'])
del runoff['Unnamed: 0']

# Calculate daily mean temperature
runoff_daily = runoff['Temperatura dell acqua istantanea (°C)'].resample('1D').mean()

# Define the start and end dates
date0 = datetime(2022, 1, 1, 12, 0, 0)
date1 = datetime(2022, 1, 31, 12, 0, 0)
generic_dates = True

if generic_dates:
    # Initialize arrays for daily data
    generic_runoff = []
    dates = []

    date = date0
    while date <= date1:
        # Select the daily mean value from runoff_daily
        daily_value = runoff_daily.loc[(runoff_daily.index.month == date.month) & (runoff_daily.index.day == date.day)]
        if not daily_value.empty:
            generic_runoff.append(daily_value.iloc[0])
            dates.append(date)
        date += timedelta(days=1)

    # Create df_runoff with generic dates
    df_runoff = pd.DataFrame({
        'Temperatura dell acqua istantanea (°C)': generic_runoff,
        'Datetime': pd.to_datetime(dates)
    })
    df_runoff.set_index('Datetime', inplace=True)
else:
    # Directly use runoff_daily if generic_dates is False
    df_runoff = runoff_daily.copy()

print(df_runoff)

plt.figure(figsize=(12, 6))
plt.plot(df_runoff,linewidth=3, marker='o', color="r", label="TEMP")

plt.xlabel("January 2022")
plt.ylabel("Daily mean Temperature [°C]")
plt.title("INLAND TEMP (OB)")
plt.legend()
# Set x-axis to show only January 2022
plt.xlim(datetime(2022, 1, 1), datetime(2022, 1, 31))
# Configure the x-axis to display daily ticks
plt.grid(True, which='major', axis='both', linestyle='--', linewidth=0.5)
plt.ylim(5, 8)

# Customize grid with smaller divisions on the y-axis
plt.grid(which='both', axis='y', linestyle='--', linewidth=2)
plt.minorticks_on()  # Enables minor ticks for more divisions
plt.grid(which='minor', axis='y', linestyle=':', linewidth=1.5)  # Fine grid for minor ticks


# Formatting the x-axis to show only days
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))  # Format to display only the day
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) # Format to display yy%mm%dd
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.DayLocator())

# Rotate date labels for readability
plt.xticks(rotation=45)
# Save the figure to a file
plt.savefig("/home/olabileonard/BOLOGNA/PhD/Research/SHYFEM/init_bound_conditions/scripts/figures/temp_river.png", format="png", dpi=300)













