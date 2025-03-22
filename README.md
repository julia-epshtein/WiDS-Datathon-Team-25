# WiDS-Datathon-Team-25

Building a model to predict both an individual's SEX and ADHD diagnosis.

- **Google Drive Folder**: Access additional resources, datasets, and presentations here: [WiDS-Datathon-Team-25 Google Drive](https://drive.google.com/drive/folders/1W7KNNP1_fpOVefiQH_p3e22zfxKHuViE?usp=share_link).
- **Notion Project Page**: Explore the project roadmap, task breakdowns, and collaboration notes here: [WiDS-Datathon-Team-25 Notion Page](https://www.notion.so/18666b317378800b812fc289bab2f8f5?v=18666b317378805b97d5000c513e1ec0&pvs=4).

### **👥 Team Members**

| Name | GitHub Handle | Contribution |
| ----- | ----- | ----- |
| Shachi Benara | @benaras | Led feature engineering efforts and implemented logistic regression, contributing to model development and data preprocessing. |
| Julia Epshtein | @julia-epshtein | Optimized XGBoost and created PCA-normalized dataframes to enhance model performance. |
| Mantra Burugu | @mantraburugu | Applied SMOTE for balancing ADHD and gender data, investigated FCM visualization, and documented code for clarity. |
| Lindsey Blau | @lindseyblau | Conducted feature selection by dropping low p-value columns, optimized XGB, and researched statistical feature relationships. |

---

## **🎯 Project Highlights**

* Built a machine learning model to predict both an individual's SEX and ADHD diagnosis.  
* Developed an **XGBoost and Logistic Regression model** using **feature engineering, SMOTE for balancing, and PCA for dimensionality reduction** to solve the **WiDS Datathon 2025 Kaggle competition task**.  
* Achieved an **F1 score of 0.75447** and a ranking of **111/543** on the final Kaggle Leaderboard.  
* Implemented **data normalization, feature selection, and balancing techniques** to optimize results within compute constraints.  

🔗 [WiDS Datathon 2025 | Kaggle Competition Page](https://www.kaggle.com/competitions/widsdatathon2025/overview)

---

## Project Organization

```
WiDS-Datathon-2025/
├── Makefile               <- The Makefile with convenience commands like `make data` or `make train`
├── README.md              <- The top-level README for developers using this project.
├── .gitignore             <- The .gitignore file to exclude unwanted files/folders from version control
├── pyproject.toml         <- Configuration file for Python projects
├── requirements.txt       <- The requirements file for reproducing the analysis environment
├── setup.cfg              <- Configuration file for setuptools
│
├── data/
│   ├── raw/               <- Original data files
│   │   │   ├── widsdatathon2025 <- Folder containing the raw dataset
│   │   │   │   ├── TEST    <- TEST dataset files
│   │   │   │   │   ├── TEST_CATEGORICAL.xlsx
│   │   │   │   │   ├── TEST_FUNCTIONAL_CONNECTOME_MATRICES.csv
│   │   │   │   │   ├── TEST_QUANTITATIVE_METADATA.xlsx
│   │   │   │   ├── TRAIN   <- TRAIN dataset files
│   │   │   │   │   ├── TRAIN_CATEGORICAL_METADATA.xlsx
│   │   │   │   │   ├── TRAIN_FUNCTIONAL_CONNECTOME_MATRICES.csv
│   │   │   │   │   ├── TRAIN_QUANTITATIVE_METADATA.xlsx
│   │   │   │   │   ├── TRAINING_SOLUTIONS.xlsx
│   │   │   │   ├── Data Dictionary.xlsx
│   │   │   │   ├── SAMPLE_SUBMISSION.xlsx
│   ├── preprocessed/       <- Processed data files
│   │   │   ├── test_data.csv
│   │   │   ├── train_data.csv
│   │   │   ├── train_data_scaled.csv
│   │   │   ├── train_data_pca.csv
│
├── notebooks/
│   ├── preprocessing/      <- Jupyter notebooks for preprocessing tasks
│   │   │   ├── je_preprocessing.ipynb
│   ├── visualizations/     <- Jupyter notebooks for creating visualizations
│   │   │   ├── je_pie_charts.ipynb
│
├── venv/                   <- Virtual environment for package management
```

## Setting Up the Virtual Environment

1. **Create a Virtual Environment:**

   First, create a virtual environment to isolate your project's dependencies.

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**

   - **For macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **For Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

   After activation, your terminal should indicate the virtual environment is active (e.g., `(venv)` before the prompt).

3. **Install Project Dependencies:**

   Once the virtual environment is active, install the dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Deactivate the Virtual Environment (optional):**

   When you're done working, you can deactivate the virtual environment:

   ```bash
   deactivate
   ```

## Getting the Data

Follow these steps to set up the dataset for the project:

1. **Create a data directory**  
   - In your project folder, create a new directory named `data`.

2. **Set up subdirectories**  
   - Inside the `data` directory, create two subdirectories:  
     - `raw` (for storing the original downloaded data)  
     - `preprocessed` (for storing the processed data)

3. **Download the dataset**  
   - Go to the competition page: [WiDS Datathon 2025 Data](https://www.kaggle.com/competitions/widsdatathon2025/data)  
   - Download all necessary files.

4. **Move the data**  
   - Place all downloaded files into the `data/raw` directory.

5. **Run preprocessing**  
   - Open and run `je_preprocessing.ipynb`.  
   - After running all cells, the preprocessed data will be saved in `data/preprocessed`.

# Additional Dependencies
Before installing Python dependencies, install `libomp` (required for XGBoost) using:

```bash
brew install libomp
brew link libomp
```

## **🏗️ Project Overview**

**Describe:**

Our Team, MIT Team 25, has been working on the Women in Data Science (WiDS)  2025 Datathon. The datathon is an international data science competition aimed at increasing participation and skill development among women in data science. This year’s challenge and project focuses on building a predictive model that can determine both an individual’s SEX and ADHD diagnosis based on provided data. This project aims to shed light on the gaps in ADHD diagnosis for genders. 

ADHD is a widely studied neurodevelopmental disorder, yet its diagnosis remains challenging, especially in females. Historically, ADHD research and diagnostic criteria have been largely based on male-centric studies and data, leading to incorrect and under diagnostics in women and girls. Symptoms in females often present differently, manifesting as inattentiveness, causing many cases to go undetected and undiagnosed. 

This project aims to:
* Develop a machine learning capable of accurately predicting an individual sex and ADHD diagnosis based on available features. 
* Investigate and analyze the relationships between various demographic, behavioral, and medical factors to gain insights into ADHD diagnosis patterns. 
* Develop insight into the ADHD diagnosis gender gap.

This project is designated for a wide variety of audiences, primarily data scientists, machine learning engineers, students, and participants in the WiDS datathon. Additionally, this project is intended for all participants of the Break Through Tech program, who are hosting us in this datathon. 

---

## **📊 Data Exploration**

**Describe:**

* The dataset(s) used (i.e., the data provided in Kaggle \+ any additional sources)
* Data exploration and preprocessing approaches
* Challenges and assumptions when working with the dataset(s)

**Potential visualizations to include:**

* Plots, charts, heatmaps, feature visualizations, sample dataset images

---

## **🧠 Model Development**

* Model(s) used (e.g., CNN with transfer learning, regression models)
* Feature selection and Hyperparameter tuning strategies
* Training setup (e.g., % of data for training/validation, evaluation metric, baseline performance)

---

## **📈 Results & Key Findings**

* F1-score: 0.75447
* Kaggle Leaderboard Rank: 111/543
* Model performance insights, fairness evaluation.

**Potential visualizations to include:**


---

## **🖼️ Impact Narrative**

1. What brain activity patterns are associated with ADHD; are they different between males and females, and, if so, how?
2. How could your work help contribute to ADHD research and/or clinical care?

---

## **🚀 Next Steps & Future Improvements**

* What are some of the limitations of your model?
* What would you do differently with more time/resources?
* What additional datasets or techniques would you explore?

---

## **📄 References & Additional Resources**

# 1. Building an image classification model with Tensorflow vs. Pytorch:

https://www.youtube.com/watch?v=ay1E1f8VqP8&list=WL&index=1&t=372s

# Notebook From The Video:

https://colab.research.google.com/drive/1UhZMd2u-hQjI-YmIojmZtEDA_jI-VWgo?usp=sharing

# 2. **Statistical Approaches on Vectorized Connectomes for Brain-Behavior Mapping**

https://www.youtube.com/watch?v=jbIsfVxuMWM&list=PLHAk3jHXWpxIqDNkF5olNdgCtYCecedsy&index=10

# 3. Graph Neural Networks to Process Brain Connectomes**

https://www.youtube.com/watch?v=OkE3776GfWU&list=PLHAk3jHXWpxIqDNkF5olNdgCtYCecedsy&index=7 

---
