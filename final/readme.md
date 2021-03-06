# Final
The purpose of this assignment was to perform 5 analyses on a readily downloadable dataset. With global warming being such a *hot* topic lately, I chose to look into global temperature patterns and what might be causing those patterns.

## Analysis 1: Hot vs Cold
To start, I wanted to understand the dataset a bit more. First, I calculated the average temperature of the dataset of country temperature. According to that dataset, the average temperature of the globe is 17.5&deg;C. I then created a histogram of the country temperature dataset to get a feel for the distribution of temperatures around the world. That histogram is below.

<img align="center" src="analysis/ana_1/countryhistogram.png" width="600">

### Quadrants of the Globe
Next I wanted to answer a few simple questions like 'What are the hottest/coldest countries in the world?'. I started broad and separated cities into quadrants of the globe (North West, South West, North East, and South East.

<img src="analysis/ana_1/quadboxplot.png" width="600">

### Continents
From there I narrowed the categorization into continents and wanted to see the average temperature of each continent and how much the temperature varied; I used a boxplot to show that data. 

<img src="analysis/ana_1/continentboxplot2.png" width="600">

Overall I was surprised by how little the data for each continent varied on average, but how great the range of temperatures was for some continents like North America.

### Countries
Next I narrowed to a country level of focus to find the top five hottest and coldest countries in the world. The top five hottest countries in the world are Aruba(27.92&deg;C), Senegal( 27.96&deg;C), Burkina Faso(28.07&deg;C), Mali(28.44&deg;C), and Djibouti(28.82&deg;C). The variation across the top five hottest countries is only 0.90&deg;C.

<img src="analysis/ana_1/hotcountryboxplot.png" width="600">

The top five coldest countries in the world are Canada(-5.33&deg;C), Russia(-5.58&deg;C), Svalbard And Jan Mayen(-7.44&deg;C), Denmark(-18.05&deg;C), and Greenland(-18.58&deg;C). The variation of the top five coldest countries is 13.25&deg;C.

<img src="analysis/ana_1/coldcountryboxplot.png" width="600">

### Cities
Finally I went to a city level of granularity to find the top five hottest/coldest cities in the world. The hottest cities in the world are Kassala(28.92&deg;C), Niamey(29.04&deg;C), Umm Duran(29.06&deg;C), Khartoum(29.06&deg;C), and Jibuti(29.16&deg;C). The variation between the top five hottest countries is only 0.24&deg;C.

<img src="analysis/ana_1/hotcityboxplot.png" width="600">

The coldest cities in the world are Surgut(-3.53&deg;C), Ust Ilimsk(-4.00&deg;C), Chita(-4.36&deg;C), Kyzyl(-6.22&deg;C), and Norilsk(-11.84&deg;C). At 8.31&deg;C, the variation between the top five coldest countries is a bit more than the hottest countries. 

<img src="analysis/ana_1/coldcityboxplot.png" width="600">

Overall it would seem the hotter countries and cities don't vary in temperature as much, which could have something to do with their location; especially their distance from the equator. Generally, the close to the equator the country is, the more regular (and hotter) the temperatures will be. To get an idea of how the cities of the dataset are distributed, see the plot below.

<img src="analysis/ana_1/worldHeat.png" width="1000">

## Analysis 2: Largest Temperature Delta

For the next analysis I wanted to determine which countries had the greatest temperature delta from the beginning of data collection until now. The time range I had to work with was from 1750 to 2013. However, as I began comparing values, there was an issue. The recorded temperatures from the earlier end of the data were sporadic and the uncertainty was too high. To see what I mean, see the plot of the global temperature average pre year below. The dark line is the global average while the shaded region is the uncertainty of the temperature.

<img src="analysis/ana_2/globalAverage.png" width="600">

As you can see, the temperature recordings are all over the place until it stabilizes a bit between 1850 and 1900. To view the uncertainly levels in more detail, I plotted them below.

<img src="analysis/ana_2/uncertaintyPlot.png" width="600">

The global average uncertainty level begins to stabilize just before 1850. I decided to use 1850 as a cut-off date to use as much data possible while only using viable data. There are a few outliers in uncertainty after 1850, so I also removed any data points with an uncertainty greater than 1.5. I chose 1.5 because that is the value at which the uncertainty stabilizes around by 1850.

Once I had a more reliable set of data, I calculated the delta of average temperature change between 1850 and 2013. I was looking for an overall trend and due to the possible variation from year to year, I chose to use a 5 year average for the end points. The top five ten countries with the largest delta can be seen below. The plot of all countries deltas was too large for this markdown and can be viewed [here](analysis/ana_2/alldiffsPlot.png) if you'd like to.

<img src="analysis/ana_2/topTenDelta.png" width="750">

Next I wanted to get an idea of what the distribution of deltas was across the globe and so I plotted that below.

<img src="analysis/ana_2/deltahist.png" width="600">

Finally I wanted to see how the countries with the highest deltas compared to the global average and so I plotted them together. Plotting all ten would have been too much for one graph, so I only plotted the top five and averaged around 0&deg;C.

<img src="analysis/ana_2/globcomparison.png" width="1000">

They all tend to follow the same trend, although I would need to look further into the UAE data to determine if the rapid change in temperature from 1850 to 1880 is valid or representative of their data collection system at the time. Almost all countries seem to begin to stray from the average and climb around 1990. It would be interesting to look closer at what changes happened in those countries around that time. Another observation is the temperature changes between 1920 and 1950. All but the UAE seem to have large temperature changes in that time span, but not necessarily in the same direction.

## Analysis 3: Rate of Change
For this next analysis, I wanted to look at the rate of temperature change of each country over 3 year spans to determine if there were any specific events that drastically changed the temperature of a country. Again, due to data inconsistencies, I used the same time cut-off of 1850. The top ten temperature events were held by six different countries as can be seen in the bar graph below.

| Country     | Year | Temperature Change (&deg;C)| 
| ----------- |:----:|:------------------:|
|Saudi Arabia |1859  |9.31                |
|Saudi Arabia |1856  |-9.19               |
|Mauritania   |1853  |-7.13               |
|Mauritania   |1856  |6.91                |
|India        |1867  |5.24                |
|India        |1862  |-5.01               |
|Vietnam      |1865  |4.55                |
|Finland      |1941  |-4.53               |
|Vietnam      |1862  |-4.46               |
|Laos         |1865  |4.32                |

<img src="analysis/ana_3/topTenDiff.png" width="650">

For the countries that have two events of about the same temperature change, if you look at the years when they happened, some events are around the same time period. I graphed the temperature records for each country that had an event around the same time. Six of the top ten unique countries had events in a similar time frame.

<img src="analysis/ana_3/maxDiffs.png" width="750">

You can clearly see a severe dip in temperature from Saudi Arabia and Mauritania around the same time. However Mauritania dips in 1853 and rebounds in 1856 while Saudi Arabia dips in 1856 and rebounds in 1859. These events may not be related and could simply be a measurement error. Both countries measurements start close to that date, which would also point toward a potential measurement error.

India, Vietnam, Laos, and Burma, however, all have a dip between 1862 and 1865. This makes me think it is less of a measurement error and more of an event that caused a drastic dip in temperature. This would definitely warrant further investigation.

The remaining four of the top ten countries with events in similar time frames are graphed below.

<img src="analysis/ana_3/maxDiffs2.png" width="750">

These four countries follow a very similar temperature profile and one can clearly see a severe dip in temperature between 1941 and 1944. As before, seeing as this dip is displayed in all four countries, I'm inclined to think this is a true measurement and it would be interesting to investigate the cause. Beside that single event, the overall average temperature profile of these four countries seems to vary year to year more than the six from the other comparison. This follows what we saw in the first analysis with the colder climates varying more than the warmer climates. 

## Analysis 4: Effect of Gases on Temperature

After looking at different trends and events in global temperatures, I wanted to investigate a cause. The most mentioned cause in global warming are CO2 and other greenhouse gases. I decided to compare the emissions of CO2, NO2, and methane to the change in temperature between 1970 and 2013; the emissions data I found starts at 1970. The graph below is of the ten countries with the highest temperature delta between 1970 and 2013; a condensed time period relative to Analysis 2. 

<img src="analysis/ana_4/topSixDiffs.png" width="650">

To get an idea of what their temperature profiles look like during that time period, I wanted to graph the top five from the ten above. One of the top five countries, Saint Pierre and Miquelon, was excluded from further investigation, however, because the emissions dataset did not contain information for it. Therefore, I graphed the top six countries as to include the five that will be reviewed further down.

<img src="analysis/ana_4/maxDiffs.png" width="800">

The general trend is that the temperature is rising, but something to note is that Greenland and Denmark have nearly identical temperature patterns. This could be due to Greenland being a colony of Denmark's and so linking the two countries data together. 

### Greenland
I can't discern much by comparing the two graphs other than the temperature, methane, and NO2 all have the same upward trend.

<img src="analysis/ana_4/GreenlandTemp.png" width="720">
<img src="analysis/ana_4/GreenlandGases.png" width="750">

### Denmark
Denmark's emissions seem to be on the descent and much lower than they were in 1970 despite the rise in temperature. 

<img src="analysis/ana_4/DenmarkTemp.png" width="720">
<img src="analysis/ana_4/DenmarkGases.png" width="750">

### Canada
Canada's gas emissions are rather erratic and it's difficult to determine their effect on temperature.

<img src="analysis/ana_4/CanadaTemp.png" width="705">
<img src="analysis/ana_4/CanadaGases.png" width="750">

### Iran
Iran has a surprisingly steady increase in all gas emissions.

<img src="analysis/ana_4/IranTemp.png" width="690">
<img src="analysis/ana_4/IranGases.png" width="750">

### Armenia
Armenia has had an aggressive increase in both CO2 and NO2 since the mid-nineties. The sudden drop in all three gases in the early nineties may correlate to the dip in temperature around that same time.

<img src="analysis/ana_4/ArmeniaTemp.png" width="710">
<img src="analysis/ana_4/ArmeniaGases.png" width="750">


## Analysis 5: 
For my final analysis, I wanted to look at the gas correlation a different way. Rather than start with the largest rises in temperature over a period of time, I looked at the rate of change, over a five year period, in total gas emissions to see if there were trends in those countries' temperatures that were more apparent. The top 16 changes in total emissions were either in Indonesia or China and in the top 50 instances, 23 were China and 16 were Indonesia. For the sake of comparison, I've plotted the maximum changes of the top ten unique countries.

<img src="analysis/ana_5/topTenEmissions.png" width="700">

I then wanted to see what the top five countries emissions profiles looked like. 

<img src="analysis/ana_5/topFiveEmissionsPlot.png" width="650">

Indonesia's change in total emissions is far more sporadic than China's, but the rate of increase for China is far greater. Note the Russian Federation data doesn't start until 1992; prior to that year, it was the Soviet Union. Comparing the change in temperature to the total emissions...

<img src="analysis/ana_5/ChinaGasVsTemp.png" width="650">

Looking at the graph comparing China's increase in temperature to its total emissions shows a general correlation of slope increase other than the span of 2005 to 2011. However, the rapid jump in 2013 brought the correlation back to normal. The peaks of emissions do seem to precede some of the peaks in temperature change, so there could be something there.

<img src="analysis/ana_5/IndoGasVsTemp.png" width="650">

Indonesia's plot seems to show more correlation between Indonesia's emissions and its gas emissions. The paths of both generally follow the same pattern and the CO2 precedes the rise in temperatures as you'd expect. There is not a direct correlation, however, which suggests there is more that needs to be taken into account than just the level of emissions. Indonesia's total emissions rate is also much more chaotic than China's and it'd be interesting to understand why.

Since I was having trouble finding a trend at such a granular level, I decided take a step back. To better evaluate if there is a correlation between greenhouse gases and temperature rise, I plotted the the deltas of both temperature and emissions between 1970 and 2013. Using the scatterplot below, I was able to apply a line of best fit for the global data. As can be seen in the graph, there is a positive correlation between the two in that the higher emissions, the more likely the temperature is to increase as well.

<img src="analysis/ana_5/tempVsEms.png" width="600">

Global temperature and weather patterns are extremely complex and are effected by a myriad of variables. I think if I were to continue analyzing this information, I would include the temperature of the ocean and perhaps reduce the resolution of focus and move to an area view of temperature rather than countries.


## Additional Instructions to Run Code
### Data
The main source of my data was too large to upload to Github, so you will need to download it from Kaggle, [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data). You will need to set up an account with Kaggle, but it is free. I will also include a zipped file of the datset if you wish to use that instead.

### Additional Library
I used the basemap library from matplotlib to plot the world map. The documentation can be found [here](https://matplotlib.org/basemap/). To install, simply execute `$conda install basemap` in your terminal.


## Extra
Out of curiosity, I wanted to know which countries had the greatest rise in total emissions since 1970 and so I plotted those below.

<img src="analysis/ana_5/topDeltas.png" width="750">

<img src="analysis/ana_5/topDeltaPlot.png" width="600">

As you can see, China has had a staggering increase in emissions over 43 years and shows no signs of stopping. 

I also wanted to see which countries were currently producing the most greenhouse gases around the world. You can find a graph of all emissions [here](analysis/ana_5/topEmissions.png) and the total emissions of the top five contributors since 1970, below. Although the US is one of the top contributors, it's good to see the total emissions are declining.

<img src="analysis/ana_5/topEmsPlot.png" width="600">


