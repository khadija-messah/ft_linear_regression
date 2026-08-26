import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
import os

def verify_input(inpt):

    try:
        x = int(inpt)
    except ValueError:
        print("wrong input")
        return False
    return int(inpt)


def check_path_parameters():

    a = Path("model_parameters.txt")
    if not a.exists():
        print("file of paramaters.txt doesn't exists")
        return False
    x = os.stat("model_parameters.txt").st_size
    if x == 0:
        print("empty file")
    return True

def print_paramettre(input_mileage,mileage_min,mileage_max,normalized_input,theta0,theta1 ):
    print("input_mileage:", input_mileage)
    print("mileage_min:", mileage_min)
    print("mileage_max:", mileage_max)
    print("normalized_input:", normalized_input)
    print("theta0:", theta0)
    print("theta1:", theta1)

def calcule_predection_price(input_mileage):
    with open("model_parameters.txt", "r") as f:
            theta0, theta1, mileage_min, mileage_max = map(
                float,
                f.read().split(",")
            )
        
    normalized_input = (
            input_mileage - mileage_min
        ) / (mileage_max - mileage_min)
    estimated_price = theta0 + theta1 * normalized_input
    print_paramettre(input_mileage,mileage_min,mileage_max,normalized_input,theta0,theta1)
    print(f"Estimated price for {input_mileage} km: {estimated_price}")
    graph_data(mileage_min,mileage_max,theta0,theta1)
    return estimated_price

def graph_data(mileage_min,mileage_max,theta0,theta1):
    km_values = np.linspace(mileage_min, mileage_max, 100)
    normalized_km_values = (km_values - mileage_min) / (mileage_max - mileage_min)
    price_values = theta0 + theta1 * normalized_km_values

    f = pd.read_csv("data.csv")
    x = f.columns.tolist()

    plt.scatter(f[x[0]], f[x[1]], color='blue', label='Data Points')
    plt.plot(km_values, price_values, color='red', label='Linear Regression')
    calcule_precision_model(f[x[1]],f[x[0]],theta0,theta1,mileage_min,mileage_max)


def calcule_precision_model(prices,km,theta0,theta1,mileage_min,mileage_max):
    calculated_mean_price = np.mean(prices)
    ss_total= np.sum((prices - calculated_mean_price) ** 2)
    ss_residual = np.sum((prices - (theta0 + theta1 * ((km - mileage_min) / (mileage_max - mileage_min)))) ** 2)
    r_squared = 1 - (ss_residual / ss_total)
    print("precision model is:", r_squared)


def save_graph(input_mileage,estimated_price):

    f = pd.read_csv("data.csv")
    x = f.columns.tolist()
    plt.title(f"Estimated Price for Mileage {input_mileage} km",fontdict={'family':'serif','color':'pink','size':12})
    plt.plot(input_mileage, estimated_price, marker='o', markersize=8, color='green', label='Estimated Price')
    plt.xlabel(x[0])
    plt.ylabel(x[1])
    plt.grid(color = 'pink', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.savefig("prediction.png")


def main():
     
    while(True):
        inpt = input("write the mealge you want to know him price : \n")
        input_mileage = verify_input(inpt)
        if not input_mileage :
            return 
        
        if not check_path_parameters():
            return
        with open("model_parameters.txt", "r") as f:
            theta0, theta1, mileage_min, mileage_max = map(
                float,
                f.read().split(",")
            )
        estimated_price = calcule_predection_price(input_mileage)
        save_graph(input_mileage,estimated_price)
        return
if __name__ == "__main__":
    main()