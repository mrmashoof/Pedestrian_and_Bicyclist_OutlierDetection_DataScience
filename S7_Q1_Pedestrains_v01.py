# Course   : Data Science with Python
# Teacher  : Mr. Pouriya Baghdadi
# Student  : Mohammadreza Mashouf
# Session  : 7
# Question : 1 (Pedestrians)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../S7_Assignment/pedestrian-and-bicyclist-counts.csv')
df = pd.DataFrame(pd.read_csv(filename))
print ('Skewness : ',df['Pedestrians'].skew())
print ('Kurtosis : ',df['Pedestrians'].kurt())

'*************************************************************************************************************************'

# Question : 01_الف_Pedestrians
fig,axs = plt.subplots (2,2, figsize=(30,20), sharex=True)
sns.boxplot    (df['Pedestrians'],ax=axs[0,0])
sns.distplot   (df['Pedestrians'],ax=axs[1,0])
sns.histplot   (df['Pedestrians'],ax=axs[0,1])
sns.kdeplot    (df['Pedestrians'],ax=axs[1,1])
plt.show()

'*************************************************************************************************************************'

# Question : 01_ب_Pedestrians
q1 = np.percentile (df['Pedestrians'],q=25)
q3 = np.percentile (df['Pedestrians'],q=75)
iqr = q3 - q1
iqr_lower_limit = q1 - 1.5 * iqr
iqr_upper_limit = q3 + 1.5 * iqr
iqr_outliers = []
for item in df['Pedestrians']:
    if not (iqr_lower_limit < item < iqr_upper_limit) :
        iqr_outliers.append(item)
print ('Question 01_ب_Pedestrians : \n' +
       'In IQR method,acceptable range is between '+
       str('{:,.0f}'.format(iqr_lower_limit))+
       ' and '+
       str('{:,.0f}'.format(iqr_upper_limit))+
       '.')
print ('IQR method outlier(s) list: ',iqr_outliers,'\n')

'*************************************************************************************************************************'

# Question : 01_پ_Pedestrians
avg = df['Pedestrians'].mean()
std = df['Pedestrians'].std()
std_lower_limit = avg - 3 * std
std_upper_limit = avg + 3 * std
std_outliers = []
for item in df['Pedestrians']:
    if not (std_lower_limit < item < std_upper_limit) :
        std_outliers.append(item)
print ('Question 01_پ_Pedestrians : \n'+
       'In std method,acceptable range is between '+
       str('{:,.0f}'.format(std_lower_limit))+
       ' and '+
       str('{:,.0f}'.format(std_upper_limit))+
       '.')    
print ('Std method outlier(s) list: ',std_outliers,'\n')

'*************************************************************************************************************************'

# Question : 01_ت_Pedestrians
df = df.sort_values(by=['Pedestrians'],ascending=True)
avg = df['Pedestrians'].mean()
std = df['Pedestrians'].std()
zscore = (df['Pedestrians'] - avg) / std
df = df.join(zscore, rsuffix='_zscore')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print ('Question 01_ت_Pedestrians : \n'+
       'Sorted dataframe, by pedestrains numbers along with Z-Score is as below : ')
print(df)