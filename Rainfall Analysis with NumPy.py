import numpy as np

rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

rainfall_array = np.array(rainfall)
print("Rainfall array:", rainfall_array)

total_rainfall = np.sum(rainfall_array)
print("Total rainfall for the week:", total_rainfall, "mm")

average_rainfall = np.mean(rainfall_array)
print("Average rainfall for the week:", average_rainfall, "mm")

no_rain_days = np.sum(rainfall_array == 0.0)
print("Number of days with no rain:", no_rain_days)

high_rain_days = np.where(rainfall_array > 5.0)[0]
print("Days with rainfall > 5 mm (by index):", high_rain_days)

percentile_75 = np.percentile(rainfall_array, 75)
above_75th = rainfall_array[rainfall_array > percentile_75]
print("75th percentile:", percentile_75)
print("Values above 75th percentile:", above_75th)
