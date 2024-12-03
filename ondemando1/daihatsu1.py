# import os

# path = os.getcwd()

# print(path)
# # /Users/mbp/Documents/my-project/python-snippets/notebook

# print(type(path))
# # <class 'str'>

import pandas as pd
import datetime as dt
import os

base_path = "C:/Users/fs203/OneDrive/University_Python_Lecture/ondemando1"
dfA = pd.read_csv(os.path.join(base_path, "okinawa.csv"))
dfB = pd.read_csv(os.path.join(base_path, "osaka.csv"))
dfC = pd.read_csv(os.path.join(base_path, "tokyo.csv"))

dfA["地点"] = "沖縄"
dfB["地点"] = "大阪"
dfC["地点"] = "東京"


# print(dfA)
# print(dfB)
# print(dfC)

# df1 = pd.concat([dfA, dfB, dfC], axis=0)

# print(df1)

# df2 = pd.concat([dfA, dfB, dfC], axis=1)

# print(df2)

# mean_temp_Okinawa = dfA["気温(℃)"].mean()
# mean_temp_Osaka = dfB["気温(℃)"].mean()
# mean_temp_Tokyo = dfC["気温(℃)"].mean()
# print("沖縄の平均気温：", mean_temp_Okinawa)
# print("大阪の平均気温：", mean_temp_Osaka)
# print("東京の平均気温：", mean_temp_Tokyo)

# dfA["DateTime"] = pd.to_datetime(dfA["DateTime"])
# dfB["DateTime"] = pd.to_datetime(dfB["DateTime"])
# dfC["DateTime"] = pd.to_datetime(dfC["DateTime"])

# may_rain_data_A = dfA[(dfA["DateTime"].dt.month == 5) & (dfA["降水量(mm)"] >= 0)]
# may_rain_data_B = dfB[(dfB["DateTime"].dt.month == 5) & (dfB["降水量(mm)"] >= 0)]
# may_rain_data_C = dfC[(dfC["DateTime"].dt.month == 5) & (dfC["降水量(mm)"] >= 0)]

# total_rainA = may_rain_data_A["降水量(mm)"].sum()
# total_rainB = may_rain_data_B["降水量(mm)"].sum()
# total_rainC = may_rain_data_C["降水量(mm)"].sum()

# print("沖縄における5月の合計降水量：", total_rainA)
# print("大阪における5月の合計降水量：", total_rainB)
# print("東京における5月の合計降水量：", total_rainC)

dfA["DateTime"] = pd.to_datetime(dfA["DateTime"])
dfB["DateTime"] = pd.to_datetime(dfB["DateTime"])
dfC["DateTime"] = pd.to_datetime(dfC["DateTime"])


# df1[(df1['日付'] >= dt.datetime(2019,5,3)) & (df1['日付'] < dt.datetime(2019,5,6))]


span_rain_data_A = dfA[
    (dfA["DateTime"] >= dt.datetime(2021, 1, 1))
    & (dfA["DateTime"] < dt.datetime(2021, 10, 31))
    & (dfA["降水量(mm)"] >= 0.1)
]

span_rain_data_B = dfB[
    (dfB["DateTime"] >= dt.datetime(2021, 1, 1))
    & (dfB["DateTime"] < dt.datetime(2021, 10, 31))
    & (dfB["降水量(mm)"] >= 0.1)
]
span_rain_data_C = dfC[
    (dfC["DateTime"] >= dt.datetime(2021, 1, 1))
    & (dfC["DateTime"] < dt.datetime(2021, 10, 31))
    & (dfC["降水量(mm)"] >= 0.1)
]

days_over_count_A = span_rain_data_A["DateTime"].dt.date.nunique()
days_over_count_B = span_rain_data_B["DateTime"].dt.date.nunique()
days_over_count_C = span_rain_data_C["DateTime"].dt.date.nunique()


print(
    "沖縄で2021年1月1日から10月30日までに0.1mm以上の降水量を観測した日数は",
    days_over_count_A,
    "日です。",
)
print(
    "大阪で2021年1月1日から10月30日までに0.1mm以上の降水量を観測した日数は",
    days_over_count_B,
    "日です。",
)
print(
    "東京で2021年1月1日から10月30日までに0.1mm以上の降水量を観測した日数は",
    days_over_count_C,
    "日です。",
)
