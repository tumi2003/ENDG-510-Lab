import pandas as pd # in case of error, install pandas using: pip install pandas
# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')
new_data = {
'Temp': 366,
'Humd': 901,
'Label': 0
}
df = df._append(new_data, ignore_index=True)
# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data.csv", index=False)
