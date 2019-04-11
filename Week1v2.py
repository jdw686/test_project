import pandas as pd

data = pd.read_csv('names/yob2000.txt', header=None, index_col=None)
data.columns = ['Name', 'Gender', 'Amount']
data.to_csv('Baby_Names.csv', index=None, header=True)

baby_names = pd.read_csv('Baby_Names.csv')
baby_names.head(10)  # 0724

# Calculate the sum of the birth count column in the file yob2000.txt.
baby_names_amount = baby_names['Amount'].sum()

# Calculate separate sums for boys and girls
gender_count = baby_names.groupby(["Gender"]).sum()

import matplotlib.pyplot as plt
# Plot both sums in a bar plot
gender_count.plot(kind='bar', ax=None, color='green', figsize=(8, 4))

# Count how many names occur at least 1000 times in the file yob2000.txt.
popular_baby_names = (baby_names['Amount'] > 1000).sum()

# Create a new column containing the percentage of a name on the total births of that year.
baby_names['Percentage'] = baby_names['Amount']/baby_names['Amount'].sum()
baby_names['Percentage'].sum() # verify that it is equal to 1.0/100%

# Identify and print all lines containing your name in the year 2000
baby_names[baby_names['Name'] == 'Joshua']

# Create a bar plot showing 5 selected names for the year 2000

# Concatenate baby names files for all years available
years = range(1880, 2018)
data = []
for y in years:
    fn = f'names/yob{y}.txt'
    df = pd.read_csv(fn, names=['Name', 'Gender', 'Amount'])
    df['Year'] = y
    data.append(df)
df = pd.concat(data)

#Create a line graph of your name over time
josh = df[df['Name'] == 'Joshua'].groupby('Year')['Amount'].sum()
plt.plot(josh, color='green', linewidth=1, linestyle='dashed')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Babies Named Josh Over Time')
plt.legend()
plt.savefig('Baby Plot')

# Create a line graph showing the diversity of baby names over time
diversity = df.groupby('Year')['Name'].count()
plt.plot(diversity, color='pink', linewidth=2, linestyle='dashed')
plt.xlabel('Year')
plt.ylabel('Amount of Names')
plt.title('Diversity of Names over Time')
plt.savefig('Diversity Plot')

# add an extra column that contains the length of the name
df['Name Length'] = [len(i) for i in df['Name']]

# print the ten largest names
df.nlargest(10, 'Name Length').sort_values(by='Name Length', ascending = False)

# create a line graph for a celebrity, i.e., Elvis
celebrity = df[df['Name'] == 'Elvis'].groupby('Year')['Amount'].sum()
plt.plot(celebrity, color='green', linewidth=1, linestyle='solid')
plt.xlabel('Year')
plt.ylabel('Elvis per Year')
plt.title('People named Elvis over time.')
plt.savefig('Elvis Plot')

# create a plot that shows the total birth rate in the U.S. over time
birth_by_year = df.groupby('Year')['Amount'].sum()
plt.plot(birth_by_year, color='red', linewidth=1, linestyle='dashdot')
plt.xlabel('Year')
plt.ylabel('Number of Births')
plt.title('Number of Births Over Time')
plt.savefig('Number of Births Over Time')

# separate the plot by gender
male_births = df[df['Gender'] == 'M'].groupby('Year')['Amount'].sum()
female_births = df[df['Gender'] == 'F'].groupby('Year')['Amount'].sum()
plt.plot(male_births, color='blue', linewidth=1, linestyle='solid')
plt.plot(female_births, color='pink', linewidth=1, linestyle='solid')
plt.xlabel('Year')
plt.ylabel('Births')
plt.title('Number of Births by Gender Over Time')
plt.savefig('Male and Female Births Over Time')