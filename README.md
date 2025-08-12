# Ad Spend Optimization using Lasso Regression

This project demonstrates how to use **Lasso Regression** to predict business revenue based on advertising spend across multiple channels (TV, Radio, Social Media). The final app is built and deployed using **Gradio** with a clean UI.

---

## Model Info

- **Algorithm**: Lasso Regression  
- **Use Case**: Ad Spend Optimization / Marketing ROI  
- **Input Features**:
  - TV Ad Spend
  - Radio Ad Spend
  - Social Media Spend
- **Target Variable**: Revenue (in dollars)

---
## Tech Stack

| Technology     | Use                  |
|----------------|----------------------|
| Python         | Core language        |
| scikit-learn   | Machine Learning     |
| Pandas         | Data manipulation    |
| NumPy          | Numeric operations   |
| Gradio         | Web-based UI         |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF6B81?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---
## Project Structure

```
ad_spend_optimization_lasso/
├── ad_spend_dataset.csv 
├── train_model.py 
├── lasso_model.pkl 
├── scaler.pkl
└── app_gradio.py 
```

---

## Installation

### 1. Install Dependencies
```bash
pip install flask scikit-learn pandas gradio
```

### 2. Train the Model (if not already)
```bash
python model.py
```

### 3. Run the Gradio App
```bash
python app.py
```

Then visit: [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## Sample UI

**Input**:

<img width="1332" height="311" alt="image" src="https://github.com/user-attachments/assets/3dad15c1-13c1-49a8-aadb-acf4400788e1" />

**Output**:

<img width="1291" height="321" alt="image" src="https://github.com/user-attachments/assets/146c33d1-0af1-4f81-aefd-537af3450a7c" />

---
