#Choose a visual encoding channel to express GDP (gdpPercap) and life expectancy 

#(lifeExp) respectively (e.g. x-position-position). Use the same channel for these 
#attributes in all charts of Part A

#Then create 3 variants of the charts that encode, the quantitative attribute 
#population (pop) using 3 other encoding channels. 

#✦ Ensure that Ireland is distinguishable from other countries (BUT it is not required 
#that every single country is identifiable i.e., other data points can be anonymous)

#✦ Each chart must created for viewing as a figure no larger than half an A4 page 

#✦ It is optional to visualize the remaining attributes in this part.

#✦ You are only required to visualize 2002 data for this part.

#✦ In max half a page, add some brief text stating the tool(s) used for creating the 
#visualizations. Discuss briefly your opinion on the efficacy of the visualizations in 
#Charts #1 – 3.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("/Users/griff809/Library/CloudStorage/OneDrive-TrinityCollegeDublin/Year 4, Semester 1/Data Visualization/CS7DataVisualization/Assignment1/gapminder.csv")

# Filter data for the year 2002
data_2002 = data[data['year'] == 2002]

# Set figure size for half an A4 page
plt.figure(figsize=(8, 4.5))

#plot 1
# Bubble plot
sns.scatterplot(data=data_2002, x='gdpPercap', y='lifeExp', size='pop', sizes=(20, 200),
                hue='country', palette='muted', legend=False)

#highlight ireland so that it is easily found on the plot
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=200, color='red', label='Ireland')

#change the labels on the axes and adds a title to the graph
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Bubble Size = Population, 2002)')
plt.legend()

plt.show()


#Chart 2
# Set figure size for half an A4 page
plt.figure(figsize=(8, 4.5))

# Color-coded scatter plot
sns.scatterplot(data=data_2002, x='gdpPercap', y='lifeExp', hue='pop', size='pop',
                sizes=(20, 100), palette='viridis', legend=False)

# Highlight Ireland
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=200, color='red', label='Ireland')

# Customize labels and title
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Color = Population, 2002)')
plt.legend()

plt.show()



#Chart 3
# Create a function to assign marker styles based on population size
def get_marker(pop):
    if pop > 1e8:
        return 'o'  # Circle for large populations
    elif pop > 1e7:
        return 's'  # Square for medium populations
    else:
        return '^'  # Triangle for small populations

# Set figure size for half an A4 page
plt.figure(figsize=(8, 4.5))

# Plot each point with a specific marker based on population
for _, row in data_2002.iterrows():
    plt.scatter(row['gdpPercap'], row['lifeExp'], marker=get_marker(row['pop']),
                s=100, color='blue')

# Highlight Ireland with a distinct shape and color
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=200, marker='*', color='red', label='Ireland')

# Customize labels and title
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Shapes = Population, 2002)')
plt.legend()

plt.show()
