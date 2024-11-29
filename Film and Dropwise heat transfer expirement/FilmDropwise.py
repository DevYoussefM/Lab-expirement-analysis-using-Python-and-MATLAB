import pandas as pd
import numpy as np
import os

data = {
    "T2 (°C)": [97.7, 96.7, 95.7, 95.4, 95, 94.5, 94.1, 93.8, 93.9, 93.7],
    "T3 (°C)": [21.4, 21, 20.6, 20.5, 20.7, 20.5, 20.5, 20.4, 20.6, 20.3],
    "T4 (°C)": [62.4, 51.8, 43.9, 39.7, 36.8, 34.9, 33.3, 32.3, 31.8, 31.1],
    "T5 (°C)": [97.2, 95, 91.7, 90.6, 88.9, 87.1, 86.4, 84.8, 83, 82.6],
    "T6 (°C)": [21.6, 21.3, 20.7, 20.8, 20.5, 20.6, 20.5, 20.3, 20.4, 20.2],
    "T7 (°C)": [65.2, 61, 54.3, 49.8, 46.6, 44.8, 43.7, 40.8, 38.3, 36.7],
    "md (g/s)": [4, 8, 12, 16, 20, 24, 28, 32, 36, 38],
    "mf (g/s)": [1, 2, 3.5, 4.5, 6, 7, 8, 9.5, 11, 12],
}

cp = 4.18  # Specific heat capacity of water (kJ/kg·K)
x_k = 2e-6  # Conductivity factor (m·K/W)
d = 12.7e-3  # Diameter (m)
L = 0.09  # Length (m)
area = np.pi * d * L  # Surface area (m^2)
T_sat = 100  # Saturation temperature (°C)

df = pd.DataFrame(data)
df["Qd (kW)"] = (df["md (g/s)"] / 1000) * cp * (df["T4 (°C)"] - df["T3 (°C)"])
df["qd (kW/m^2)"] = df["Qd (kW)"] / area
df["T2"] = df["qd (kW/m^2)"] * x_k + df["T2 (°C)"]
df["hd (kW/m^2·°C)"] = df["qd (kW/m^2)"] / (T_sat - df["T2"])

df["Qf (kW)"] = (df["mf (g/s)"] / 1000) * cp * (df["T7 (°C)"] - df["T6 (°C)"])
df["qf (kW/m^2)"] = df["Qf (kW)"] / area
df["T5"] = df["qf (kW/m^2)"] * x_k + df["T5 (°C)"]
df["hf (kW/m^2·°C)"] = df["qf (kW/m^2)"] / (T_sat - df["T5"])

downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
output_file = os.path.join(downloads_dir, "Condensation_Results_100.xlsx")
df.to_excel(output_file, index=False)

print(f"Excel file saved at: {output_file}")
