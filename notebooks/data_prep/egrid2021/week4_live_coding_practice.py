#############
# What states have the most inefficient power plants
# and what states have the

import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)

plants = pd.read_csv("eGRID2021_livecoding.csv", skiprows=[1])
plants.head()
for c in plants.columns:
    print(c)

# drop first row, change vars
# open csv, drop row
# read_csv

columns_to_keep = [
    "Plant name",
    "Plant state abbreviation",
    "Plant primary fuel",
    "Plant primary fuel category",
    "Plant annual CO2 equivalent emissions (tons)",
    "Plant annual CO2 equivalent total output emission rate (lb/MWh)",
    "Plant annual net generation (MWh)",
]

plants = plants[columns_to_keep]
plants.sample(5)
plants.info()

plants.loc[
    plants["Plant annual CO2 equivalent emissions (tons)"].isnull(),
    "Plant primary fuel category",
].value_counts()


for output in [
    "Plant annual CO2 equivalent emissions (tons)",
    "Plant annual CO2 equivalent total output emission rate (lb/MWh)",
]:
    plants.loc[
        plants["Plant primary fuel category"].isin(
            ["SOLAR", "HYDRO", "WIND", "BIOMASS", "NUCLEAR", "GEOTHERMAL"]
        )
        & plants[output].isnull(),
        output,
    ] = 0


plants = plants.rename(
    columns={
        "Plant annual CO2 equivalent emissions (tons)": "co2",
        "Plant annual CO2 equivalent total output emission rate (lb/MWh)": "co2_per_mwh",
    }
)


plants["co2"] = plants["co2"].str.replace(",", "").astype("float")
plants["co2"].describe() / 1_000
plants["co2_per_mwh"]
