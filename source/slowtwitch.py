from datetime import datetime
import pandas as pd
import os


class SlowtwitchDatabase:

    def __init__(self):
        self.file_name = self.find_most_recent_csv()
        self.dataframe = None
        if self.file_name is not None:
            self.dataframe = pd.read_csv(self.file_name,
                                         header=1,
                                         usecols=['Brand',
                                                  'Model',
                                                  'Tri/Road',
                                                  'Size',
                                                  'Stack',
                                                  'Reach',
                                                  'Trail',
                                                  'Front Center',
                                                  'Head Tube',
                                                  "Wheelsize"]
                                         ).dropna(how="any")
            print(self.dataframe)

    def is_database_found(self):
        return self.dataframe is not None

    def find_most_recent_csv(self):
        most_recent_db = None
        most_recent_date = None
        for dirName, subdirList, fileList in os.walk('./slowtwitch_database', topdown=True):
            for file in fileList:
                if file.startswith("DB") and file.endswith(".csv"):
                    date = file[2:10]
                    date = datetime.strptime(date, "%d%m%Y")
                    if most_recent_date is None or date > most_recent_date:
                        most_recent_date = date
                        most_recent_db = str(dirName + "/" + file)
        return most_recent_db

    def get_stack_reach_matches(self, stack, reach, search_radius=10):
        if not self.is_database_found():
            return None
        matches = self.dataframe[self.dataframe['stack'].between(
            stack - search_radius,
            stack + search_radius
        )]
        matches = matches[matches['reach'].between(
            reach - search_radius,
            reach + search_radius
        )]
        return matches
