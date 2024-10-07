import pandas as pd
import numpy as np

# Given retirement data
retirement_data = {
    'age': [25, 30, 35, 40, 45, 50, 55, 60, 67],
    'retirement_multiplier': [0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 10.0]
}

# Extract age and retirement_multiplier
ages_given = retirement_data['age']
multipliers_given = retirement_data['retirement_multiplier']

# Create a list to store the estimated values
age_range = np.arange(ages_given[0], ages_given[-1] + 1)

# Initialize the estimated multipliers list with the first known value
estimated_multipliers = [multipliers_given[0]]

# Loop through the pairs of known ages and calculate growth rate for each segment
for i in range(1, len(ages_given)):
    age_start, age_end = ages_given[i - 1], ages_given[i]
    multiplier_start, multiplier_end = multipliers_given[i - 1], multipliers_given[i]

    # Calculate the number of years between the two ages
    num_years = age_end - age_start

    # Calculate the growth rate for this specific interval
    growth_rate = (multiplier_end / multiplier_start) ** (1 / num_years) - 1

    # Estimate multipliers for each year in this range
    for j in range(1, num_years + 1):
        new_multiplier = estimated_multipliers[-1] * (1 + growth_rate)
        estimated_multipliers.append(new_multiplier)

# Create a DataFrame with the age range and estimated retirement multipliers
df_estimated_multipliers = pd.DataFrame({
    'age': age_range,
    'estimated_multiplier': estimated_multipliers
})

import os
from global_inputs.inputs import file_path

# Create the exports folder if it doesn't exist
os.makedirs(file_path, exist_ok=True)

# Export each DataFrame to a CSV file at the specified file path
df_estimated_multipliers.to_csv(os.path.join(file_path, 'df_estimated_multipliers.csv'), index=False)

