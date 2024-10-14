import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.interpolate import griddata

# Load the dataset
data = pd.read_csv("/Users/griff809/Library/CloudStorage/OneDrive-TrinityCollegeDublin/Year 4, Semester 1/Data Visualization/CS7DataVisualization/Assignment1/gapminder.csv")

# Filter the data for Ireland
data_ireland = data[data['country'] == 'Ireland']

# Set default figure size
plt.figure(figsize=(12, 6))

# Create a scatter plot
sns.scatterplot(data=data, x='year', y='lifeExp', hue='continent', size='pop', sizes=(50, 500),
                palette='Set1', alpha=0.7, legend=False)  # Disable default legend

# Highlight Ireland with distinct size and color
plt.scatter(data_ireland['year'], data_ireland['lifeExp'],
            s=data_ireland['pop']/1e5, color='green', alpha=0.9, label='Ireland')

# Create a color gradient for the area around data points based on GDP per capita
# Creating a grid for contour plot
x_grid = np.linspace(data['year'].min(), data['year'].max(), 100)
y_grid = np.linspace(data['lifeExp'].min(), data['lifeExp'].max(), 100)
X, Y = np.meshgrid(x_grid, y_grid)

# Interpolate GDP per capita values for the grid
gdp_values = data['gdpPercap'].values
grid_z = griddata((data['year'], data['lifeExp']), gdp_values, (X, Y), method='linear')

# Plot the contour with color based on GDP per capita
contour = plt.contourf(X, Y, grid_z, levels=15, cmap='viridis', alpha=0.3)

# Customize labels and title
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Year vs Life Expectancy (Bubble Size = Population, Color = Continent)')

# Set x-axis limits to expand the range slightly
plt.xlim(data['year'].min() - 1, data['year'].max() + 1)  # Adjust the limits as needed
plt.ylim(data['lifeExp'].min() - 3, data['lifeExp'].max() + 3)  # Adjust the limits as needed


# Add color bar for GDP per capita
cbar = plt.colorbar(contour)
cbar.set_label('GDP per Capita')

# Create a custom legend for continents and population sizes
plt.scatter([], [], label='Asia', marker='o', color='blue', alpha=0.7, s=100)
plt.scatter([], [], label='Europe', marker='o', color='green', alpha=0.7, s=100)
plt.scatter([], [], label='Africa', marker='o', color='red', alpha=0.7, s=100)
plt.scatter([], [], label='Americas', marker='o', color='purple', alpha=0.7, s=100)
plt.scatter([], [], label='Oceania', marker='o', color='orange', alpha=0.7, s=100)
plt.scatter([], [], label='Ireland', marker='o', color='green', s=100, alpha=0.9)

# Add a legend for population size bubbles
plt.scatter([], [], label='Population Size', marker='o', color='gray', s=200, alpha=0.5)

# Place the legend outside the plot area and move it further to the right
plt.legend(loc='upper left', bbox_to_anchor=(1.2, 1), title='Continents and Population Size')

# Add gridlines for clarity
plt.grid(True)

# Display the plot
plt.tight_layout()  # Adjust layout to make room for the legend
plt.show()
