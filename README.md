# Coronavirus: What can Tweet location tell us about the state of the virus?
My goal is to use supervised machine learning to determine if the contents of a tweet about coronavirus tells us anything about the location of the user. If so, can a model show the spread of coronavirus based on the volume and contents of people's tweets?

I've used Python to pipeline live tweets about COVID-19/Coronavirus into a MySQL database. It contains two tables: one capturing tweets featuring keywords "coronavirus" and "COVID-19", and the other capturing keywords "novel" and "unprecedented." Collected information includes username, tweet text, tweet location as reported by user, and date and time of tweet.

# Start Here: 
I've posted a series of ![Jupyter Notebooks](https://github.com/LBBL96/Coronavirus-on-Twitter/blob/master/Code/Jupyter%20Notebooks/EDA%20for%20UK%20vs%20USA.ipynb) that I created to show some of my initial exploratory data analysis. This is the first one.
