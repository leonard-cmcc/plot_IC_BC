
                                                                         ###############################################################################
                                                                         ##                        Lecce 10/12/2024                                   ##
                                                                         ##         extract and plot runoff at the inland open boundary               ##
                                                                         ##                                                                           ##
                                                                         ###############################################################################


import pandas as pd
import matplotlib.pyplot as plt
import pdb # import the python debugger
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import pdb


    # change here when needed!
pathnamefig = '.../figures/48_chunks/' # fig path

# Initialize lists to store dates and runoff (discharge) values
dates = []
discharges = []

# Initialize lists to store extracted data
dates = []
discharges = []

# Open the file and read line by line
with open(".../river_runoff_pont.dat", "r") as file:

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

print('data=',data)
print('data=',data.shape)

# Filter data for the date range from 2 Jan 2019 to 02 Jan 2023
start_date = "2019-01-02"
end_date = "2023-01-02"
#end_date = "2020-01-02"


filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
# Plotting the data
plt.figure(figsize=(12,8))
#plt.plot(data['Date'], data['Discharge (m³/s)'], marker='o', linestyle='-', color='b')
plt.plot(filtered_data['Date'], filtered_data['Discharge (m³/s)'], linestyle='-', linewidth= '1.5', color='b')
# Set y-axis ticks and limits
plt.yticks(range(0, 8050, 500))  # Ticks from 500 to 8050 with an increment of 500
plt.ylim(0, 8050)  # Set the y-axis limits
plt.grid()
plt.title("INPUT FILE = runoff.dat",fontsize=18,weight='bold')
plt.legend()
plt.xlabel("Time")
# Add legend in the upper center
#plt.legend(loc='upper left')
plt.ylabel("Discharge (m³/s)")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.savefig(pathnamefig+'plot_input_river_daily', dpi=300, facecolor='w', edgecolor='w',
      orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1)
plt.close()
plt.show()
