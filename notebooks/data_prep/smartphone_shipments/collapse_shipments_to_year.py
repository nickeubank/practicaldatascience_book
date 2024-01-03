import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)

ships = pd.read_csv("shipments_by_quarter.csv")
ships = ships.drop(columns="Q")
annual = ships.groupby("Year", as_index=False).sum()
rotated = annual.set_index("Year").T
rotated = rotated.reset_index()

rotated = rotated.rename(lambda x: "shipments_" + str(x), axis="columns")
rotated = rotated.rename(columns={"shipments_index": "vendor"})
rotated.to_csv("annual_smartphone_shipments_by_vendor.csv", index=False)


test = pd.read_csv("annual_smartphone_shipments_by_vendor.csv")
