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

data = pd.read_csv(r"C:\Users\Griffin\OneDrive - Trinity College Dublin\Year 4, Semester 1\Data Visualization\CS7DataVisualization\Assignment1WindowsVersion\gapminder.csv")

#Filter for 2002 data
data_2002 = data[data['year'] == 2002]


#Chart 1
plt.figure(figsize=(8, 4.5))

#Create the bubble plot
sns.scatterplot(data=data_2002, x='gdpPercap', y='lifeExp', size='pop', sizes=(100, 1000),
                color='gray', alpha=0.6, legend=False)  # Transparent bubbles with alpha

#Highlight Ireland in green
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=data_2002[data_2002['country'] == 'Ireland']['pop']/1e5,  # Adjust size according to population
            color='green', alpha=0.8, label='Ireland')  # Slightly more opaque for emphasis

#Labels and such
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Bubble Size = Population, 2002)')

#Add the gridlines
plt.grid(True)

#creates a custom legend
pop_sizes = [1e7, 5e7, 1e8]
population_legend = [plt.scatter([], [], s=size/1e5, color='gray', alpha=0.6, label=f'{int(size/1e6)}M') for size in pop_sizes]

#Adds Irealnd to the legend
ireland_legend = plt.scatter([], [], s=data_2002[data_2002['country'] == 'Ireland']['pop']/1e5, 
                             color='green', alpha=0.8, label='Ireland')

#Adds the pop size to the legend
plt.legend(handles=population_legend + [ireland_legend], 
           title='Population Size', loc='lower right', 
           prop={'size': 12}, title_fontsize='10', borderpad=1.5, labelspacing=1.2)  # Adjusting spacing

plt.show()


#Chart 2
plt.figure(figsize=(8, 4.5))

#Create the color coded scatter plot
sns.scatterplot(data=data_2002[data_2002['country'] != 'Ireland'], 
                x='gdpPercap', 
                y='lifeExp', 
                hue='continent',
                size='pop', 
                sizes=(100, 1000),
                palette='Set1',
                alpha=0.6,
                legend='brief')

#Highlight Ireland
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=data_2002[data_2002['country'] == 'Ireland']['pop']/5e4,
            color='green', alpha=0.8, label='Ireland')

#Labels and such
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Color by Continent, 2002)')

#Adds gridlines
plt.grid(True)

plt.legend(prop={'size': 8})

plt.show()

#Chart 3

#function to assign marker size and shape
def get_marker_and_color(pop):
    if pop > 1e8:
        return 'o', 'blue'
    elif pop > 1e7:
        return 's', 'red'
    else:
        return '^', 'purple'


plt.figure(figsize=(8, 4.5))

#Plot each point
for _, row in data_2002.iterrows():
    marker, color = get_marker_and_color(row['pop'])
    plt.scatter(row['gdpPercap'], row['lifeExp'], marker=marker, color=color, s=100, alpha=0.6)

#Highlight Ireland
plt.scatter(data_2002[data_2002['country'] == 'Ireland']['gdpPercap'],
            data_2002[data_2002['country'] == 'Ireland']['lifeExp'],
            s=200, marker='*', color='green', alpha=0.8, label='Ireland')

#Labels and such
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('GDP vs Life Expectancy (Shapes = Population, 2002)')

# Add gridlines
plt.grid(True)

#Creates customer legend for shapes
large_pop = mpatches.Patch(label='> 100M (Blue Circle)', facecolor='blue', edgecolor='black', alpha=0.6)
medium_pop = mpatches.Patch(label='10M - 100M (Red Square)', facecolor='red', edgecolor='black', alpha=0.6)
small_pop = mpatches.Patch(label='< 10M (Purple Triangle)', facecolor='purple', edgecolor='black', alpha=0.6)
ireland = mpatches.Patch(label='Ireland (Green Star)', facecolor='green', edgecolor='black', alpha=0.8)

#Moves legend to the bottom right
plt.legend(handles=[large_pop, medium_pop, small_pop, ireland], 
           title='Population', loc='lower right', prop={'size': 8})

plt.show()



