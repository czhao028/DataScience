import pickle as pk
# import csv
import pandas as pd
file_path = "../excel_data/airport_data/AIRPORTSGEOCODED_MSA_COUNTY.csv"
website_data_path = "../excel_data/airport_data/AIRPORTS_FLIGHT24.xlsx"
with open(file_path, "r") as file:
    pd_obj = pd.read_csv(file)

flight24 = pd.read_excel(website_data_path, sheet_name="Sheet1")

pd_obj = pd.merge(left=pd_obj, right=flight24, left_on="iata_code", right_on="iata_code")
airportcode_to_county = pd.Series(pd_obj["County, State"].values, index=pd_obj["iata_code"]).to_dict()

with open("airports_geocoded.pk", "wb") as pik:
    pk.dump(airportcode_to_county, pik)

