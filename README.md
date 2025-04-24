# Calpred • Calorie‑Burn Prediction Web App

Predict calories burned for every workout, log exercise sessions, and explore your fitness data on an interactive dashboard — all powered by Python + Flask, SQLite, and a machine‑learning model.

---

## ✨  Key Features
| Module | Highlights |
|--------|------------|
| **Calorie Predictor** | • XGBoost regression model (`final_model.pkl`) trained on gender, age, height, duration, heart‑rate, body‑temperature.<br>• Instant prediction on the home page or via API. |
| **User Auth** | • Register / log in with SQLite credentials.<br>• Sessions handled with Flask’s `session` object. |
| **Exercise Logger** | • After each prediction the workout is auto‑stored: exercise name, duration, date, BPM, temperature, calories. |
| **Analytics Dashboard** | • Bar: total calories per exercise<br>• Line: calories over time<br>• Pie: exercise share vs. calories<br>• Scatter: heart‑rate vs. calories<br>• Heat‑map: feature correlation<br>• Bonus charts: violin, temp vs exercise, heart‑rate timeline & pie. |
| **Secure & Portable** | • Single‑file Flask backend.<br>• No external DB server — just `Calorie.db`.<br>• Secret key stored in app config for session protection. |

---
## ⚙️  Setup & Run Locally

```bash
# 1  Clone repo & enter folder
git clone https://github.com/your‑org/ignifit.git
cd ignifit

# 2  Create virtual env
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3  Install deps
pip install -r requirements.txt
# (Flask, pandas, plotly, xgboost, etc.)
```

###Screenshots

![image](https://github.com/user-attachments/assets/bfebb314-2d46-43b1-bace-332282a40c9f)


![image](https://github.com/user-attachments/assets/117d67eb-6209-4995-a6ae-1b9ec03273a3)

