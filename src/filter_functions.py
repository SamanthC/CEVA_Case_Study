def delay_per_Journey_per_item(train, row):
    result = train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["Delay_new"].mean()
    return result

def delay_per_Journey(train, row):
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["Delay_new"].mean()
    return result

def zero_ratio_sup_cust_item(train, row) : 
    result = train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_0"].sum()/ \
    len(train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result
    
def one_ratio_sup_cust_item(train, row) : 
    result = train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_1"].sum()/ \
    len(train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def two_ratio_sup_cust_item(train, row) : 
    result = train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_2"].sum()/ \
    len(train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def three_ratio_sup_cust_item(train, row) : 
    result = train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_3"].sum()/ \
    len(train[(train["Part_Number"] == row["Part_Number"]) &
      (train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def zero_ratio_sup_cust(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_0"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result
    
def one_ratio_sup_cust(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_1"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def two_ratio_sup_cust(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_2"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def three_ratio_sup_cust(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_3"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Destination_Alias"] == row["Destination_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def zero_ratio_sup(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_0"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result
    
def one_ratio_sup(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_1"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def two_ratio_sup(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_2"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result

def three_ratio_sup(train, row) : 
    result = train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])]["class_3"].sum()/ \
    len(train[(train["Origin_Alias"] == row["Origin_Alias"]) &
      (train["Expected_Ship_Date"] < row["Expected_Ship_Date"])])
    return result