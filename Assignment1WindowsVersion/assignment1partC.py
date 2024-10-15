import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.interpolate import griddata

data = pd.read_csv(r"C:\Users\Griffin\OneDrive - Trinity College Dublin\Year 4, Semester 1\Data Visualization\CS7DataVisualization\Assignment1WindowsVersion\gapminder.csv")

#Filter data for Ireland
data_ireland = data[data['country'] == 'Ireland']

#Set half A4 size
plt.figure(figsize=(12, 6))

#Create the scatter plot
sns.scatterplot(data=data, x='year', y='lifeExp', hue='continent', size='pop', sizes=(50, 500),
                palette='Set1', alpha=0.7, legend=False)  # Disable default legend

#Highlight ireland so it is visible
plt.scatter(data_ireland['year'], data_ireland['lifeExp'],
            s=data_ireland['pop']/1e5, color='green', alpha=0.9, label='Ireland')

x_grid = np.linspace(data['year'].min(), data['year'].max(), 100)
y_grid = np.linspace(data['lifeExp'].min(), data['lifeExp'].max(), 100)
X, Y = np.meshgrid(x_grid, y_grid)

#Get the GDP per capita values to plot
gdp_values = data['gdpPercap'].values
grid_z = griddata((data['year'], data['lifeExp']), gdp_values, (X, Y), method='linear')

#Plots the color based on GDP per capita
contour = plt.contourf(X, Y, grid_z, levels=15, cmap='viridis', alpha=0.3)

#labels and such
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Year vs Life Expectancy (Bubble Size = Population, Color = Continent)')

#change the range of the axes
plt.xlim(data['year'].min() - 1, data['year'].max() + 1)  # Adjust the limits as needed
plt.ylim(data['lifeExp'].min() - 3, data['lifeExp'].max() + 3)  # Adjust the limits as needed


# adds the color bar for the GDP gradient
cbar = plt.colorbar(contour)
cbar.set_label('GDP per Capita')

# Create custom legend
plt.scatter([], [], label='Asia', marker='o', color='blue', alpha=0.7, s=100)
plt.scatter([], [], label='Europe', marker='o', color='green', alpha=0.7, s=100)
plt.scatter([], [], label='Africa', marker='o', color='red', alpha=0.7, s=100)
plt.scatter([], [], label='Americas', marker='o', color='purple', alpha=0.7, s=100)
plt.scatter([], [], label='Oceania', marker='o', color='orange', alpha=0.7, s=100)
plt.scatter([], [], label='Ireland', marker='o', color='green', s=100, alpha=0.9)

plt.scatter([], [], label='Population Size', marker='o', color='gray', s=200, alpha=0.5)

#puts the legend to the right of the plot
plt.legend(loc='upper left', bbox_to_anchor=(1.2, 1), title='Continents and Population Size')

# Adds gridlines
plt.grid(True)

# displays the plot
plt.tight_layout() 
plt.show()
