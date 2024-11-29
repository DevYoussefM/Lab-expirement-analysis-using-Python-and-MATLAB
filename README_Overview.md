# Film and Dropwise Condensation Experiment

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js"></script>

This repository contains a Python script to automate the analysis of experimental data for comparing **Film-wise** and **Drop-wise condensation**. It processes input data, computes critical thermal properties, and exports the results as an Excel file for lab reports.

---

## Overview

This project supports experiments focused on:
- **Film-wise condensation**: Characterized by a continuous liquid film over the surface, reducing heat transfer efficiency.
- **Drop-wise condensation**: Involves discrete droplet formation, significantly enhancing heat transfer rates.

The analysis includes:
1. Heat transfer rate \( Q \).
2. Heat flux \( q \).
3. Adjusted surface temperatures \( T_{\text{adjusted}} \).
4. Heat transfer coefficients \( h \).

---

## Script Features

### 1. Heat Transfer Rate
The heat transfer rate is calculated as:

$$
Q = \dot{m} \cdot c_p \cdot (T_{\text{out}} - T_{\text{in}})
$$

Where:
- \( \dot{m} \): Mass flow rate (kg/s)  
- \( c_p \): Specific heat capacity of water (\( 4.18 \, \text{kJ/kg·°C} \))  
- \( T_{\text{out}}, T_{\text{in}} \): Cooling water outlet and inlet temperatures  

---

### 2. Heat Flux
The heat flux is computed using:

$$
q = \frac{Q}{A}
$$

Where:
- \( A = \pi \cdot d \cdot L \): Surface area of the condenser (m²)

---

### 3. Adjusted Surface Temperature
The adjusted surface temperature is given by:

$$
T_{\text{adjusted}} = q \cdot \frac{x}{k} + T_{\text{initial}}
$$

Where:
- \( \frac{x}{k} \): Thermal conductivity factor (\( 2 \times 10^{-6} \, \text{m·K/W} \))

---

### 4. Heat Transfer Coefficient
The heat transfer coefficient is calculated as:

$$
h = \frac{q}{T_{\text{sat}} - T_{\text{adjusted}}}
$$

Where:
- \( T_{\text{sat}} \): Saturation temperature (\( 80^\circ\text{C} \))

---

### 5. Data Integrity Check
The script ensures:
- All input lists are of equal length.
- Automatically adjusts mismatched lengths with placeholders to maintain consistent data.

---

### 6. Automated Thermal Analysis
The script computes:
- \( Q, q, T_{\text{adjusted}}, h \) for both film-wise and drop-wise condensation modes.

---

### 7. Excel Output
Results are saved as an Excel file in the **Downloads folder**, containing all raw and computed data for easy use in lab reports.

---

## Output Example
The output Excel sheet contains:
- **Experimental data columns**: \( P_{\text{gage}}, T_1, T_3, T_4, T_6, T_7, \dot{m}_d, \dot{m}_f \)
- **Computed columns**: \( Q, q, T_{\text{adjusted}}, h \) for both modes of condensation.

---

Feel free to contribute by opening an issue or submitting a pull request!