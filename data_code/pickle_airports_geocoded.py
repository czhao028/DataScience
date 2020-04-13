import pickle as pk
import csv
import pandas as pd
file_path = "../excel_data/AIRPORTSGEOCODED_MSA_COUNTY.csv"
with open(file_path, "r") as file:
    pandas_obj = pd.read_csv(file)

pandas_obj.to_pickle("./airports_geocoded.pk")
