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

import matplotlib.font_manager as font_manager
import matplotlib.patches as mpatches

# Load the dataset
data = pd.read_csv("/Users/griff809/Library/CloudStorage/OneDrive-TrinityCollegeDublin/Year 4, Semester 1/Data Visualization/CS7DataVisualization/Assignment1/gapminder.csv")

# Filter data for the year 2002
data_2002 = data[data['year'] == 2002]


#Chart 1
# Set figure size for half an A4 page
plt.figure(figsize=(8, 4.5))

# Bubble plot with all countries in gray and transparent bubbles
sns.scatterplot(data=data_2002, x='gdpPercap', y='lifeExp', size='pop', sizes=(100, 1000),
                color='gray', alpha=0.6, legend=False)  # Transparent bubbles with alpha

# Highlight Ireland in green with its actual data point size and transparency
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=data_2002[data_2002['country'] == 'Ireland']['pop']/1e5,  # Adjust size according to population
            color='green', alpha=0.8, label='Ireland')  # Slightly more opaque for emphasis

# Customize labels and title
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Bubble Size = Population, 2002)')

# Add gridlines
plt.grid(True)

# --- Create custom legend for population sizes ---
pop_sizes = [1e7, 5e7, 1e8]  # 10M, 50M, and 100M
population_legend = [plt.scatter([], [], s=size/1e5, color='gray', alpha=0.6, label=f'{int(size/1e6)}M') for size in pop_sizes]

# Add Ireland to the legend
ireland_legend = plt.scatter([], [], s=data_2002[data_2002['country'] == 'Ireland']['pop']/1e5, 
                             color='green', alpha=0.8, label='Ireland')

# Add the population size legend and Ireland to the legend
plt.legend(handles=population_legend + [ireland_legend], 
           title='Population Size', loc='lower right', 
           prop={'size': 12}, title_fontsize='10', borderpad=1.5, labelspacing=1.2)  # Adjusting spacing

plt.show()


#Chart 2
# Set figure size for half an A4 page
plt.figure(figsize=(8, 4.5))

# Color-coded scatter plot based on continent, with larger transparent bubbles
sns.scatterplot(data=data_2002[data_2002['country'] != 'Ireland'], 
                x='gdpPercap', 
                y='lifeExp', 
                hue='continent',  # Color based on continent
                size='pop', 
                sizes=(100, 1000),  # Increase the size scaling for larger bubbles
                palette='Set1',     # You can choose any color palette
                alpha=0.6,          # Set transparency for all points
                legend='brief')

# Highlight Ireland in green with its actual data point size and transparency
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=data_2002[data_2002['country'] == 'Ireland']['pop']/5e4,  # Increase Ireland's size scaling for consistency
            color='green', alpha=0.8, label='Ireland')  # Slightly less transparent for emphasis

# Customize labels and title
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Color by Continent, 2002)')

# Add gridlines
plt.grid(True)

plt.legend(prop={'size': 8})

plt.show()

#Chart 3

# Create a function to assign marker styles and colors based on population size
def get_marker_and_color(pop):
    if pop > 1e8:
        return 'o', 'blue'  # Circle for large populations, colored blue
    elif pop > 1e7:
        return 's', 'red'   # Square for medium populations, colored red
    else:
        return '^', 'purple'  # Triangle for small populations, colored purple

# Set figure size for half an A4 page
plt.figure(figsize=(8, 4.5))

# Plot each point with a specific marker and color based on population
for _, row in data_2002.iterrows():
    marker, color = get_marker_and_color(row['pop'])
    plt.scatter(row['gdpPercap'], row['lifeExp'], marker=marker, color=color, s=100, alpha=0.6)  # Set transparency using alpha

# Highlight Ireland with a distinct shape and color
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=200, marker='*', color='green', alpha=0.8, label='Ireland')  # Slightly less transparent for emphasis

# Customize labels and title
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Shapes = Population, 2002)')

# Add gridlines
plt.grid(True)

# --- Create custom legend for Shapes ---
large_pop = mpatches.Patch(label='> 100M (Blue Circle)', facecolor='blue', edgecolor='black', alpha=0.6)
medium_pop = mpatches.Patch(label='10M - 100M (Red Square)', facecolor='red', edgecolor='black', alpha=0.6)
small_pop = mpatches.Patch(label='< 10M (Purple Triangle)', facecolor='purple', edgecolor='black', alpha=0.6)
ireland = mpatches.Patch(label='Ireland (Green Star)', facecolor='green', edgecolor='black', alpha=0.8)

# Add the custom legend for the shapes and move it to the bottom right
plt.legend(handles=[large_pop, medium_pop, small_pop, ireland], 
           title='Population', loc='lower right', prop={'size': 8})

plt.show()



