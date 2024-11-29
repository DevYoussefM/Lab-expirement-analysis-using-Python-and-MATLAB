Repository Summary
Airfoil Analysis
- Objective: Investigate the drag coefficient ($C_D$) and lift coefficient ($C_L$) of an airfoil at varying angles of attack (α) and Reynolds numbers (Re).
- Parameters:
  - Angles of Attack (α): 0°, 5°, 10°, 15°, and 20°.
  - Reynolds Numbers (Re): Varying across experiments.
- Modeling Approach: Smooth spline interpolation for $C_D$ and $C_L$ curves with logical constraints, ensuring $C_D$ = 0 and C_L = 0 at α = 0.
- Applications: Provides training data for AI models, benchmarks for computational fluid dynamics (CFD), and educational resources for aerodynamic studies.
Sphere Analysis
- Objective: Analyze the drag coefficient ($C_D$) of smooth and rough spheres across different Reynolds number regimes.
- Findings:
  - Smooth Sphere: Laminar flow dominates for Re < 3 × 10^5, transitioning to turbulence at higher Re.
  - Rough Sphere: Surface roughness induces earlier transition to turbulence, affecting $C_D$.
- Applications: Offers insights into flow characteristics for sports (e.g., golf balls) and industrial processes (e.g., fluidized beds). Data aids in AI modeling for flow prediction and validation of CFD simulations.
Repository Contents
1. Datasets:
   - Airfoil: Experimental results for varying α and Re, including zeroed-out values at α = 0.
   - Sphere: Drag coefficient data across laminar, transition, and turbulent flow regimes for smooth and rough spheres.
2. Scripts:
   - MATLAB: Curve fitting and visualization of $C_D$ and $C_L$ vs. α for airfoils.
   - Python: Data preprocessing and consistency checks.
3. Plots:
   - $C_D$ vs. α and C_L vs. α for airfoils at multiple Re.
   - $C_D$ vs. Re for smooth and rough spheres.
Applications
The repository serves as a resource for:
- Machine Learning: Training regression models to predict aerodynamic behavior.
- CFD Validation: Benchmarking against experimental and analytical results.
- Education: Illustrating aerodynamic principles and mathematical modeling.
Future Work
- Integrating AI models for predicting aerodynamic coefficients.
- Extending analysis to include fully turbulent airfoil flows.
- Developing generalized models for various sphere roughness conditions.
