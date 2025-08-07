# app_gradio.py
import gradio as gr
import pickle
import numpy as np

# Load model and scaler
with open("lasso_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Prediction function
def predict_revenue(tv, radio, social):
    input_data = np.array([[tv, radio, social]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    return f"Estimated Revenue: ${prediction:,.2f}"

# Gradio interface
interface = gr.Interface(
    fn=predict_revenue,
    inputs=[
        gr.Slider(0, 300, label="TV Ad Spend ($1000s)"),
        gr.Slider(0, 100, label="Radio Ad Spend ($1000s)"),
        gr.Slider(0, 150, label="Social Media Spend ($1000s)")
    ],
    outputs=gr.Textbox(label="Predicted Revenue"),
    title="📊 Ad Spend Optimization with Lasso Regression",

)

interface.launch()
