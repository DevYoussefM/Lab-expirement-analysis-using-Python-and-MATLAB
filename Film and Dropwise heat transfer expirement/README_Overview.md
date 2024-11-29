
# Film and Dropwise Condensation Experiment  

This document describes a Python script that automates the analysis of experimental data for comparing **Film-wise** and **Drop-wise condensation**. The script processes input data, computes critical thermal properties, and exports the results as an Excel file suitable for lab reports.  


## Objective  

The primary objective of this experiment is to compare the heat transfer coefficient ($h$) of **film-wise condensation** and **drop-wise condensation**. By analyzing the experimental data, the script highlights the differences in thermal performance between the two modes of condensation.  



## Overview  

This project supports experiments focused on:  
- **Film-wise condensation**: Characterized by a continuous liquid film over the surface, reducing heat transfer efficiency.  
- **Drop-wise condensation**: Involves discrete droplet formation, significantly enhancing heat transfer rates.  

The analysis includes:  
1. Heat transfer rate $Q$.  
2. Heat flux $q$.  
3. Adjusted surface temperatures $T_{\text{adjusted}}$.  
4. Heat transfer coefficients $h$.  



## Script Features  

### 1. Heat Transfer Rate  
The heat transfer rate is calculated as:  

$$  
Q = \dot{m} \cdot c_p \cdot (T_{\text{out}} - T_{\text{in}})  
$$  

Where:  
- $\dot{m}$ is the mass flow rate (kg/s).  
- $c_p$ is the specific heat capacity of water ($4.18 \, \text{kJ/kg°C}$).  
- $T_{\text{out}}, T_{\text{in}}$ are the cooling water outlet and inlet temperatures.  

---

### 2. Heat Flux  
The heat flux is computed using:  

$$  
q = \frac{Q}{A}  
$$  

Where:  
- $A = \pi \cdot d \cdot L$ is the surface area of the condenser (m²).  

---

### 3. Adjusted Surface Temperature  
The adjusted surface temperature is given by:  

$$  
T_{\text{adjusted}} = q \cdot \frac{x}{k} + T_{\text{initial}}  
$$  

Where:  
- $\frac{x}{k}$ is the thermal conductivity factor ($2 \times 10^{-6} \, \text{m.K/W}$).  

---

### 4. Heat Transfer Coefficient  
The heat transfer coefficient is calculated as:  

$$  
h = \frac{q}{T_{\text{sat}} - T_{\text{adjusted}}}  
$$  

Where:  
- $T_{\text{sat}}$ is the saturation temperature ($80^\circ\text{C}$).  

---

### 5. Data Integrity Check  
The script ensures that all input lists are of equal length and automatically adjusts mismatched lengths with placeholders to maintain consistent data.  

---

### 6. Automated Thermal Analysis  
The script computes $Q$, $q$, $T_{\text{adjusted}}$, and $h$ for both film-wise and drop-wise condensation modes.  

---

### 7. Excel Output  
The results are saved as an Excel file in the **Downloads folder**, containing all raw and computed data for easy use in lab reports.  

---

## Output Example  
The output Excel sheet contains:  
- **Experimental data columns**: $P_{\text{gage}}, T_1, T_3, T_4, T_6, T_7, \dot{m}_d, \dot{m}_f$.  
- **Computed columns**: $Q, q, T_{\text{adjusted}}, h$ for both modes of condensation.  

---

Feel free to contribute to the project by opening an issue or submitting a pull request!  

---  

