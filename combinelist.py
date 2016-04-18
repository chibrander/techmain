import pandas as pd

all = pd.read_excel("excel/myfile316.xlsx")

for file in range(317,718):
    df = pd.read_excel("excel/myfile" + str(file) + ".xlsx")
    all = pd.concat([all,df])

all.to_excel("all.xlsx")
