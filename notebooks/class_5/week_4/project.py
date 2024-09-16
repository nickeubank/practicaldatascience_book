import pandas as pd
import matplotlib.pyplot as plt
from difflib import SequenceMatcher, get_close_matches

# Function to process CO2 data.
def process_co2(infile,outfile):
    # Read the data
    co2_all = pd.read_csv(infile)
    
    # Select the columns that we need and rename them for ease of reference
    co2 = co2_all[["country", "2017"]]
    co2 = co2.rename(columns={"2017": "co2"})
    
    # Output the resulting data
    co2.to_csv(outfile, index=False)


# Function to process income data
def process_income(infile,outfile):
    # Helper function to convert string data within the file into numerical data
    def string2num(string):
        if "k" in string:
            number = float(string[:-1]) * 1000
        else:
            number = float(string)
        return number
    
    # Read the file, select the columns of interest
    income_all = pd.read_csv(infile)
    income_2017 = income_all[["country", "2017"]]
    
    # Convert the textual data in the dataset into numerical data
    income = income_2017.copy(deep=True)
    income["2017"] = income_2017["2017"].apply(string2num)
    
    # Rename the columns to make them more readable and save the output to file
    income = income.rename(columns={"2017": "income"})
    income.to_csv(outfile, index=False)
    

def process_population(infile,outfile):
    # Helper function to convert string data within the file into numerical data
    def string2num(string):
        if "k" in string:
            number = float(string[:-1]) * 1000
        elif "M" in string:
            number = float(string[:-1]) * 1e6
        elif "B" in string:
            number = float(string[:-1]) * 1e9
        else:
            number = float(string)
        return number
    
    # Read the file, select the columns of interest
    pop_all = pd.read_csv(infile)
    pop_2017 = pop_all[["country", "2017"]]
    
    # Convert the textual data in the dataset into numerical data
    pop = pop_2017.copy(deep=True)
    pop["2017"] = pop_2017["2017"].apply(string2num)
    
    # Rename the columns to make them more readable and save the output to file
    pop = pop.rename(columns={"2017": "population"})
    pop.to_csv(outfile, index=False)
    
def process_continents(infile,outfile):
    # Helper function to convert string data within the file into numerical data
    
    continents_all = pd.read_csv(infile, sep=";")
    continent = continents_all[["Region Name", "Country or Area"]]
    continent = continent.rename(
        columns={"Region Name": "continent", "Country or Area": "country"}
    )
    continent = continent.sort_values(by=["country"])
    continent.to_csv(outfile, index=False)
    
    
def match(continent, data):

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def closest(a, B):
        return get_close_matches(a, list(B), n=1, cutoff=0)

    long = list(continent["country"].values)
    short = list(data["country"].values)
    long_strings = long.copy()
    short_strings = short.copy()

    # First pass, match those with exact subsets
    matches = []
    for ss in short:
        candidates = []
        for ls in long:
            if ss in ls:
                candidates.append(ls)
        if len(candidates) > 0:
            selected = closest(ss, candidates)[0]
            sim = similar(ss, selected)
            long_strings.remove(selected)
            short_strings.remove(ss)
            matches.append([ss, selected, 1])

    # Second pass, match what remains using proximity
    slength = len(short_strings)
    while slength > 0:
        matching_options = []
        similarity = []
        for ss in short_strings:
            selected = closest(ss, long_strings)[0]
            similarity.append(similar(ss, selected))
            matching_options.append([ss, selected])
        x = 1
        max_index = similarity.index(max(similarity))
        sim = max(similarity)
        long_strings.remove(matching_options[max_index][1])
        short_strings.remove(matching_options[max_index][0])
        matches.append([matching_options[max_index][0], matching_options[max_index][1], sim])
        slength = len(short_strings)
    
    # Retain matches with a similarirty score greater than 0.5
    for match in matches:
        if match[2] > 0.5:
            continent = continent.replace(match[1], match[0])
    
    return continent


def merge_data(co2_file, income_file, pop_file, continent_file,outfile):
    # Load the data
    co2 = pd.read_csv(co2_file)
    income = pd.read_csv(income_file)
    pop = pd.read_csv(pop_file)
    continent = pd.read_csv(continent_file)
    
    # Merge CO2 and income:
    data = pd.merge(co2, income, how="inner", on="country")
    
    # Next merge in population:
    data = pd.merge(data, pop, how="inner", on="country")
    
    # Next align the continents data for merging, then merge it in:
    continent = match(continent, data)
    data = pd.merge(data, continent, how="left", on="country")
    
    # Manually adjust the unmatched continents:
    data.at[35, "continent"] = "Africa"
    data.at[72, "continent"] = "Asia"
    data.at[90, "continent"] = "Asia"
    data.at[94, "continent"] = "Asia"
    data.at[140, "continent"] = "Asia"
    data.at[177, "continent"] = "Asia"
    
    # Replace Oceania with Asia:
    data["continent"] = data["continent"].replace("Oceania", "Asia")
    
    # Save to file
    data.to_csv(outfile, index=False)


# Create a scatterplot of per capita emissions vs per capita GDP:
def plot_emissions_gdp(infile,outfile):
    data = pd.read_csv(infile)

    region = ["Africa", "Asia", "Europe", "Americas"]
    color = ["#00d5e9", "#ff5872", "#ffe700", "#84ec04"]

    # Create a color list for each country that corresponds to the assigned color of the continent
    color_list = []
    for ir, r in enumerate(data.continent.values):
        for ireg, reg in enumerate(region):
            if r == reg:
                color_list.append(color[ireg])

    # Create "fake" plot elements to generate custom legend entries
    fig, ax = plt.subplots()
    legend_elements = []
    for r, c in zip(region, color):
        legend_elements.append(
            ax.plot(
                [],
                [], # Coordinates of the item to plot (we leave this blank so it doesn't actually plot anything)
                linewidth=0,  # removes the line
                marker="o",  # Sets our plot to be a circle
                color="black",  # Sets the edge color of the marker
                label=r,  # The label we want for this legend entry
                markerfacecolor=c,  # The color of the inside of the marker
                markersize=10,  # Pick a size the looks readable on the plot
            )[0] # Since the plot method returns a list of Line2D objects, we select the first (and in this case only) entry
        )
    
    fig, ax = plt.subplots(figsize=(10, 10))
    z = ax.scatter(
        x=data.income,
        y=data.co2,
        s=data.population / 100000,
        alpha=0.7,
        color=color_list,
        edgecolors="black",
    )
    ax.set(
        xlabel="Income Per Capita (GDP per person in USD)",
        ylabel="Carbon Dioxide Emissions per person (metric tonnes)",
        xscale="log",
        yscale="log",
    )
    ax.grid(which="both")
    ax.set_axisbelow(True)
    ax.legend(handles=legend_elements)

    fig.savefig(outfile, dpi=300, bbox_inches='tight')