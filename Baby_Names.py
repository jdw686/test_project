import pandas as pd
years = range(1880, 2018)
data = []
for y in years:
    fn = f'names/yob{y}.txt'
    df = pd.read_csv(fn, names=['Name', 'Gender', 'Amount'])
    df['Year'] = y
    data.append(df)
df = pd.concat(data)

# Creating New Columns
df['Name Length'] = [len(i) for i in df['Name']]

def first_letter(names_1):
    return names_1[0]
def last_letter(names_1):
    return names_1[-1]


df['Name First Letter'] = df['Name'].apply(first_letter)
df['Name Last Letter'] = df['Name'].apply(last_letter)
df['E-Occurrences'] = df['Name'].str.count('e')

# My favorite plot
import matplotlib.pyplot as plt
josh = df[df['Name'] == 'Joshua'].groupby('Year')['Amount'].sum()
plt.plot(josh, color='blue', linewidth=2.5, linestyle='solid')
plt.xlabel('Year')
plt.ylabel('Josh Babies per Year')
plt.title('Babies Named Josh Over Time')
plt.savefig('Josh Plot')