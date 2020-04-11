# Predicting the Next COVID-19 Hotspot

Adelle Jia (ajia90) and Christine Zhao (czhao028)

## Motivation
This goal is ambitious: like predicting the stock market, coronavirus outbreak predictions can be a tricky thing. An unaccounted variable can come into play: someone with coronavirus decided to have a birthday party, and the virus spreads like wildfire. Nonetheless, after reading [a few opinions by experts](https://www.statnews.com/2020/04/01/coronavirus-how-bad-it-gets-different-communities/), there are a few factors that we can identify that make a city more vulnerable than others. Our project seeks to identify which of those factors are most powerful in predicting an outbreak and the probability that Houston as vulnerable or likely to a massive coronavirus spread.

## Methodology
After individually going through [current hotspots](https://www.scientificamerican.com/article/map-reveals-hidden-u-s-hotspots-of-coronavirus-infection/) as defined by cases per 10,000 people (including rural areas that often get overlooked), we listed out the major reasons that coronavirus was brought to regions & what worsened the problem in [this document](https://docs.google.com/document/d/1aYphRfF8b_siem5ZNdMKAaTm5iFiyQtQwD_adOMns5U/edit?usp=sharing). By examining expert opinions & narrowing down into the most recurring causes, we chose 6 factors to investigate the importance of:
<ol>
  <li> Travel
    <ul>
      <li> The majority of cases were brought to coasts and small towns by international or out-of-state travel
    </ul>
   <li> Population Density
     <ul>
      <li> "Density is a factor in this pandemic, as it has been in previous ones. The very same clustering of people that makes our great cities more innovative and productive also makes them, and us, vulnerable to infectious disease." Source: https://bit.ly/2wvBocR
     </ul>
    <li> Pre-Existing Conditions Population
      <ul> 
        <li>It's well-known that those with pre-existing conditions are much more suspectible to this respitory disease. We investigate surveys by the CDC to estimate this per metropolitan area.
      </ul>
      
 <li> Low-income Population
  <ul> 
    <li> People from low-income backgrounds are those who are forced to continue working despite the transmissable nature of the disease and are therefore more susceptible. There are many estimates that black & Latino populations are equally vulnerable as well, [highlighting the disparty in socioeconomic status perpetuaded over the decades](https://www.nola.com/news/coronavirus/article_d804d410-7852-11ea-ac6d-470ebb61c694.html). We decided to look at low-income populations as many news sources point to economic status as a huge contributor to coronavirus deaths/cases.
  </ul>
  
  <li> Medically Underserved Areas
  <ul> 
    <li> In Albany, GA, few would have expected coronavirus to balloon so quickly: a lack of [ICU beds](https://www.nytimes.com/2020/03/30/us/coronavirus-funeral-albany-georgia.html) and medical care compounded the problem. This issue has been frequently pointed out, that coronavirus cases may soon overpower hospital capabilities. We chose to look at medically underserved areas, as shown in a Google Cloud public dataset.
  </ul>
  
  <li> State/County Response Time & Stay-At-Home Orders (as of March 30)
<ul> 
  <li> [Slow response time, especially in New York](https://www.cnn.com/2020/03/26/us/new-york-coronavirus-explainer/index.html) is the mantra nowadays as we saw our nations & municipalities slowly react to a pandemic identified 2 months ago. Though states have been swift to enact social distancing, there are still a key few states who hold out. 
  </ul>
     
 </ol>
      
        




