import pandas as pd
import os

# Given constants
rho = 1.184  # Density of air (kg/m^3)
mu = 1.849e-5  # Dynamic viscosity (kg/m·s)
Ap = 0.05  # Approximate projected area (m^2)
zero_error_L = 0.485  # Zero error for lift
zero_error_D = -6.495  # Zero error for drag

# Data for alpha = 20 degrees
alpha_20_data = {
    "Frequency (Hz)": [10, 15, 20, 25, 30, 35, 40],
    "D_recorded": [-6.573, -6.675, -6.82, -7.027, -7.29, -7.597, -7.98],
    "L_recorded": [0.563, 0.703, 0.92, 1.23, 1.59, 2.08, 2.73]
}

# Convert data into a DataFrame
df = pd.DataFrame(alpha_20_data)

# Correct the D and L values by subtracting zero errors
df["D_corrected"] = df["D_recorded"] - zero_error_D
df["L_corrected"] = df["L_recorded"] - zero_error_L

# Calculate the drag and lift forces (F_D and F_L)
df["F_D"] = df["D_corrected"] * 9.81
df["F_L"] = df["L_corrected"] * 9.81

# Calculate velocity V
df["V"] = 1.594 * df["Frequency (Hz)"] + 0.995

# Calculate drag coefficient C_D and lift coefficient C_L using the formula for airfoil
df["C_D"] = 53.82 * (df["F_D"] / df["V"]**2)
df["C_L"] = 53.82 * (df["F_L"] / df["V"]**2)

# Calculate Reynolds number Re
df["Re"] = (rho * df["V"] * 0.05) / mu  # Using characteristic length of 0.05 m for airfoil

# Display the resulting DataFrame
df

# Define the specific path to save the Excel file in your Downloads folder
output_path = r"C:\Users\youss\Downloads\airfoil_alpha_20_results.xlsx"

# Save the DataFrame to an Excel file
df.to_excel(output_path, index=False)

print(f"Results have been saved to {output_path}")

