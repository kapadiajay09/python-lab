import pandas as pd

asking_prices = pd.Series([25000, 18000, 22000, 27000, 20000])
fair_prices = pd.Series([26000, 19000, 23000, 26500, 21000])

good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print("Good Deals Indices:", good_deals)