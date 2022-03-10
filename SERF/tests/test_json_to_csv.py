import unittest
import json_to_csv

import geopandas as gp
import pandas as pd
import datetime as dt
import numpy as np

lst = [1, 2, 3, 4, 5, 6]
dummydf = pd.DataFrame(lst)

sample2 = 'NASA/POWER_Point_Monthly_Timeseries_1981_2020_047d6155N_122d2917W_LST.csv'
sample3 = 'NASA/POWER_Point_Monthly_Timeseries_1981_2020_047d5590N_122d7195W_LST.json'

data = json_to_csv.import_geojson(sample3)
convert = json_to_csv.convert_data(data)
monthly = json_to_csv.remove_annual(convert)
dated = json_to_csv.to_datetime(monthly)
df = json_to_csv.geojson_to_csv(sample3)

class TestJsonToCsv(unittest.TestCase):
    
    
    def test_import(self):
        # check that import_geojson imports a .json
        sample2 = 'NASA/POWER_Point_Monthly_Timeseries_1981_2020_047d6155N_122d2917W_LST.csv'
        self.assertRaises(TypeError, json_to_csv.import_geojson, sample2)
        
    def test_remove(self):
        # remove only the 13th 'month' from the pandas df. no more, no less.
        lst = [1, 2, 3, 4, 5, 6]
        dummydf = pd.DataFrame(lst)
        self.assertRaises(AttributeError, json_to_csv.remove_annual, dummydf)
        
    def test_all(self):
        lst = [1, 2, 3, 4, 5, 6]
        dummydf = pd.DataFrame(lst)
        sample3 = 'NASA/POWER_Point_Monthly_Timeseries_1981_2020_047d5590N_122d7195W_LST.json'
        data = json_to_csv.import_geojson(sample3)
        self.assertRaises(AttributeError, json_to_csv.geojson_to_csv, dummydf)
        
        
        