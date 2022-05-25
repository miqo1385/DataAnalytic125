import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

trump = pd.read_csv('approval_topline.csv')
print(trump.head())
print(trump.approve_estimate.describe())
sns.boxplot(y= trump.approve_estimate, x= trump.disapprove_estimate )
plt.savefig("approve.png")

