import pandas

def calculate_average(data_list):
    if not data_list:
        return 0
    df = pandas.Series(data_list)
    return df.mean()

if __name__ == "__main__":
    print("Average calculation logic loaded successfully.")
    test_data = [10, 20, 30, 40]
    result = calculate_average(test_data)
    print(f"Test data: {test_data}")
    print(f"Calculated average using pandas: {result}")
