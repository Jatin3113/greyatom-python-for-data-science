# --------------
# Importing header files
import numpy as np
import warnings
import math

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record),axis=0)

age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std =np.sqrt(np.mean(abs(age - age. mean())**2)) 

race_0=[x for x in census[:,2] if x==0]
race_1=[x for x in census[:,2] if x==1]
race_2=[x for x in census[:,2] if x==2]
race_3=[x for x in census[:,2] if x==3]
race_4=[x for x in census[:,2] if x==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
minority_race=3

senior_citizens=census[census[:,0]>60]
working_hours_sum=np.sum([senior_citizens[:,6]])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)







