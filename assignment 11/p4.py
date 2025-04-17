import pandas as pd
import numpy as np

data = {
    'John': [True, False, True, False, True, True, False, False, True, False],
    'Judy': [False, True, True, False, True, False, False, True, True, True]
}

schedule = pd.DataFrame(data)

schedule['Party'] = schedule['John'] & schedule['Judy']
party_days = schedule.index[schedule['Party']].tolist()
schedule['days_til_party'] = np.zeros(len(schedule), dtype=int)

for i in schedule.index:
    if not schedule.loc[i, 'Party']:
        days_until = [(day - i) for day in party_days if day > i]
        schedule.loc[i, 'days_til_party'] = days_until[0] if days_until else -1

print(schedule)