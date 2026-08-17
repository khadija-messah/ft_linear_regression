import pandas as pd
import numpy as np
import sys

def read_data_and_preprocess(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print("An error occurred while reading the data:", e)
        return 
    
    if df.empty:
        print("The dataset is empty.")
        return
    
    header = df.columns.tolist()
    if len(header) < 2:
        print("The dataset does not have enough columns.")
        return 
    if header[0] != "km" or header[1] != "price":
        print("The dataset does not have the expected headers.")
        return 
    
    data = np.array(df)

    if not np.issubdtype(data.dtype, np.number):
        print("The dataset contains non-numeric values.")
        return 
    mileage = data[:, 0]
    price = data[:, 1]
    print("Original mileage:", mileage)
    print("Original price:", price)
    print("--------------------------------\n\n")
    mileage, mileage_min, mileage_max = normalize_data(mileage)
    print("Normalized mileage:", mileage)
    print("denormalized mileage:", denormalize_data(mileage, mileage_min, mileage_max))

    return mileage, price

def training_data(file_path):
    print("here\n\n")
    mileage, price = read_data_and_preprocess(file_path)
    print("here1",mileage," \n\n",price)
    if mileage is None or price is None:
        print("Training data could not be loaded.")
        return None, None
    print("Starting the training process...")
    theta0 = 0
    theta1 = 0
    m = len(mileage)
    estimated_price = estimate_price(mileage, theta0, theta1)
    print("Estimated price:", estimated_price)

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def normalize_data(mileage):
     normalized_mileage = (mileage - mileage.min()) / (mileage.max() - mileage.min())
     return normalized_mileage,mileage.min(), mileage.max()


def denormalize_data(normalized_mileage, mileage_min, mileage_max):
    mileage = normalized_mileage * (mileage_max - mileage_min) + mileage_min
    return mileage


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2 or not sys.argv[1].endswith('.csv'):
        print("please enter 1 dataset file name with .csv extension")
        return
    try:
        training_data(sys.argv[1])
    except Exception as e:
        print("An error occurred:", e)
main()