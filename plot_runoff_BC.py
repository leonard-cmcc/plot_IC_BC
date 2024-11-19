import re
import pandas as pd
import matplotlib.pyplot as plt
import pdb # import the python debugger
import matplotlib.dates as mdates
from datetime import datetime

    # change here when needed!
pathname = '/home/olabileonard/BOLOGNA/PhD/Research/SHYFEM/init_bound_conditions/input/'  # input path
pathnamefig = '/home/olabileonard/BOLOGNA/PhD/Research/SHYFEM/init_bound_conditions/scripts/figures/' # fig path

# Initialize lists to store dates and runoff (discharge) values
dates = []
discharges = []

# Open the file and read line by line
with open("/home/olabileonard/BOLOGNA/PhD/Research/SHYFEM/init_bound_conditions/input/river_runoff_pont.dat", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 6):  # Each block is 6 lines long
        if i + 3 < len(lines):  # Make sure there are enough lines
            date_line = lines[i + 1].strip()
            discharge_line = lines[i + 3].strip()

            # Parse date and discharge values
            date = pd.to_datetime(date_line, format='%Y%m%d %H%M%S')  #  convert date to %Y%m%d %H%M%S'
            discharge = float(discharge_line)

            # Append to lists
            dates.append(date)
            discharges.append(discharge)

# Create a DataFrame for plotting or further processing
data = pd.DataFrame({"Date": dates, "Discharge (m³/s)": discharges})

# Filter data for the date range from 6 Jan 2022 to 31 Jan 2022
start_date = "2022-01-01"
end_date = "2022-01-31"
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
# Plotting the data
plt.figure(figsize=(10, 5))
#plt.plot(data['Date'], data['Discharge (m³/s)'], marker='o', linestyle='-', color='b')
plt.plot(filtered_data['Date'], filtered_data['Discharge (m³/s)'], marker='o', linestyle='-', color='b')

# Customize grid with smaller divisions on the y-axis
plt.grid(which='both', axis='y', linestyle='--', linewidth=2)
plt.minorticks_on()  # Enables minor ticks for more divisions
plt.grid(which='minor', axis='y', linestyle=':', linewidth=1.5)  # Fine grid for minor ticks


plt.title("INPUT river Discharge ")
plt.xlabel("January 2022")
plt.ylabel("Discharge (m³/s)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
# Set x-axis to show only the day part of the date
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))  # Show only day number
# Ensure every day is displayed on the x-axis
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.savefig(pathnamefig+'plot_input_river', dpi=300, facecolor='w', edgecolor='w',
      orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1)
plt.close()
# Show the plot
plt.show()

