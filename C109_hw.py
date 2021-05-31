from os import stat
import pandas as pd
import statistics
import plotly.express as pt
import plotly.figure_factory as ff

file = pd.read_csv('data2.csv')


#reading scores
reading = file['reading score'].to_list()





#reading statistics
reading_mean = statistics.mean(reading)

reading_std = statistics.stdev(reading)

reading_fstd_s,reading_fstd_e = reading_mean - reading_std , reading_mean + reading_std

reading_sstd_s,reading_sstd_e = reading_mean - 2*reading_std , reading_mean + 2*reading_std

reading_tstd_s,reading_tstd_e = reading_mean - 3*reading_std , reading_mean + 3*reading_std

reading_std1 = [res1 for res1 in reading if res1 > reading_fstd_s and res1 < reading_fstd_e]

reading_std2 = [res2 for res2 in reading if res2 > reading_sstd_s and res2 < reading_sstd_e]

reading_std3 = [res3 for res3 in reading if res3 > reading_tstd_s and res3 < reading_tstd_e]

print('{}% of the reading data lies in first std'.format(len(reading_std1)*100/len(reading)))

print('{}% of the reading data lies in second std'.format(len(reading_std2)*100/len(reading)))

print('{}% of the reading data lies in third std'.format(len(reading_std3)*100/len(reading)))


graph = ff.create_distplot([reading,reading_std1,reading_std2,reading_std3],['Reading scores','Reading STD 1','Reading STD 2','Reading STD 3'],show_hist=False)
graph.show()


