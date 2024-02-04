# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:52:28 2024

@author: Erna Leticia

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movie_dataset.csv")#, index_col="Year", parse_dates = True)

print(df.head())
print(df.info())
print(df.describe())

##Dropping values with missing data
df = df.dropna(axis=0)
print(df)
print(df.describe())

###############################################################################
##Q1. The highest rated movie in the data set
print(df[df['Rating'].max() == df['Rating']]['Title'])

##R1. The Dark Knight
rated_movie = df.nlargest(5,'Rating')[['Title', 'Rating']]
print(rated_movie)

rated_movie = df.nlargest(10,'Rating')[['Title', 'Rating', 'Director']].set_index('Title').plot.bar()
plt.show()
###############################################################################
##Q2. The average revenue of all movies in the dataset
print(df['Revenue (Millions)'].mean())

##R2. Between 70 and 100 Million
###############################################################################
##Q3. The average revenue of movies in the dataset from 2015 to 2017
movie= pd.read_csv("movie_dataset.csv", index_col="Year", parse_dates = True)
movie.dropna(inplace = True)
print(movie["2015":"2017"]["Revenue (Millions)"].mean())

##R3. Between 50 and 80 Million
"""df.groupby('Year')['Revenue (Millions)'].mean().plot.bar()
plt.title('Revenue (Millions)')
plt.show()
"""
###############################################################################
##Q4. The number of movies released in the year 2016
print(df['Year'].value_counts())

##R4. 297 when data are not cleaned
"""df['Year'].value_counts().sort_values(ascending=True).plot.bar()
plt.title('Number of Movies per Year')
plt.show()
"""
###############################################################################
##Q5. The number of movies directed by Christopher Nohan
Christopher_Nolan = df[df['Director'] == 'Christopher Nolan']

##R5. 5 movies
###############################################################################
##6. The movies in the dataset with a rating of at least 8.0
print(df[df['Rating'] >= 8.0])

##R6. 78 when data are not cleaned
###############################################################################
##Q7. The median rating of movies directed by Christopherb Nolan
print(Christopher_Nolan['Rating'].median())

##R7. 8,6
###############################################################################
##Q8. The year with the highest average rating
dr = pd.date_range('2006-01-01', '2016-01-01')
h_a_r = pd.DataFrame(range(len(dr)), index=dr, columns=['AverageRating'])
print(h_a_r.resample('1y').AverageRating.agg([min, max]))

##R8. 2007
"""df.groupby('Year')['Rating'].mean().plot.bar()
plt.title('AverageRating')
plt.show()"""
###############################################################################
##Q9. The percentage increase 0f in number of movies made between 2006 and 2016
print(df.describe())

##R9. 210
###############################################################################
##Q10. The most commonn actor in all the movies
da = df['Actors'].str.split(',')
dm = [actor for sublist in da for actor in sublist]
m_c_a = pd.Series(dm).value_counts().index[0]
print(m_c_a)

##R10. Mark Wahlberg
###############################################################################
##Q11. The number of unique genres in the dataset
du = set(df['Genre'].str.split(',').explode())
print(len(du))

##R11. 20
