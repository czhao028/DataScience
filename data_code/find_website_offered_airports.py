import re
import xlrd

loc = ("../excel_data/airport_data/AIRPORTS_FLIGHT24.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.nrows)
airport_codes = set()
for i in range(1, sheet.nrows):
    value = sheet.cell_value(i, 0)
    match = re.search("\((.*)\/.*\)", value)
    if match == None:
        break
    g0 = match.group(1)
    print(g0)

    airport_codes.add(g0)

print(len(airport_codes))
