from dataclasses import dataclass
import pandas as pd

@dataclass
class dataprep:
    dataframe: pd.DataFrame
    division: list
    numeric_features: float | int


    def division_prep(self):
        division = self.dataframe[self.division].unique()
        

