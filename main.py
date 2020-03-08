'''
Created on 08.03.2020

@author: 49157
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filepath_base = 'C:/Users/49157/Desktop/Simulationsergebnisse/Sim_complete'
filepath_log = os.path.join(filepath_base,'log_complete.csv')
filepath_forecast = os.path.join(filepath_base,'kpi_forecast_complete.csv')
filepath_control = os.path.join(filepath_base,'kpi_control_complete.csv')

df_log = pd.read_csv(filepath_log, sep=';', decimal='.', index_col='time')

df_c = pd.read_csv(filepath_control, sep=';', decimal='.', index_col = 'start')
df_c.index = pd.to_datetime(df_c.index)

df_f = pd.read_csv(filepath_forecast, sep=';', decimal='.', index_col = 'time')
df_f.index = pd.to_datetime(df_f.index)


''' remove double data from control KPI'''
# df = pd.DataFrame({'start': [],
#                    'stop': [],
#                    'kpi forecast': [],
#                    'kpi standard': []})
# 
# for i in range(df_c.__len__()-1):
#     if df_c.index[i] != df_c.index[i+1]:
#         results = pd.DataFrame({'start': [df_c.index[i]],
#                                 'stop': [df_c.iloc[i]['stop']],
#                                 'kpi forecast': [df_c.iloc[i]['kpi forecast']],
#                                 'kpi standard': [df_c.iloc[i]['kpi standard']]})
# 
#         df = df.append(results)
#         
# df.set_index('start')
# df.to_csv('C:/Users/49157/Desktop/Simulationsergebnisse/Sim_complete/kpi_control_comp2.csv', sep = ';', decimal=',')



plt.figure(1)
plt.title('evaluation - control')
plt.plot(df_c['kpi forecast'], label = 'kpi forecast')
plt.plot(df_c['kpi standard'], label = 'kpi standard')
plt.plot(df_c['kpi forecast']-df_c['kpi standard'], label = 'diff')
plt.legend()
plt.grid()

print(' ----- controlling results ----- \n')
print('cost forecast control: {}'.format(sum(df_c['kpi forecast'])))
print('cost standard control: {}'.format(sum(df_c['kpi standard'])))


plt.figure(2)
plt.title('evaluation - 24h forecast')
plt.plot(df_f['24h_median'], label = '24h median')
plt.plot(df_f['24h_quartil_25'], 'k--', linewidth = 0.5, label = 'quartile low')
plt.plot(df_f['24h_quartil75'], 'k--', linewidth = 0.5, label = 'quartil high')
plt.legend()
plt.grid()


plt.figure(3)
plt.title('evaluation - 2h forecast')
plt.plot(df_f['2h_median'], label = '2h median')
plt.plot(df_f['2h_quartil_25'], 'k--', linewidth = 0.5, label = 'quartile low')
plt.plot(df_f['2h_quartil75'], 'k--', linewidth = 0.5, label = 'quartil high')
plt.legend()
plt.grid()


# Praediktionsfehler nach Tageszeit



plt.pause(0.1)


