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

print(voters.head())
print(voters.approve_estimate.describe())
print(voters.disapprove_estimate.describe())
sns.boxplot(y=voters.approve_estimate, x=voters.disapprove_estimate )
plt.savefig('votersapproval.png')
plt.show()
