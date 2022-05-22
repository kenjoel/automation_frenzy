import pandas as pd

file = "/home/kenjoel/Downloads/athicor.csv"
required_columns = ["Hostname", "Device Policy", "Result"]

data_frame = pd.read_csv(file)
extraction = data_frame[required_columns]
new_excel = extraction.to_csv('newone.csv', index=False)

print(data_frame[required_columns])

# Filter data

# filter_df = data_frame.filter()

# Select Rows
passed = data_frame["Result"]

# Passed Percent
count_percent = passed.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
print(count_percent)
