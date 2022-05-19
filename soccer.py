import pandas as pd
dataset = pd.read_csv("./csv/mls-salaries-2017.csv")
# print(dataset)
# print(dataset.head(10))
# print(dataset.index)
# print(dataset.mean())
# print(dataset[(dataset["guaranteed_compensation"].max()) == (dataset["guaranteed_compensation"])])
# print(dataset[dataset["last_name"] == "Gonzalez Pirez"]["position"].iloc[0])
# print(dataset.groupby("position").mean())
# print(dataset["position"].nunique())
# # print(dataset["position"].value_counts())
# def function(x):
#     if "son" in x.lower():
#         return True
#     return False

# print(dataset[dataset["last_name"].apply(function)])
