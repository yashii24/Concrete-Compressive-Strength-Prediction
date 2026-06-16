📌 Problem Statement:

This project predicts the compressive strength of concrete based on its material composition and curing age using machine learning models.
It helps in civil engineering to estimate concrete strength before actual testing, saving time and cost.


📊 Dataset Information:
    Source: UCI Machine Learning Repository
    Total Samples: 1030
    Features: 8 input features
    Target: Concrete compressive strength (MPa)
    Features:
        Cement
        Blast Furnace Slag
        Fly Ash
        Water
        Superplasticizer
        Coarse Aggregate
        Fine Aggregate
        Age (days)

    
🔄 Machine Learning Workflow:
   1. Data Collection
   2. Data Preprocessing
   3. Exploratory Data Analysis (EDA)
   4. Feature Selection
   5. Train-Test Split
   6. Model Training
   7. Model Evaluation

   
🤖 Models Used:
   1. Linear Regression
      MAE: 7.74
      RMSE: 9.79
   2. Random Forest Regressor
      MAE: 3.75
      RMSE: 5.51

👉 Random Forest performed significantly better due to its ability to capture non-linear relationships.

📊 Feature Importance (Random Forest):
    Age → Most important factor
    Cement → Highly influential
    Water → Moderately affects strength
    Other aggregates → Lower impact

    
🧠 Key Insights:
    Age and Cement are the most important predictors of concrete strength
    Water content significantly affects strength due to water-cement ratio
    Non-linear models perform better than linear regression

    
🛠️ Tech Stack:
    Python
    Pandas
    NumPy
    Scikit-learn
    Matplotlib
    Seaborn
    Joblib
