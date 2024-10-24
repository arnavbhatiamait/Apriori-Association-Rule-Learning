# %% [markdown]
# Apriori Association Rule Learning

# %%
# !pip install apyori

# %% [markdown]
# Importing the libraries

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# Importing the datasets

# %%
df=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
df.head()


# %% [markdown]
# Data Preprocessing

# %%
list_transactions=[]
for i in range(7501):
    list_transactions.append([str(df.values[i,j]) for j in range(20) ])
list_transactions

# %% [markdown]
# Training The Apriori Model on the data Set 

# %%
from apyori import apriori
# 3*7/7500
rules=apriori(transactions=list_transactions, min_support=0.003, min_confidence=0.2,min_lift=3,min_length=2,max_length=2)
# to get buy one get one


# %% [markdown]
# Displaying the results directly from the output of the Model

# %%
results = list(rules)
results

# %% [markdown]
# Putting the results well organized into a Pandas DataFrame

# %%
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

# %% [markdown]
# Displaying the non sorted results

# %%
resultsinDataFrame

# %% [markdown]
# Displaying the Rules in Descending order by Lift value

# %%
resultsinDataFrame.nlargest(n = 10, columns = 'Lift')


