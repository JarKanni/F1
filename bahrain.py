import fastf1
import pandas as pd
from fastf1 import plotting
from matplotlib import pyplot as plt

## Load data ##
# fastf1 plotting setup
plotting.setup_mpl()

# enable cache for faster loading
fastf1.Cache.enable_cache('C:/Users/Admin/Coding/sports')
# load session, check event details
race = fastf1.get_session(2023, 1, 'R')
race.load()

# load data for analysis
bot = race.laps.pick_driver('BOT')
zho = race.laps.pick_driver('ZHO')


## Plotting ##
fig, ax = plt.subplots()
ax.plot(bot['LapNumber'], bot['LapTime'], color = 'blue')
ax.plot(zho['LapNumber'], zho['LapTime'], color = 'red')
ax.set_title('BOT vs ZHO')
ax.set_xlabel('Lap')
ax.set_ylabel('Lap Time')
plt.show()
