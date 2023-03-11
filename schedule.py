import fastf1
import pandas as pd
from pandas.tseries.offsets import DateOffset
from datetime import datetime as dt

##Load Data##
# enable cache for faster loading
fastf1.Cache.enable_cache('C:/Users/Admin/Coding/sports')
# load full season schedule from fastf1
sch = fastf1.get_event_schedule(2023, include_testing = False)

##Cleaning##
# add Country into Location
sch['Location'] = sch['Location'] + ', ' + sch['Country']
# convert EventDate to central time and change name to 'StartTime'
sch['EventDate'] = sch.EventDate + pd.DateOffset(hours = -11)
# format StartTime to 'Month 01 @ 9AM'
sch['EventDate'] = sch['EventDate'].apply(lambda x: x.strftime('%B %d @ %I %p'))
# rename columns
sch.rename(columns = {'RoundNumber':'Round' , 'EventName':'Race', 'EventDate':'StartTime'}, inplace = True)


## Main schedule ##
# build schedule dataframe
schedule = sch[['Round', 'StartTime', 'Race','Location']]
schedule = schedule.set_index('Round')


print(schedule)
