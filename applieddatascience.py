# data source: https://fivethirtyeight.com/features/voter-registrations-are-way-way-down-during-the-pandemic/
# import stats tools and libraries required
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# import database for voter registration
voters = pd.read_csv(voter-registration.csv)

# transform the data to be python readable
df = pd.melt(voters, value_name = "New Voter Count", var_name = "Voter Year")

# generate box plot based on comparing scores from 2016 to 2020 for a given state
sns.boxplot(x="Voter Year", y="New Voter Count", data=df)
# save boxplot image
plt.savefig("boxplot.png")

#display boxplot
plt.show()