import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def main():
    if len(sys.argv) != 2:
        print("Usage: python predict.py <mileage>")
        return

    try:
        input_mileage = float(sys.argv[1])
    except ValueError:
        print("Please enter a valid mileage value.")
        return

    with open("model_parameters.txt", "r") as f:
        theta0, theta1, mileage_min, mileage_max = map(
            float,
            f.read().split(",")
        )
    normalized_input = (
        input_mileage - mileage_min
    ) / (mileage_max - mileage_min)
    estimated_price = theta0 + theta1 * normalized_input


    print("input_mileage:", input_mileage)
    print("mileage_min:", mileage_min)
    print("mileage_max:", mileage_max)
    print("normalized_input:", normalized_input)
    print("theta0:", theta0)
    print("theta1:", theta1)


    f = pd.read_csv("data.csv")
    x = f.columns.tolist()
    km_values = np.linspace(mileage_min, mileage_max, 100)
    normalized_km_values = (km_values - mileage_min) / (mileage_max - mileage_min)
    price_values = theta0 + theta1 * normalized_km_values

    print(f"Estimated price for {input_mileage} km: {estimated_price}")

    plt.scatter(f[x[0]], f[x[1]], color='blue', label='Data Points')
    plt.plot(km_values, price_values, color='red', label='Linear Regression')

    

    calculated_mean_price = np.mean(f[x[1]])
    print("calculated_mean_price:", calculated_mean_price)
    ss_total= np.sum((f[x[1]] - calculated_mean_price) ** 2)
    print("total_sum_of_squares:", ss_total)

    ss_residual = np.sum((f[x[1]] - (theta0 + theta1 * ((f[x[0]] - mileage_min) / (mileage_max - mileage_min)))) ** 2)
    print("residual_sum_of_squares:", ss_residual)

    r_squared = 1 - (ss_residual / ss_total)
    print("R-squared value:", r_squared)

    plt.title("km,prix")
    plt.xlabel(x[0])
    plt.ylabel(x[1])
    plt.legend()
    # plt.show()

if __name__ == "__main__":
    main()