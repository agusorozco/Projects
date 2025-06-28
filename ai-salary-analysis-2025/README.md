# 🌍 Global AI/ML/Data Science Salaries — 2025 Analysis

This project analyzes global salary trends in AI, ML, and Data Science roles using a 2025 dataset from Kaggle. It includes exploratory data analysis, visualizations, and a simple predictive model for salary estimation.

---

## 📁 Project Structure

- `notebooks/`: Data cleaning, EDA, and modeling
- `data/`: Raw CSV file from Kaggle
- `sql/`: Future space for salary query exploration
- `tableau-dashboard/`: Dashboard assets (optional)
- `README.md`: This file

---

## 🔍 Key Questions Explored

- How do salaries differ by experience level?
- Do remote roles earn more or less?
- What are the highest-paying common job titles?
- Can we predict salary based on role, level, and company traits?

---

## 📊 Visual Highlights

- Bar plots comparing average salaries by:
  - Experience level
  - Remote ratio
  - Job title
- Choropleth (planned): Avg salary by country

---

## ⚙️ Model Summary

Built a regression model to predict salary based on:
- Experience Level
- Employment Type
- Remote Ratio
- Job Title
- Company Size

| Model | R² Score | MSE |
|-------|----------|-----|
| Linear Regression | 0.2381 | 420M |
| Random Forest     | 0.2321 | 424M |

---

## 🛠 Tools Used

- Python (pandas, seaborn, sklearn)
- Jupyter Notebook
- Matplotlib
- Git/GitHub

---

## 📌 Next Steps

- Add Tableau dashboard
- Clean job titles via clustering or NLP
- Try ensemble methods (XGBoost, LightGBM)