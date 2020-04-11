# Predicting the Next COVID-19 Hotspot

Adelle Jia (ajia90) and Christine Zhao (czhao028)


## Motivation
This goal is ambitious: like predicting the stock market, coronavirus outbreak predictions can be extremely tricky. There are numerous intertwining causes of outbreak, as well as unaccounted variables: someone with coronavirus decides to have a birthday party, and the virus spreads like wildfire in an otherwise unsusceptible area. Nonetheless, after reading [a few opinions by experts](https://www.statnews.com/2020/04/01/coronavirus-how-bad-it-gets-different-communities/), there are a few factors that we can identify that make a city more vulnerable than others. Our project seeks to identify <b> which of those factors are most powerful in predicting an outbreak </b> and <b>the probability that counties in Houston are as vulnerable or likely to a massive coronavirus spread</b>.

### Does Houston carry the deadly combination of factors that rapidly spreads COVID?
Are other less-acknowledged areas of the country in danger of becoming the next epicenter of the epidemic? The quicker we can predict which areas are most vulnerable, the more knowledgeable we can be in directing assistance towards struggling hospitals or prevention of spread in those areas. With over 12,000 people confirmed with COVID-19 in New Orleans, and 1,300+ confirmed in the Houston-Galveston-Sugarland Metropolitan area, quick calculations could save lives. 

Taiwan, though much smaller, [moved quickly to stamp out the coronavirus](https://www.cnn.com/2020/04/04/asia/taiwan-coronavirus-response-who-intl-hnk/index.html) by having high sanctions on travel, distributing masks to high-need areas, and upping testing, setting a model for the world. The country only had *382 cases and 6 deaths*, about 1 in every 500,000 people, whereas the US is at 1 in every 600 people in terms of cases, still exponentially growing. The country has now surpassed [half a million cases](https://www.cnn.com/2020/04/10/health/us-coronavirus-friday/index.html). Taiwan demonstrates how rapid action, even on a small scale like county-wide and state responses, can greatly prevent deaths.

### Millions of at-risk Americans live in Counties with Ventilator & ICU Shortages
![](https://github.com/czhao028/DataScience/blob/master/no%20icu%20beds.PNG)
The data is staggering: a large portion of the country have hospitals with no ICU beds. [More than 7 million people who are age 60 and up are at risk.](https://khn.org/news/as-coronavirus-spreads-widely-millions-of-older-americans-live-in-counties-with-no-icu-beds/) The quicker people in at-risk areas can identify alternative means of hospital care, and the quicker we can move to put ICU beds in vulnerable areas identified by our model, the safer we become in this country. 

## Methodology
After individually going through [current hotspots](https://www.scientificamerican.com/article/map-reveals-hidden-u-s-hotspots-of-coronavirus-infection/) as defined by cases per 10,000 people (including rural areas that often get overlooked), we listed out suspected major reasons that coronavirus was brought to regions & what worsened the problem in [this document](https://docs.google.com/document/d/1aYphRfF8b_siem5ZNdMKAaTm5iFiyQtQwD_adOMns5U/edit?usp=sharing). By examining expert opinions & narrowing down into the most recurring causes, we chose 6 factors to investigate the importance of: 
<ol>
  
  <li> <b> Transportation </b> 
    <ul>
      <li> 
        
The majority of cases were brought to coasts and small towns by international or out-of-state travel. We look at most traveled airplane routes coming into each city; for small towns, this is their link to large, coronavirus-heavy areas. 
    </ul>
   <li> <b> Population Density </b>
     <ul>
      <li> 
        
"Density is a factor in this pandemic, as it has been in previous ones. The very same clustering of people that makes our great cities more innovative and productive also makes them, and us, vulnerable to infectious disease." Source: https://bit.ly/2wvBocR
     </ul>
    <li><b> Pre-Existing Conditions Population</b>
      <ul> 
        <li>
          
It's well-known that those with pre-existing conditions are much more suspectible to this respitory disease. We investigate surveys by the CDC to estimate this per metropolitan area. 
      </ul>
      
 <li> <b>Low-income Population</b>
  <ul> 
    <li> 
In addition to looking at factors that directly influence the mechanistic spread of disease, we also chose to look at social determinants of health. The new outbreak puts even more pressure/stress on those of lower socio-economic status. Not only do they typically have less insurance coverage/access to healthcare, they are also forced to continue working despite the transmissable nature of the disease. There are several areas in which cases are disportionately more of black & Latino populations [highlighting the disparty in socioeconomic status perpetuaded over the decades](https://www.nola.com/news/coronavirus/article_d804d410-7852-11ea-ac6d-470ebb61c694.html). We decided to look at low-income populations as many news sources point to socioeconomic status as a huge contributor to coronavirus deaths/cases.
  </ul>
  
  <li> <b>Medically Underserved Areas</b>
  <ul> 
    <li> 

 In Albany, GA, few would have expected coronavirus to balloon so quickly: a lack of [ICU beds](https://www.nytimes.com/2020/03/30/us/coronavirus-funeral-albany-georgia.html) and medical care compounded the problem. This issue has been frequently pointed out, that coronavirus cases may soon overpower hospital capabilities. We chose to look at medically underserved areas, as shown in a Google Cloud public dataset.
  </ul>
  
  <li> <b>State/County Response Time & Stay-At-Home Orders (as of March 30)</b>
<ul> 
  <li> 
   
[Slow response time, especially in New York](https://www.cnn.com/2020/03/26/us/new-york-coronavirus-explainer/index.html) is the mantra nowadays as we saw our nations & municipalities slowly react to a pandemic identified 2 months ago. Though most states and counties have been swift to enact social distancing, there are still a key few states who hold out. 
  </ul>
</ol>

### Cases By County
![Cases By County](https://github.com/czhao028/DataScience/blob/master/cases%20by%20county.PNG)

To really see how these different factors may have had a pull on coronavirus outbreak, let's look at a few different maps:

![prexisting](https://github.com/czhao028/DataScience/blob/master/pre-existing.PNG)
![prexisting](https://github.com/czhao028/DataScience/blob/master/pictures-country.jpg)
 ## What's Been Accomplished
 
 ### Issues Tackled
 We started on Monday & have been working every day since. The bulk of the work is making sure that all of the data is in one format: the Census uses zip codes and tracts, while the CDC's/Kaiser's pre-existing condition projections only have data for metropolitan areas (MSA). In addition, Harris County doesn't report cases but only as a metropolitan area: if we used zip codes, then that would fail to capture all reported cases. In addition, medically underserved areas only used counties, and airports are likely to service more than 1 zip code or county, leaning towards metropolitan areas. Airports were also only given their airport code & GPS coordinates. In the end, we decided to use all the information we had for MSA's and apply them to each county, with most of our data being on the county-level to ensure most accuracy in representation the population of the area.
 
 ### Our Solutions
We've loaded all the data we've been able to clean, organize, geocode, assign counties/MSA's into Jupyter using pandas (Python) or into Excel or CSV Files. This includes poverty level by county, using US Census 2010 data, airports (and corresponding MSA) & most common incoming travel routes, and population density per MSA. Not all of the data is yet on Github, since Adelle had some issues using Github on Friday, but they will be by next week. What's not done yet is 
- Medically Underserved Areas: the data by zip-code is only available through ArcGIS so we've requested a license, hopefully to be fufilled by Monday
- Pre-existing condition estimates: Christine has messaged the author of the study & they've agreed to provide the data. Hope to hear from her soon as well
 
 ## Our Timeline
By the end of the second week, we will have all our data into one spreadsheet to feed into different models to try: the first we're attempting is <b>backpropogation through a neural network</b>, so we can identify the weights of the different factors. Does airport travel have less of an impact now, now that people are at home? Does economic status affect coronavirus outbreak more than we thought it would? Which combination of factors is most deadly for a city to have? How many hidden layers will the neural network have? We strive to have the data cleaned by mid-week and start testing different models on our numbers by Friday. 

By the end of the third week, we will have identified a suitable model that fits our data & even start constructing the algorithms from. Christine has taken a few Artificial Intelligence Courses & Adelle is in Computational Neuro. We hope we can deeply investigate how different machine learning techniques predict coronavirus outcomes in the Houson area. 
 

      
        




