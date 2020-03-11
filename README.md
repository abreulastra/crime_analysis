### Goal: 
To understand the crime landscape in LA by answering the following questions.
##### 1. What are most recurring crimes in LA?
##### 2. Is the police response a match for the criminal activity?
##### 3. Does the LA police deparment seems to follow a strategy based on data to mitigate crime?

# Structure
1. **prepare_data.py** is the file I ran with the original *.csv databases. The purpose was to trim them, in order to get the last 6 months of data, and bring them to a size small enough to be able to share them on github.
2. **help_functions.py** contains all the data engineering part, creating dummy variables, formating dates, and dealing with missing values. 
3. **crime_patterns_LA.ipynb**, is a Jupyter notebook that proposes three questions to understand the crime dynamics in LA, and provides answers with data. 

# Libraries
#We start by importing our dependencies
pandas
matplotlib.pyplot
seaborn
from sklearn.preprocessing, StandardScaler
from sklearn.decomposition, PCA

# Data Source
https://www.kaggle.com/cityofLA/los-angeles-crime-arrest-data#arrest-data-from-2010-to-present.csv

# Conclusion
Crime in LA seems to have a very heterogeneous pattern, making it difficult to maximize the impact of the police deparment's action. It seems that fighting the most violent types of crimes (assaults) is uncorrelated with the more prevalent crimes, like larceny and burglary.

It also seems that the department concetrates efforst in those efforts that seem "close to home". Namely, the most frequent type of arrests have to do with court orders (violations of parore, etc), and flagrant acts (like assaults), paying more attention to the Central neighborhood, rather than the one where most of the crime reports happen: 77th street.

While the data analyzed here only considers arrestss and not any other actions performed by the police, it seems that the department could benefit from a more systematic approach to its own data. Prospectively, this data could shed some light toward strategies focusing on prevention.
