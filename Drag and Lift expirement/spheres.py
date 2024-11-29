import pandas as pd
import numpy as np

# Constants
diameter_sphere = 0.0508  # m (diameter of the sphere)
A_f_sphere = (np.pi / 4) * diameter_sphere ** 2  # Projected area for the sphere
rho = 1.184  # kg/m^3 (density of air)
mu = 1.849e-5  # kg/m.s (dynamic viscosity)
g = 9.81  # m/s^2 (gravitational acceleration)
D0 = -6.495 # Zero error for drag

# Data for the smooth sphere (no lift)
smooth_sphere_data = {
    "Frequency (Hz)": [10, 15, 20, 25, 30, 35, 40],
    "D_recorded": [-6.45, -6.462, -6.485, -6.51, -6.53, -6.66, -6.69]
}

# Convert data into a DataFrame
smooth_sphere_df = pd.DataFrame(smooth_sphere_data)

# Correct the D values by subtracting the zero error for drag
smooth_sphere_df["D_corrected"] = smooth_sphere_df["D_recorded"] - D0

# Calculate the drag force F_D
smooth_sphere_df["F_D"] = smooth_sphere_df["D_corrected"] * g

# Calculate velocity V
smooth_sphere_df["V"] = 1.594 * smooth_sphere_df["Frequency (Hz)"] + 0.995

# Calculate drag coefficient C_D for the sphere
smooth_sphere_df["C_D"] = smooth_sphere_df["F_D"] / (0.5 * rho * smooth_sphere_df["V"]**2 * A_f_sphere)

# Calculate Reynolds number Re for the sphere
smooth_sphere_df["Re"] = (rho * smooth_sphere_df["V"] * diameter_sphere) / mu

# Define the path to save the results in the Downloads folder (modify if necessary)
output_path = r"C:\Users\youss\Downloads\smooth_sphere_results.xlsx"

# Save the results to an Excel file
smooth_sphere_df.to_excel(output_path, index=False)
print(f"Results have been saved to {output_path}")
