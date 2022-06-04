# Bilateral Countermovement Jump
# 100Hz, 500Hz, & 1,000Hz
# Analysis of Raw Force Plate Data

"""The purpose of this project will be to observe how much of an impact
frequency rates (i.e. 100Hz, 500Hz, 1000Hz) has on the ability to record
'accurate & precise' data. For simplicity purposes, we will assume that the
subject performed all 3 jumps exactly the same. Because we are analyzing
jumping data, we will primarily be paying attention to the Force:Z column."""

# Import libraries that may be needed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_1 = pd.read_csv('E:/Biomechanics/Bilateral Countermovement Jump 100Hz.csv')
df_2 = pd.read_csv('E:/Biomechanics/Bilateral Countermovement Jump 500Hz.csv')
df_3 = pd.read_csv('E:/Biomechanics/Bilateral Countermovement Jump 1000Hz.csv')
# print(df_1.head())
# print(df_2.head())
# print(df_3.head())

df_1_mean = df_1['Force:Z'].mean()
#print(df_1_mean)
"682.32N"
df_1_median = df_1['Force:Z'].median()
#print(df_1_median)
"682.15N"
df_1_min = df_1['Force:Z'].min()
#print(df_1_min)
"0.0N"
df_1_max = df_1['Force:Z'].max()
#print(df_1_max)
"2385.86N"
df_1_range = (df_1['Force:Z'].max()) - (df_1['Force:Z'][0])
#print(df_1_range)
"1704.27N"
df_1_std = df_1['Force:Z'].std()
#print(df_1_std)
"332.92N"


df_2_mean = df_2['Force:Z'].mean()
#print(df_2_mean)
"682.61N"
df_2_median = df_2['Force:Z'].median()
#print(df_2_median)
"682.68N"
df_2_min = df_2['Force:Z'].min()
#print(df_2_min)
"0.0N"
df_2_max = df_2['Force:Z'].max()
#print(df_2_max)
"2886.20N"
df_2_range = (df_2['Force:Z'].max()) - (df_2['Force:Z'][0])
#print(df_2_range)
"2203.30N"
df_2_std = df_2['Force:Z'].std()
#print(df_2_std)
"313.91N"


df_3_mean = df_3['Force:Z'].mean()
#print(df_3_mean)
"682.37N"
df_3_median = df_3['Force:Z'].median()
#print(df_3_median)
"682.23N"
df_3_min = df_3['Force:Z'].min()
#print(df_3_min)
"0.0N"
df_3_max = df_3['Force:Z'].max()
#print(df_3_max)
"3181.03N"
df_3_range = (df_3['Force:Z'].max()) - (df_3['Force:Z'][0])
#print(df_3_range)
"2498.18N"
df_3_std = df_3['Force:Z'].std()
#print(df_3_std)
"348.76N"

# mean_data = [682.32, 682.61, 682.37]
# ax = plt.subplot()
# plt.bar(range(len(mean_data)), mean_data)
# ax.set_xticks([0, 1, 2])
# ax.set_xticklabels(['100Hz', '500Hz', '1,000Hz'])
# plt.xlabel('Frequency')
# plt.ylabel('Force(N)')
# plt.title('Difference of Means')
# plt.show()


# median_data = [682.15, 682.68, 682.23]
# ax = plt.subplot()
# plt.bar(range(len(median_data)), median_data)
# ax.set_xticks([0, 1, 2])
# ax.set_xticklabels(['100Hz', '500Hz', '1,000Hz'])
# plt.xlabel('Frequency')
# plt.ylabel('Force(N)')
# plt.title('Difference of Medians')
# plt.show()


# max_data = [2385.86, 2886.20, 3181.03]
# ax = plt.subplot()
# plt.bar(range(len(max_data)), max_data)
# ax.set_xticks([0, 1, 2])
# ax.set_xticklabels(['100Hz', '500Hz', '1,000Hz'])
# plt.xlabel('Frequency')
# plt.ylabel('Force(N)')
# plt.title('Difference of Max Values')
# plt.show()


# std_data = [332.92, 313.91, 348.76]
# ax = plt.subplot()
# plt.bar(range(len(std_data)), std_data)
# ax.set_xticks([0, 1, 2])
# ax.set_xticklabels(['100Hz', '500Hz', '1,000Hz'])
# plt.xlabel('Frequency')
# plt.ylabel('Force(N)')
# plt.title('Difference of Standard Deviations')
# plt.show()

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""First we will plot each frequency individually, then together on one graph."""

# ax = plt.subplot()
# plt.plot(df_1['Force:Z'])
# ax.set_xticks([0.0, (1/5) * float(len(df_1['Force:Z'])),
#                     (2/5) * float(len(df_1['Force:Z'])),
#                     (3/5) * float(len(df_1['Force:Z'])),
#                     (4/5) * float(len(df_1['Force:Z'])),
#                     float(len(df_1['Force:Z']))])
# ax.set_xticklabels(['0sec.', '1sec.', '2sec.', '3sec.', '4sec.', '5sec.'])
# plt.ylabel('Force (N)')
# plt.xlabel('Time')
# plt.title('Countermovement Jump At 100Hz')
# plt.show()


# ax = plt.subplot()
# plt.plot(df_2['Force:Z'])
# ax.set_xticks([0.0, (1/5) * float(len(df_2['Force:Z'])),
#                     (2/5) * float(len(df_2['Force:Z'])),
#                     (3/5) * float(len(df_2['Force:Z'])),
#                     (4/5) * float(len(df_2['Force:Z'])),
#                     float(len(df_2['Force:Z']))])
# ax.set_xticklabels(['0sec.', '1sec.', '2sec.', '3sec.', '4sec.', '5sec.'])
# plt.ylabel('Force (N)')
# plt.xlabel('Time')
# plt.title('Countermovement Jump At 500Hz')
# plt.show()


# ax = plt.subplot()
# plt.plot(df_3['Force:Z'])
# ax.set_xticks([0.0, (1/5) * float(len(df_3['Force:Z'])),
#                     (2/5) * float(len(df_3['Force:Z'])),
#                     (3/5) * float(len(df_3['Force:Z'])),
#                     (4/5) * float(len(df_3['Force:Z'])),
#                     float(len(df_3['Force:Z']))])
# ax.set_xticklabels(['0sec.', '1sec.', '2sec.', '3sec.', '4sec.', '5sec.'])
# plt.ylabel('Force (N)')
# plt.xlabel('Time')
# plt.title('Countermovement Jump At 1,000Hz')
# plt.show()


            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# plt.plot(df_1['Force:Z'])
# plt.plot(df_2['Force:Z'])
# plt.plot(df_3['Force:Z'])
# plt.xlabel('Data Points')
# plt.ylabel('Force (N)')
# plt.title('Countermovement Jump At Different Frequencies')
# plt.legend(['100Hz', '500Hz', '1,000Hz'])
# plt.show()

"""The main takeaway from this graph is the difference in the amount of data
recorded and magnitude of the landing forces at each frequency."""
