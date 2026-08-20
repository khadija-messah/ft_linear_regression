import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python predict.py <mileage>")
        return

    try:
        mileage = float(sys.argv[1])
    except ValueError:
        print("Please enter a valid mileage value.")
        return

    with open("model_parameters.txt", "r") as f:
        theta0, theta1, mileage_min, mileage_max = map(
            float,
            f.read().split(",")
        )

    normalized_mileage = (
        mileage - mileage_min
    ) / (mileage_max - mileage_min)

    estimated_price = theta0 + theta1 * normalized_mileage

    print(f"Estimated price for {mileage} km: {estimated_price}")


if __name__ == "__main__":
    main()