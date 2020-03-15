The city of Los Angeles has made available its crime reports database. I’m interested in learning how to analyse crime data in order to derive policy recommendations. [The results are described in a blog post I published in medium.](https://medium.com/@abreulastra/crime-patterns-in-la-85eff44d6529)

## Business Understanding - Project goal
Data is changing they way in which organizations reach their goals. For any metropolitan area, perhaps there is no goal more important than reducing crime to a minimum. In this excersize, I try to assess if the LA police deparment appears to be following a strategy based on data to mitigate crime.

## Data Understanding
[The city of Los Angeles has made available its crime reports database, through kaggle.](https://www.kaggle.com/cityofLA/los-angeles-crime-arrest-data)
The file **prepare_data.py** takes the original *.csv databases, and trims them, in order to get the last 6 months of data, and bring them to a size small enough to be able to share them on github.
Once this process is done, we get two csv files:
- LA Police department crimes reports from 2018–12–25, until 2019–06–22, which contains a total of 103,181 crime reports.
- LA Police department arrests reports from 2018–12–25, until 2019–06–22. This table contains 40,884 cases. The LA police identifies in its database 27 types of charge groups, and 835 types of charges.

## Prepare Data
There were two guiding questions in order to decide how the data should be shaped.:

##### 1. What are most recurring crimes in LA?
##### 2. Is the police response a match for the criminal activity?

Since there are more than a hundred kind of crimes reported in the database, I relabeled the crime description code, based on the variable 'Charge Group Description', from the arrests database. We benefit in two ways from this: first, we would have broader categories for types of crimes, allowing us to identify the main problems in the city; second, we could have consistency across the crime and arrests database.

Also, it became evident that to answers this questions, it' is also necessary to format the date columns from both tables, create dummies for types of crimes, and neighborhoods, and dealling with missing values. The file **help_functions.py** implements this.

## Data Modeling
Since the project's goal is to understand if the LA police department seems to follow a strategy based on data to mitigate crime, the methodology is descriptive, not predictive. I implement an algorithm to reduce dimensionality and describe the factors that explain for most of the variance in crime. For this we use a principal component analysis (PCA), and analyse the first eigenvectors to see how the variables correlate with each other. Thus, we could be able to see if crimes go hand in hand with other types of crime or with certain areas.

## Evaluate the Results
The evaluation for the PCA is not very rigorous,and just based on descriptive statitics. [In the conclusion seccion of the Jupyter notebook](https://github.com/abreulastra/crime_analysis/blob/master/crime_patterns_LA.ipynb), there some graphs that show that describe the ocurrence of crime to victims of different ethnicities. These results are very well in line with the PCA findings (i.e. larceny victims tend to be of white ethnicity, hispanic and black ethnicites suffer relatively more from aggravated assaults).

 ## Analysis
**crime_patterns_LA.ipynb**, is a Jupyter notebook ilustrates the whole process, and how I answered the questions.

## Conclusion
Crime in LA seems to have a very heterogeneous pattern, making it difficult to maximize the impact of the police deparment's action. It seems that fighting the most violent types of crimes (assaults) is uncorrelated with the more prevalent crimes, like larceny and burglary.

It also seems that the department concetrates efforst in those efforts that seem "close to home". Namely, the most frequent type of arrests have to do with court orders (violations of parore, etc), and flagrant acts (like assaults), paying more attention to the Central neighborhood, rather than the one where most of the crime reports happen: 77th street.

While the data analyzed here only considers arrestss and not any other actions performed by the police, it seems that the department could benefit from a more systematic approach to its own data. Prospectively, this data could shed some light toward strategies focusing on prevention.

# Libraries used
* pandas
* matplotlib.pyplot
* seaborn
* from sklearn.preprocessing, StandardScaler
* from sklearn.decomposition, PCA



