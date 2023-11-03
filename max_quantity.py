import pandas as pd

# read csv
df = pd.read_csv('practice_level_prescribing.csv')

#cal the sum and max of the QUALITY column
column_sum = df['QUANTITY'].sum()
max_value = df['QUANTITY'].max()

#percentage
max_value_percentage = (max_value / df['QUANTITY'].sum()) * 100
print(max_value_percentage)

import unittest
import pandas as pd

# Function for calculating max value percentage
def calculate_max_value_percentage(data, column_name):
    max_value = data[column_name].max()
    max_value_percentage = (max_value / data[column_name].sum()) * 100
    return max_value_percentage

# Unit Test Class
class TestMaxValuePercentage(unittest.TestCase):

    def test_max_value_percentage(self):
        # Sample data to simulate an existing DataFrame
        df = pd.DataFrame({
            'QUANTITY': [5, 10, 15, 20, 25]  # Simulating existing DataFrame with a 'QUANTITY' column
        })

        # Call the function to calculate the max value percentage
        result = calculate_max_value_percentage(df, 'QUANTITY')

        # Calculate the expected result
        expected_percentage = df['QUANTITY'].max() / df['QUANTITY'].sum() * 100

        # Assert whether the result matches the expected percentage
        self.assertAlmostEqual(result, expected_percentage, delta=0.001)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)