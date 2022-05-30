from preprocess_train import TrainSet
from preprocess_valid import ValidSet
from model import Model
from sklearn.linear_model import LogisticRegression
import pandas as pd
import datetime
import os.path

#Definition of the grid search that will be applied to get the best model
HYPERPARAM = {
    'log_reg__solver': ['liblinear', 'lbfgs'],
    'log_reg__C': [0.0001, 0.001, 0.01, 0.1, 1]
}

#Definition of features that will be used for training the model
FEATURES = [
    "Delay_per_Journey_per_item", "Delay_per_Journey", "0_ratio_sup_cust_item",
    "1_ratio_sup_cust_item", "2_ratio_sup_cust_item", "3_ratio_sup_cust_item", 
    "0_ratio_sup_cust", "1_ratio_sup_cust", "2_ratio_sup_cust", "3_ratio_sup_cust", 
    "0_ratio_sup", "1_ratio_sup", "2_ratio_sup", "3_ratio_sup" 
]

#Definition of the model
model = Model(
    name = "log_reg",
    estimator = LogisticRegression(),
    hyperparam = HYPERPARAM
)

if __name__ == '__main__':

    #Computation of preprocessed train and validation if not already done
    if not os.path.isfile("../Data/Train_preprocessed.csv"):
        train = TrainSet()
        train.preprocess_train()
    if not os.path.isfile("../Data/Valid_preprocessed.csv"):
        valid = ValidSet()
        valid.preprocess_valid()

    #Importation of preprocessed datasets
    train_preprocessed = pd.read_csv("../Data/Train_preprocessed.csv")
    valid_preprocessed = pd.read_csv("../Data/Valid_preprocessed.csv")

    #Splitting of features and label datasets for modelling
    X_train = train_preprocessed[FEATURES]
    y_train = train_preprocessed["Delay_Class"]
    X_valid = valid_preprocessed[FEATURES]

    #Modelling and prediction
    model.choose_best_params(X_train, y_train)
    predict = model.estimator.predict(X_valid)


    #Edition of results
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_valid = pd.concat([ 
        pd.read_csv("../Data/Validation.csv"),
        pd.Series(predict, name = "result").map({0 : "No Delay ",1 : "Small Delay", 2 : "Medium Delay", 3 : "High Delay"})
    ], axis=1)
    csv_valid.to_csv("../Data/{}.csv".format(timestamp))


