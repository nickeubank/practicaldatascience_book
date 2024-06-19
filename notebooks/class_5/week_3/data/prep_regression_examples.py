import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

pd.set_option("mode.copy_on_write", True)

# Get WDI data.
wdi = pd.read_csv("wdi_small_tidy_2015.csv")

# Subset and clean names for patsy
wdi = wdi[
    [
        "Country Name",
        "GDP per capita, PPP (constant 2011 international $)",
        "CPIA transparency, accountability, and corruption in the public sector rating (1=low to 6=high)",
        "Mortality rate, under-5 (per 1,000 live births)",
        "Mortality rate, under-5, female (per 1,000 live births)",
        "Mortality rate, under-5, male (per 1,000 live births)",
        "Population, total",
    ]
].rename(
    columns={
        "Country Name": "country_name",
        "GDP per capita, PPP (constant 2011 international $)": "gdp_per_capita_ppp",
        "CPIA transparency, accountability, and corruption in the public sector rating (1=low to 6=high)": "CPIA_public_sector_rating",
        "Mortality rate, under-5 (per 1,000 live births)": "mortality_rate_under5_per_1000",
    }
)

# Mostly clean up to countries with data for regression
wdi = wdi[
    wdi["CPIA_public_sector_rating"].notnull()
    | wdi["CPIA_public_sector_rating"].isin(["Venezuela, RB", "Belize"])
    & (wdi.country_name.isin(["Virgin Islands (U.S.)"]))
]

# Add regions
regions = pd.read_csv("world-regions-according-to-the-world-bank.csv")
regions

wdi.loc[wdi.country_name == "Cabo Verde", "country_name"] = "Cape Verde"

wdi_regions = pd.merge(
    wdi,
    regions[["Entity", "World Region according to the World Bank"]],
    left_on="country_name",
    right_on="Entity",
    how="left",
    indicator=True,
    validate="1:1",
)
wdi_regions._merge.value_counts()
assert (wdi_regions._merge == "both").all()

wdi_regions = wdi_regions.drop(columns=["Entity", "_merge"])
wdi_regions = wdi_regions.rename(
    columns={"World Region according to the World Bank": "region"}
)


wdi_regions.to_csv("wdi_corruption.csv", index=False)
