import pandas as pd
from pathlib import Path
from datetime import datetime as dt
import warnings
warnings.filterwarnings('ignore')

class TrainSet:
    def __init__(self, path = "../Data/Train.csv"):
        """
        Initialize Trainset with path
        """
        self.df = pd.read_csv(path)

    def preprocess_train(self):
        """
        Computes preprocessing before feature engineering
        """
        self.df = self.df.drop("ID", axis=1)
        self.df = self.df.dropna()

        #Preprocessing of Expected Shipment Date column
        self.df["Expected_Ship_Date"] = pd.to_datetime(self.df["Expected_Ship_Date"])
        self.df["Date"] = self.df["Expected_Ship_Date"].dt.to_period("D")
        self.df["Year-Month"] = self.df["Expected_Ship_Date"].dt.to_period("M")
        self.df["Year"] = self.df["Expected_Ship_Date"].dt.year
        self.df["Month"] = self.df["Expected_Ship_Date"].dt.month
        self.df["Week"] = self.df["Expected_Ship_Date"].dt.week
        self.df["Weekday"] = self.df["Expected_Ship_Date"].dt.weekday
        self.df["Day"] = self.df["Expected_Ship_Date"].dt.day
        self.df["Time"] = self.df["Expected_Ship_Date"].dt.time
        self.df["Is_Jan"] = self.df["Month"].apply(lambda x : 1 if x == 1 else 0)
        self.df["Is_Mon"] = self.df["Weekday"].apply(lambda x : 1 if x == 0 else 0)


        #Drop duplicates
        self.df = self.df.drop_duplicates()

        #Keep rows in 2018
        self.df = self.df[self.df["Year"] == 2018]

        #Keep rows with delays between -60 days and 100 days (Business rule)
        self.df = self.df[(self.df["Delay"]>=-60) & (self.df["Delay"]<=100)].sort_values("Expected_Ship_Date")

        #Label encoding
        label_dict = {
            "No Delay" : 0,
            "Small Delay" : 1,
            "Medium Delay" : 2,
            "High Delay" : 3
        }
        self.df["Delay_Class"] = self.df["Delay_Class"].map(label_dict)
        
        #Negatives delays set to zero for ratios calculation
        self.df["Delay_new"] = self.df["Delay"].apply(lambda x : 0 if x<=0 else x)

        #Compute average delays for past shipments (at journey level and journey/item level)
        self.df["Delay_per_Journey_per_item"] = self.df.groupby(["Origin_Alias","Destination_Alias", "Part_Number"])["Delay_new"].apply(lambda x: x.shift().expanding().mean())
        self.df["Delay_per_Journey"] = self.df.groupby(["Origin_Alias","Destination_Alias"])["Delay_new"].apply(lambda x: x.shift().expanding().mean())

        #Add dummy columns from delay_class to compute ratios
        self.df = pd.concat([self.df, pd.get_dummies(self.df["Delay_Class"], prefix = "class")], axis=1)

        #3 columns added for raio computation (denominator)
        self.df["count_tuple_sup_cust_item"] = self.df.groupby(["Part_Number", "Origin_Alias", "Destination_Alias"]).cumcount()
        self.df["count_tuple_sup_cust"] = self.df.groupby(["Origin_Alias", "Destination_Alias"]).cumcount()
        self.df["count_sup"] = self.df.groupby(["Origin_Alias"]).cumcount()

        #Add ratios at route/item, route and supplier level by class
        list_class = [0, 1 ,2, 3]

        for i in list_class:
            self.df["{}_ratio_sup_cust_item".format(i)] = self.df. \
                groupby(["Part_Number", "Origin_Alias", "Destination_Alias"])["class_{}".format(i)]. \
                apply(lambda x : x.shift().cumsum())/self.df["count_tuple_sup_cust_item"]

            self.df["{}_ratio_sup_cust".format(i)] = self.df. \
                groupby(["Origin_Alias", "Destination_Alias"])["class_{}".format(i)]. \
                apply(lambda x : x.shift().cumsum())/self.df["count_tuple_sup_cust"]

            self.df["{}_ratio_sup".format(i)] = self.df. \
                groupby(["Origin_Alias"])["class_{}".format(i)]. \
                apply(lambda x : x.shift().cumsum())/self.df["count_sup"]

        self.df = self.df.fillna(0)
        

        self.df.to_csv("../Data/Train_preprocessed.csv")

