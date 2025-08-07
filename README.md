# 📊 Ad Spend Optimization using Lasso Regression (Gradio App)

This project demonstrates how to use **Lasso Regression** to predict business revenue based on advertising spend across multiple channels (TV, Radio, Social Media). The final app is built and deployed using **Gradio** with a clean UI.

---

## 🚀 Model Info

- **Algorithm**: Lasso Regression  
- **Use Case**: Ad Spend Optimization / Marketing ROI  
- **Input Features**:
  - TV Ad Spend
  - Radio Ad Spend
  - Social Media Spend
- **Target Variable**: Revenue (in dollars)

---

## 📁 Project Structure



```
📁 ad_spend_optimization_lasso/
├── ad_spend_dataset.csv 
├── train_model.py 
├── lasso_model.pkl 
├── scaler.pkl
└── app_gradio.py 
```

---

## 🔧 Installation

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

Then visit: [http://127.0.0.1:7860]

---

## 🖥️ Sample UI

**Input**:

<img width="1332" height="311" alt="image" src="https://github.com/user-attachments/assets/3dad15c1-13c1-49a8-aadb-acf4400788e1" />

**Output**:

<img width="1291" height="321" alt="image" src="https://github.com/user-attachments/assets/146c33d1-0af1-4f81-aefd-537af3450a7c" />

---

## 🙋‍♂️ Author

**Hari Prasath **  
[GitHub Profile](https://github.com/hariprasath2105)

---

## 📘 License

This project is open source and free to use.
