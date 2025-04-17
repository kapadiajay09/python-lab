import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()
lower_case = s.str.lower()
string_length = s.str.len()

print("Upper Case Values:\n", upper_case)
print("Lower Case Values:\n", lower_case)
print("Length of String Values:\n", string_length)