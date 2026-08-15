import pandas as pd
import numpy as np

def read_data_and_preprocess():
    try:
        df = pd.read_csv("data.csv")
    except Exception as e:
        print("An error occurred while reading the data:", e)
        return None
    
    if df.empty:
        print("The dataset is empty.")
        return None
    
    header = df.columns.tolist()
    if len(header) < 2:
        print("The dataset does not have enough columns.")
        return None
    if header[0] != "km" or header[1] != "price":
        print("The dataset does not have the expected headers.")
        return None
    
    data = np.array(df)

    if not np.issubdtype(data.dtype, np.number):
        print("The dataset contains non-numeric values.")
        return None
    mileage = data[:, 0]
    price = data[:, 1]
    return mileage, price

def training_data():
    mileage, price = read_data_and_preprocess()
    print("km:", mileage)
    print("price:", price)
    if mileage is None or price is None:
        print("Training data could not be loaded.")
        return None, None
    theta0 = 0
    theta1 = 0
    m = len(mileage)
    print("m:", m)

def main():
    print("Starting the training process...")
    try:
        training_data()
    except Exception as e:
        print("An error occurred:", e)
main()