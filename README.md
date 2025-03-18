# 🚀 Propeller Aerodynamics Predictor

This project predicts the **Thrust Coefficient (CT)** and **Hover Figure of Merit (FM)** for a propeller using **machine learning models**. The **Streamlit** web application provides an interactive interface where users can adjust propeller parameters and receive real-time predictions.

---

## 📌 Features  
- ✅ Interactive **UI with sliders** for input parameters  
- ✅ **Real-time predictions** without needing a submit button  
- ✅ **Error handling** for model loading and predictions  
- ✅ **Live visualizations** for CT and FM values  

---

## 🛠️ Setup & Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/Propeller_Aerodynamics.git
cd Propeller_Aerodynamics
```

### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application  
```bash
streamlit run app.py
```

---

## 📂 Project Structure  
```
Propeller_Aerodynamics/
│── model_ct.pkl              # Pre-trained ML model for Thrust Coefficient
│── model_fm.pkl              # Pre-trained ML model for Figure of Merit
│── model_building.ipynb      # Jupyter Notebook for model training
│── app.py                    # Streamlit application
│── requirements.txt          # Required Python libraries
│── README.md                 # Project documentation
```

---

## 🧠 How It Works  

- Users input **propeller parameters** (Blade count, Diameter, Pitch, RPM, etc.).
- The trained ML models predict **CT** and **FM** based on inputs.
- **Results update instantly**, displaying values and a **bar chart** visualization.

---

## 📌 Model Training  

The machine learning models were trained using **Scikit-Learn**. Check the **model_building.ipynb** file for details on:  
- ✔ **Dataset preprocessing**  
- ✔ **Feature engineering**  
- ✔ **Model training & evaluation**  

---

## 📢 Contributing  
Want to improve this project? Feel free to fork the repo, make changes, and submit a **pull request!** 🚀  

---

## 📜 License  
This project is **open-source** under the MIT License.  
