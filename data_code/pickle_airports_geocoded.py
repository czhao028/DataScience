# import pickle as pk
# import csv
import pandas as pd
# file_path = "../excel_data/airport_data/AIRPORTSGEOCODED_MSA_COUNTY.csv"
# with open(file_path, "r") as file:
#     pandas_obj = pd.read_csv(file)
#
# pandas_obj.to_pickle("./airports_geocoded.pk")

with open("test.csv", "r") as f:
    pd_obj = pd.read_csv(f)
    airportcode_to_county = pd.Series(pd_obj["County"], index=pd_obj["Airport Code"].values).to_dict()
    airportcode_to_county
