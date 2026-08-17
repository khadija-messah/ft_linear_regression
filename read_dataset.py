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

    mileage1, mileage_min, mileage_max = normalize_data(mileage)
    if mileage is None or price is None:
        print("Training data could not be loaded.")
        return None, None
    return mileage1, price

def normalizeAndError(file_path):
    mileage, price = read_data_and_preprocess(file_path)
    if mileage is None or price is None:
        return None, None
    print("Starting the training process...")
    theta0 = 0
    theta1 = 0
    theta0, theta1 = train_model(mileage, price, theta0, theta1)
    return theta0, theta1


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def normalize_data(mileage):
     normalized_mileage = (mileage - mileage.min()) / (mileage.max() - mileage.min())
     return normalized_mileage,mileage.min(), mileage.max()


def train_model(mileage, price, theta0, theta1, learning_rate=0.01, num_iterations=1000):
    m = len(mileage)
    for i in range(num_iterations):
        estimated_price = estimate_price(mileage, theta0, theta1)
        error = estimated_price - price
        sum_error_price = np.sum(error)
        average_error = sum_error_price / m
        tmpθ0 = learning_rate * average_error

        sum_error_mileage = np.sum(error * mileage)
        average_error_mileage = sum_error_mileage / m
        tmpθ1 = learning_rate * average_error_mileage

        theta0 -= tmpθ0
        theta1 -= tmpθ1
    print(f"Training completed. Final parameters: theta0 = {theta0}, theta1 = {theta1}")
    return theta0, theta1
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2 or not sys.argv[1].endswith('.csv'):
        print("please enter 1 dataset file name with .csv extension")
        return
    try:
        theta0, theta1 = normalizeAndError(sys.argv[1])
        estimated_price = estimate_price(15000, theta0, theta1)
        print(f"Estimated price for 15000 km: {estimated_price}")
    except Exception as e:
        print("An error occurred:", e)
main()