# EIS Simulation and Battery Testing

## Project Overview

This project focuses on the simulation of Electrochemical Impedance Spectroscopy (EIS) models and their validation through experimental data using the AD5941 hardware. EIS is a crucial technique for understanding battery behavior, especially for assessing the state of health and predicting performance.

### Motivation

The project was created to bridge the gap between theoretical EIS models and real-world data. By using the AD5941 for validation, the project ensures that the simulations are both accurate and practical for real-world battery testing.

### Problem the Project Solves

- **Battery Health Monitoring**: The EIS simulations help to analyze the internal impedance of batteries, which is a key indicator of their health and remaining lifespan.
- **Model Validation**: The project validates different EIS theoretical models with actual data from battery tests, providing insights into how well the models perform in real-life applications.

---

## Technologies Used

- **Python**: The simulation scripts are written in Python, leveraging libraries like NumPy and Matplotlib for data analysis and visualization.
- **AD5941**: This hardware is used for capturing real-world battery impedance data.
- **Jupyter Notebook**: The `EIS_Simulation_(2).ipynb` file contains interactive simulations of various EIS models.

---

## Key Features

1. **EIS Model Simulation**:
   - Simulates various EIS theoretical models, allowing users to explore impedance characteristics.
   - Offers the ability to tweak model parameters and visualize the effect on impedance curves.
   
2. **Experimental Validation**:
   - The project includes real-world battery data, collected using the AD5941, to validate the simulated models.
   - The report (`Final_YP_EIS_report.pdf`) provides a detailed comparison between the simulated and experimental results.

---

## How to Get Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/eis-simulation-project.git
