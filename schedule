import fastf1
import pandas as pd

# enable cache for faster loading
fastf1.Cache.enable_cache('C:/Users/Admin/Coding/sports')
# load full season schedule from fastf1
schedule_full = fastf1.get_event_schedule(2023)

##Cleaning##
# add Country into Location
schedule_full['Location'] = schedule_full['Location'] + ', ' + schedule_full['Country']

# convert EventDate to central time and change name to 'StartTime'
schedule_full['EventDate'] = schedule_full.EventDate + pd.DateOffset(hours = -11)


## Main schedule ##
schedule = schedule_full[['EventDate','RoundNumber','EventName','Location']]
schedule = schedule.set_index('RoundNumber')

schedule
