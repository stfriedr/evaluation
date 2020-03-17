'''
Created on 08.03.2020

@author: 49157
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import pylab as pl

logdir = os.path.join(os.getcwd(),'sim_results')
filepath_log = os.path.join(logdir,'log_complete.csv')
filepath_forecast = os.path.join(logdir,'kpi_forecast_complete.csv')
filepath_control = os.path.join(logdir,'kpi_control_complete.csv')

df_log = pd.read_csv(filepath_log, sep=';', decimal=',', index_col='time')
df_log.index = pd.to_datetime(df_log.index)

df_c = pd.read_csv(filepath_control, sep=';', decimal='.', index_col = 'start')
df_c.index = pd.to_datetime(df_c.index)

df_f = pd.read_csv(filepath_forecast, sep=';', decimal='.', index_col = 'time')
df_f.index = pd.to_datetime(df_f.index)


''' ---------- forecast evaluation  - boxplots ----------'''

fig = pl.figure()
ax = pl.axes()
for i in range(10):
    month = df_f.loc[dt.datetime(2018,2+i,1):dt.datetime(2018,3+i,1)]
    pl.boxplot(month['2h_median'].get_values(), positions = [i+1], showfliers = False)

month = df_f.loc[dt.datetime(2018,12,1):dt.datetime(2018,12,31)]
pl.boxplot(month['2h_median'].get_values(), positions = [11], showfliers = False)
    
ax.set_xticklabels(['Feb', 'Mar', 'Apr', 'Mai','Jun','Jul','Aug','Sep','Oct','Nov','Dez'])
pl.grid()
pl.ylim([-.7,.7])
pl.title('forecast-KPI during the next two hours')   


fig = pl.figure()
ax = pl.axes()
for i in range(10):
    month = df_f.loc[dt.datetime(2018,2+i,1):dt.datetime(2018,3+i,1)]
    pl.boxplot(month['24h_median'].get_values(), positions = [i+1], showfliers = False)

month = df_f.loc[dt.datetime(2018,12,1):dt.datetime(2018,12,31)]
pl.boxplot(month['24h_median'].get_values(), positions = [11], showfliers = False)
    
ax.set_xticklabels(['Feb', 'Mar', 'Apr', 'Mai','Jun','Jul','Aug','Sep','Oct','Nov','Dez'])
pl.grid()
pl.ylim([-.7,.7])
pl.title('forecast-KPI during the next 24 hours')



''' ---------- control evaluation ----------'''
plt.figure(3)
plt.title('evaluation - control')
csv_mean = df_log.groupby(df_log.index.time).mean()
plt.plot(csv_mean['IO'], label = 'IO results')
plt.grid()

print(' ----- controlling results ----- \n')
print('Cost forecast control: {}'.format(sum(df_c['kpi forecast'])))
print('Cost two-point control: {}'.format(sum(df_c['kpi standard'])))

c = df_log['IO'].get_values()
BI = (df_log['bi'].get_values()+1)/2

e = 0
for i in range(len(BI)):
    e = e +((1-BI[i])*10 +20)*c[i]
print('\n Total costs [Euro]= ',e*0.00833/100,'Euro')



# Praediktionsfehler nach Tageszeit
# plt.figure(4)
# forecast_mean = df_f.groupby(df_f.index.time).mean()
# plt.plot(forecast_mean['2h_median'])
# plt.plot(forecast_mean['6h_median'])
# plt.plot(forecast_mean['12h_median'])
# plt.plot(forecast_mean['24h_median'])


plt.show()