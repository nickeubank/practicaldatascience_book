######################
#
# Import World Development Indicators
# and look at the relationship between income
# and health outcomes across countries
#
######################

# Download World Development Indicators
wdi <- read.csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")

# Get Mortality and GDP per capita for 2015
wdi$loggdppercap <- log(wdi[["GDP.per.capita..constant.2010.US.."]])

# Plot
library(ggplot2)
ggplot(
    wdi,
    aes(
        x = loggdppercap,
        y = Mortality.rate..under.5..per.1.000.live.births.
    )
) +
    geom_point() +
    geom_label(aes(label = Country.Name)) +
    geom_smooth()
