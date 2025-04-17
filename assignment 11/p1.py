import pandas as pd
from datetime import datetime


date_time_obj = pd.Timestamp('2012-01-15')

specific_date_time = pd.Timestamp('2012-01-15 21:20:00')


local_date_time = pd.Timestamp.now()

date_without_time = pd.Timestamp('2012-01-15').date()

current_date = pd.Timestamp.now().date()

time_from_date_time = pd.Timestamp.now().time()

current_local_time = datetime.now().time()

print("Date Time Object:", date_time_obj)
print("Specific Date and Time:", specific_date_time)
print("Local Date and Time:", local_date_time)
print("Date Without Time:", date_without_time)
print("Current Date:", current_date)
print("Time from Date Time:", time_from_date_time)
print("Current Local Time:", current_local_time)