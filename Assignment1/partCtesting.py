import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("/Users/griff809/Library/CloudStorage/OneDrive-TrinityCollegeDublin/Year 4, Semester 1/Data Visualization/CS7DataVisualization/Assignment1/gapminder.csv")

# Filter the data for Ireland
data_ireland = data[data['country'] == 'Ireland']

# Set default figure size (half A4 page)
plt.figure(figsize=(8, 4.5))

# Create a scatter plot with multiple encodings (similar to the provided image)
sns.scatterplot(data=data, x='year', y='lifeExp', hue='continent', size='pop', sizes=(50, 500),
                palette='Set1', alpha=0.7, legend='brief')

# Highlight Ireland with distinct size and color
plt.scatter(data_ireland['year'], data_ireland['lifeExp'],
            s=data_ireland['pop']/1e5, color='green', alpha=0.9, label='Ireland')

# Customize labels and title
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Year vs Life Expectancy (Bubble Size = Population, Color = Continent)')

# Add gridlines for clarity
plt.grid(True)

# Show the legend (population sizes and continent colors)
plt.legend(loc='best', prop={'size': 8})

# Display the plot
plt.show()