#!/usr/bin/env python
# coding: utf-8

# # Exercise: queries into the state of electricity production and CO2 emissions in the United States

# In data science, we often need to have a sense of the idiosyncrasies of the data, how they relate to the questions we are trying to answer, and to use that information to help us to determine what approach, such as machine learning, we may need to apply to achieve our goal. This exercise provides practice in exploring a dataset and answering question that might arise from applications related to the data.
# 
# **Data**. The data for this problem can be found in the `data` folder. The filename is `egrid2016.xlsx`. This dataset is the U.S. Environmental Protection Agency's (EPA) [Emissions & Generation Resource Integrated Database (eGRID)](https://www.epa.gov/energy/emissions-generation-resource-integrated-database-egrid) containing information about all power plants in the United States, the amount of electricity they generate, what fuel they use, emissions produced, the location of the plant, and many more quantities. We'll be using a subset of those data.
# 
# The fields we'll be using include:					
#     
# |field    |description|
# |:-----   |:-----|
# |SEQPLT16 |eGRID2016 Plant file sequence number (the index)| 
# |PSTATABB |Plant state abbreviation|
# |PNAME    |Plant name |
# |LAT      |Plant latitude |
# |LON      |Plant longitude|
# |PLPRMFL  |Plant primary fuel |
# |CAPFAC   |Plant capacity factor |
# |NAMEPCAP |Plant nameplate capacity (Megawatts MW)|
# |PLNGENAN |Plant annual net generation (Megawatt-hours MWh)|
# |PLCO2EQA |Plant annual CO2 equivalent emissions (tons)|
# 
# For more details on the data, you can refer to the [eGrid technical documents](https://www.epa.gov/sites/default/files/2021-02/documents/egrid2019_technical_guide.pdf). For example, you may want to review page 45 and the section "Plant Primary Fuel (PLPRMFL)", which gives the full names of the fuel types including WND for wind, NG for natural gas, BIT for Bituminous coal, etc. Codebooks for data are common in data science when the variable names would otherwise be onerously long.
# 
# There also are a couple of "gotchas" to watch out for with this dataset:
# - The headers are on the second row and you'll want to ignore the first row (they're more detailed descriptions of the headers).
# - NaN values represent blanks in the data. These will appear regularly in real-world data, so getting experience working with it will be important.
# 
# **Your objective**. For this dataset, your goal is answer the following questions about electricity generation in the United States by constructing appropriate queries of the data:
# 
# 1. Which power plant generated the most energy in 2016 (measured in MWh)?
# 
# 2. Which power plant produced the most CO2 emissions (measured in tons)? 
# 
# 3. In what state is that plant located and what is its primary fuel?
# 
# 4. What is the name of the northern-most power plant in the United States? (hint: latitude is the quantity the measures north-south locations across the globe)
# 
# 5. What is the state where the northern-most power plant in the United States is located?
# 
# 6. Which state has the largest number of hydroelectric plants?
# 
# 7. Which state has the largest number of coal plants?
# 
# 8. Which state(s) have the fewest coal plants?
# 
# 9. Which fuel for generation produces the most energy (MWh) in the United States?
# 
# 10. Which fuel for generation produces the least energy (MWh) in the United States?
# 
# 11. Which fuel produces the most CO2 emissions in the United States?
