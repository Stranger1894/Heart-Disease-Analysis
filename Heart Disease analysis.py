#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[66]:


df = pd.read_csv(r'C:\Users\Sourav\OneDrive\Desktop\HealthCare Analytics ineuron project/Heart disease.csv')


# In[67]:


df.head(6)


# In[68]:


df.describe().T


# In[69]:


data = df.copy()


# In[70]:


data.head()


# In[71]:


def age_group_conv(data):
    if data <= 40:
        return "40 yrs or less"
    elif (data > 40) & (data <= 60):
        return "41 - 60 yrs"
    else:
        return "More than 60 yrs"


# In[72]:


data['age_group'] = data['age'].apply(age_group_conv)


# In[73]:


data


# In[74]:


#comparision of age_group and outcome
data.groupby(['age_group', 'target']).count()['age'].unstack().plot.bar()
plt.ylabel("Number of patients")
plt.title("Number of patients by Age group")
plt.show()


# In[75]:


#comparision of different ages and outcome
plt.figure(figsize = (12,8))
sns.countplot(x= "age", data = data, hue = "target")
plt.legend(loc='upper right')
plt.ylabel("Number of patients")
plt.title("Number of patients by Age")
plt.show()


# In[77]:


#converting values for some of the categorical variables
data['sex'] = data.sex.map({0: 'female', 1: 'male'})
data['target'] = data.target.map({0: 'no', 1: 'yes'})
data['exang'] = data.exang.map({0:'no',1:'yes'})
data['fbs'] = data.fbs.map({0:'<120mg/dl',1:'>120mg/dl'})


# In[78]:


data.head()


# In[15]:


#comparision of sex with outcome
plt.figure(figsize = (8,6))
sns.countplot(x= "sex", data = data, hue = "target")
plt.legend(loc='upper right')
plt.xlabel("Sex")
plt.ylabel("Number of patients")
plt.title("Number of patients by Sex")
plt.show()


# In[62]:


data.dtypes


# In[17]:


data['cp'] = str(data['cp'])


# In[39]:


#box plot for cholesterol level and outcome

sns.boxplot(x= 'target', y='chol',data=data)
plt.show()


# In[79]:


#Comparision of fasting blood sugar with target

data.groupby(['fbs', 'target']).count()['age'].unstack().plot.bar()
plt.show()


# In[31]:


data.groupby(['fbs', 'target']).count()['age'].unstack()


# In[41]:


#Comparision of restecg with target

data.groupby(['restecg', 'target']).count()['age'].unstack().plot.bar()
plt.show()


# In[36]:


data.groupby(['restecg', 'target']).count()['age'].unstack()


# In[42]:


#Comparision of thalach with target
#box plot for max heartrate and outcome

sns.boxplot(x= 'target', y='thalach',data=data)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




