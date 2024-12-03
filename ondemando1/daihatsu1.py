# import os

# path = os.getcwd()

# print(path)
# # /Users/mbp/Documents/my-project/python-snippets/notebook

# print(type(path))
# # <class 'str'>

import pandas as pd
import datetime as dt
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

base_path = "C:/Users/fs203/OneDrive/University_Python_Lecture/ondemando1"
dfA = pd.read_csv(os.path.join(base_path, "okinawa.csv"))
dfB = pd.read_csv(os.path.join(base_path, "osaka.csv"))
dfC = pd.read_csv(os.path.join(base_path, "tokyo.csv"))

# dfA["地点"] = "沖縄"
# dfB["地点"] = "大阪"
# dfC["地点"] = "東京"


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

# dfA["DateTime"] = pd.to_datetime(dfA["DateTime"])
# dfB["DateTime"] = pd.to_datetime(dfB["DateTime"])
# dfC["DateTime"] = pd.to_datetime(dfC["DateTime"])

# span_rain_data_A = dfA[
#     (dfA["DateTime"] >= dt.datetime(2021, 1, 1))
#     & (dfA["DateTime"] < dt.datetime(2021, 10, 31))
#     & (dfA["降水量(mm)"] >= 0.1)
# ]

# span_rain_data_B = dfB[
#     (dfB["DateTime"] >= dt.datetime(2021, 1, 1))
#     & (dfB["DateTime"] < dt.datetime(2021, 10, 31))
#     & (dfB["降水量(mm)"] >= 0.1)
# ]
# span_rain_data_C = dfC[
#     (dfC["DateTime"] >= dt.datetime(2021, 1, 1))
#     & (dfC["DateTime"] < dt.datetime(2021, 10, 31))
#     & (dfC["降水量(mm)"] >= 0.1)
# ]

# days_over_count_A = span_rain_data_A["DateTime"].dt.date.nunique()
# days_over_count_B = span_rain_data_B["DateTime"].dt.date.nunique()
# days_over_count_C = span_rain_data_C["DateTime"].dt.date.nunique()


# print(
#     "沖縄で2021年1月1日から10月30日までに0.1mm以上の降水量を観測した日数は",
#     days_over_count_A,
#     "日です。",
# )
# print(
#     "大阪で2021年1月1日から10月30日までに0.1mm以上の降水量を観測した日数は",
#     days_over_count_B,
#     "日です。",
# )
# print(
#     "東京で2021年1月1日から10月30日までに0.1mm以上の降水量を観測した日数は",
#     days_over_count_C,
#     "日です。",
# )


# 相関係数
# df1 = pd.concat([dfA, dfB, dfC], axis=0)
# # print("列名一覧:", df1.columns)
# # df1.columns = df1.columns.str.strip()

# # print(df1)

# data_Correlation = df1[["降水量(mm)", "現地気圧(hPa)"]].corr().iloc[0, 1]


# print("降水量と気圧の相関係数：", data_Correlation)


# 各地点の気温の相関係数
dfA["DateTime"] = pd.to_datetime(dfA["DateTime"])
dfB["DateTime"] = pd.to_datetime(dfB["DateTime"])
dfC["DateTime"] = pd.to_datetime(dfC["DateTime"])

dfA.set_index("DateTime", inplace=True)
dfB.set_index("DateTime", inplace=True)
dfC.set_index("DateTime", inplace=True)

dfA.rename(columns=lambda x: f"{x}：沖縄", inplace=True)
dfB.rename(columns=lambda x: f"{x}：大阪", inplace=True)
dfC.rename(columns=lambda x: f"{x}：東京", inplace=True)

df2 = pd.concat([dfA, dfB, dfC], axis=1)

# correlation_temp_data = df2[["気温(℃)：沖縄", "気温(℃)：大阪", "気温(℃)：東京"]].corr()
# print(correlation_temp_data)
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation_temp_data, annot=True, fmt=".2f", cmap="coolwarm")
# plt.title("東京・大阪・沖縄の気温の相関係数")
# plt.show()

# 散布図
plt.figure(figsize=(8, 6))
plt.scatter(
    df2["現地気圧(hPa)：沖縄"], df2["降水量(mm)：沖縄"], label="沖縄", alpha=0.7
)
plt.scatter(
    df2["現地気圧(hPa)：大阪"], df2["降水量(mm)：大阪"], label="大阪", alpha=0.7
)
plt.scatter(
    df2["現地気圧(hPa)：東京"], df2["降水量(mm)：東京"], label="東京", alpha=0.7
)

plt.xlabel("気圧 (hPa)", fontsize=12)
plt.ylabel("降水量 (mm)", fontsize=12)
plt.title("降水量と気圧の散布図", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True)

plt.show()

# 時系列図
july_data = df2[df2.index.month == 7]

plt.figure(figsize=(10, 6))
plt.plot(july_data.index, july_data["気温(℃)：沖縄"], label="沖縄", linewidth=1.5)
plt.plot(july_data.index, july_data["気温(℃)：大阪"], label="大阪", linewidth=1.5)
plt.plot(july_data.index, july_data["気温(℃)：東京"], label="東京", linewidth=1.5)

plt.xlabel("日時", fontsize=12)
plt.ylabel("気温 (℃)", fontsize=12)
plt.title("地点別7月の気温の時系列図", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True)

plt.show()
