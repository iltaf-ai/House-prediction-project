# House Price Prediction

A machine learning web application that predicts house prices based on property features. Built with **Scikit-learn** for the prediction model, **FastAPI** for the backend API, and a simple UI for user interaction.

## 🚀 Features

- Predicts house prices using a trained regression model
- REST API built with FastAPI
- User authentication (signup/login with JWT)
- Simple web UI to input property details and get predictions
- Clean, documented API endpoints (interactive docs via Swagger UI)

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Database:** SQLAlchemy + PostgreSQL (or SQLite for local dev)
- **Authentication:** JWT (python-jose), Passlib (bcrypt)
- **Frontend:** HTML/CSS/JavaScript (or specify your framework)

## 📁 Project Structure

```
house-prediction-project/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── database.py       # DB connection & session
│   ├── model.py          # SQLAlchemy models
│   ├── schema.py          # Pydantic schemas
│   ├── dependencies.py    # Auth & helper functions
│   ├── routers/
│   │   ├── auth.py        # Signup/login endpoints
│   │   └── prediction.py  # Prediction endpoints
│   └── config.py          # Environment settings
├── ml_model/
│   ├── train_model.py     # Model training script
│   └── house_price_model.pkl  # Trained model file
├── static/                 # UI files (HTML/CSS/JS)
├── requirements.txt
├── .env.example
└── README.md
```

## ⚙️ Installation

1. **Clone the repository**
```bash
   git clone https://github.com/your-username/house-prediction-project.git
   cd house-prediction-project
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
   cp .env.example .env
   # Fill in your DATABASE_URL, SECRET_KEY, ALGORITHM, TOKEN_TIME_EXPIRE
```

5. **Run the application**
```bash
   uvicorn app.main:app --reload
```

6. Visit `http://127.0.0.1:8000/docs` for the interactive API documentation.

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `DATABASE` | Database connection URL |
| `SECRET_KEY` | Secret key for JWT encoding |
| `ALGORITHM` | JWT algorithm (e.g., HS256) |
| `TIME_TOKEN_EXPIRE` | Token expiry time in minutes |

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Create a new user account |
| POST | `/login` | Login and receive access token |
| POST | `/predict` | Submit property details and get a price prediction |
| GET | `/predictions` | Get all predictions for the logged-in user |

## 🧠 Model Details

- **Algorithm:** Linear Regression (Scikit-learn)
- **Features used:** Square Footage, Bedrooms, Bathrooms, Year Built, Lot Size, Garage Size, Neighborhood Quality
- **Preprocessing:** StandardScaler for feature scaling

## 📸 Screenshots

*(Add screenshots of your UI here)*

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/your-username/house-prediction-project/issues).

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Iltaf Hussain**
Python Developer | FastAPI Developer
[Portfolio](https://portfolio-iltaf.vercel.app)