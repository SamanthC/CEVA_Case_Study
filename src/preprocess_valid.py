import pandas as pd
from pathlib import Path
from datetime import datetime as dt
import warnings
from preprocess_train import TrainSet
warnings.filterwarnings('ignore')
from filter_functions import *

train_preprocessed = pd.read_csv("../Data/Train_preprocessed.csv")
train_preprocessed["Expected_Ship_Date"] = pd.to_datetime(train_preprocessed["Expected_Ship_Date"])


class ValidSet:
    def __init__(self, path = "../Data/Validation.csv"):
        """
        Initialize Validation set with path
        """
        self.df = pd.read_csv(path)

    def preprocess_valid(self):
        """
        Computes preprocessing before feature engineering
        """
        self.df = self.df.drop("ID", axis=1)
        #self.df = self.df.dropna()

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

        #Compute average delays for past shipments (at journey level and journey/item level)
        self.df["Delay_per_Journey_per_item"] = self.df.apply(lambda x : delay_per_Journey_per_item(train_preprocessed, x), axis=1)
        self.df["Delay_per_Journey"] = self.df.apply(lambda x : delay_per_Journey(train_preprocessed, x), axis=1)

        #Add ratios at route/item, route and supplier level by class
        self.df["0_ratio_sup_cust_item"] = self.df.apply(lambda x : zero_ratio_sup_cust_item(train_preprocessed, x), axis=1)   
        self.df["1_ratio_sup_cust_item"] = self.df.apply(lambda x : one_ratio_sup_cust_item(train_preprocessed, x), axis=1)
        self.df["2_ratio_sup_cust_item"] = self.df.apply(lambda x : two_ratio_sup_cust_item(train_preprocessed, x), axis=1)
        self.df["3_ratio_sup_cust_item"] = self.df.apply(lambda x : three_ratio_sup_cust_item(train_preprocessed, x), axis=1)

        self.df["0_ratio_sup_cust"] = self.df.apply(lambda x : zero_ratio_sup_cust(train_preprocessed, x), axis=1)
        self.df["1_ratio_sup_cust"] = self.df.apply(lambda x : one_ratio_sup_cust(train_preprocessed, x), axis=1)
        self.df["2_ratio_sup_cust"] = self.df.apply(lambda x : two_ratio_sup_cust(train_preprocessed, x), axis=1)
        self.df["3_ratio_sup_cust"] = self.df.apply(lambda x : three_ratio_sup_cust(train_preprocessed, x), axis=1)

        self.df["0_ratio_sup"] = self.df.apply(lambda x : zero_ratio_sup(train_preprocessed, x), axis=1)
        self.df["1_ratio_sup"] = self.df.apply(lambda x : one_ratio_sup(train_preprocessed, x), axis=1)
        self.df["2_ratio_sup"] = self.df.apply(lambda x : two_ratio_sup(train_preprocessed, x), axis=1)
        self.df["3_ratio_sup"] = self.df.apply(lambda x : three_ratio_sup(train_preprocessed, x), axis=1)
        
        self.df = self.df.fillna(0)

        self.df.to_csv("../Data/Valid_preprocessed.csv")