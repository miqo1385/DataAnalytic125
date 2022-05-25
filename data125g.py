import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

trump = pd.read_csv('approval_topline.csv')
print(trump.info())
print(trump.subgroup.value_counts())
print(trump.approve_estimate.value_counts())
print(trump.disapprove_estimate.value_counts())

trump_approval = trump.groupby(['subgroup']).approve_estimate.mean()
print(trump_approval)
trump_disapproval = trump.groupby(['subgroup']).disapprove_estimate.mean()
print(trump_disapproval)

adults= trump[trump.subgroup == 'Adults']
all_polls = trump[trump.subgroup == 'All polls']
voters = trump[trump.subgroup == 'Voters']

print(st.ttest_ind(voters['approve_estimate'], adults['approve_estimate']))

print(adults.head())
print(adults.approve_estimate.describe())
print(adults.disapprove_estimate.describe())
sns.boxplot(y=adults.approve_estimate, x=adults.disapprove_estimate )
plt.savefig('adultsapproval.png')
plt.show()

