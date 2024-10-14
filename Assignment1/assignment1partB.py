import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("/Users/griff809/Library/CloudStorage/OneDrive-TrinityCollegeDublin/Year 4, Semester 1/Data Visualization/CS7DataVisualization/Assignment1/gapminder.csv")

# Filter the data for life expectancy and year
data_ireland = data[data['country'] == 'Ireland']  # Filter for Ireland

# Set default figure size (half A4 page)
plt.figure(figsize=(8, 4.5))

#Chart 1 - Color
plt.figure(figsize=(8, 4.5))
sns.scatterplot(data=data, x='year', y='lifeExp', hue='continent', palette='Set1', alpha=0.6)
plt.scatter(data_ireland['year'], data_ireland['lifeExp'], color='green', s=100, label='Ireland')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Year vs Life Expectancy (Color = Continent)')
plt.legend()
plt.grid(True)
plt.show()

#Chart 2 - Shape
plt.figure(figsize=(8, 4.5))
markers = {"Asia": "o", "Europe": "s", "Africa": "D", "Americas": "^", "Oceania": "P"}
sns.scatterplot(data=data, x='year', y='lifeExp', style='continent', markers=markers, palette='gray', alpha=0.6)
plt.scatter(data_ireland['year'], data_ireland['lifeExp'], color='green', marker='*', s=100, label='Ireland')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Year vs Life Expectancy (Shape = Continent)')
plt.legend()
plt.grid(True)
plt.show()

#Chart 3 - Size
plt.figure(figsize=(8, 4.5))
sns.scatterplot(data=data, x='year', y='lifeExp', size='continent', sizes=(50, 200), alpha=0.6, color='gray', legend='brief')
plt.scatter(data_ireland['year'], data_ireland['lifeExp'], color='green', s=150, label='Ireland', alpha=0.9)
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Year vs Life Expectancy (Size = Continent)')
plt.legend()
plt.grid(True)
plt.show()
