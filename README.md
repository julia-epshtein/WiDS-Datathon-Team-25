# WiDS-Datathon-Team-25

Building a model to predict both an individual's SEX and ADHD diagnosis.

- **Google Drive Folder**: Access additional resources, datasets, and presentations here: [WiDS-Datathon-Team-25 Google Drive](https://drive.google.com/drive/folders/1W7KNNP1_fpOVefiQH_p3e22zfxKHuViE?usp=share_link).
- **Notion Project Page**: Explore the project roadmap, task breakdowns, and collaboration notes here: [WiDS-Datathon-Team-25 Notion Page](https://www.notion.so/18666b317378800b812fc289bab2f8f5?v=18666b317378805b97d5000c513e1ec0&pvs=4).

### **👥 Team Members**

| Name | GitHub Handle | Contribution |
| ----- | ----- | ----- |
| Shachi Benara | @benaras | Led feature engineering efforts and implemented scatterplot, contributing to model development and data preprocessing. |
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

Our Team, MIT Team 25, has been working on the Women in Data Science (WiDS)  2025 Datathon. The datathon is an international data science competition aimed at increasing participation and skill development among women in data science. This year’s challenge and project focuses on building a predictive model that can determine both an individual’s SEX and ADHD diagnosis based on provided data. This project aims to shed light on the gaps in ADHD diagnosis for genders. 

ADHD is a widely studied neurodevelopmental disorder, yet its diagnosis remains challenging, especially in females. Historically, ADHD research and diagnostic criteria have been largely based on male-centric studies and data, leading to incorrect and under diagnostics in women and girls. Symptoms in females often present differently, manifesting as inattentiveness, causing many cases to go undetected and undiagnosed. 

This project aims to:
* Develop a machine learning capable of accurately predicting an individual sex and ADHD diagnosis based on available features. 
* Investigate and analyze the relationships between various demographic, behavioral, and medical factors to gain insights into ADHD diagnosis patterns. 
* Develop insight into the ADHD diagnosis gender gap.

This project is designated for a wide variety of audiences, primarily data scientists, machine learning engineers, students, and participants in the WiDS datathon. Additionally, this project is intended for all participants of the Break Through Tech program, who are hosting us in this datathon. 

---

## 📊 Data Exploration

### Dataset Components
The WiDS Datathon 2025 dataset consists of three main file types for both training (1200+ subjects) and test (300+ subjects) sets:

1. **Categorical Metadata**:
  - Demographics: sex, age (5-22 years), race, ethnicity
  - MRI information: scan location, participant age during scan
  - Social status: Barratt Simplified Measure of Social Status
  - Parent education and occupation information

2. **Functional MRI Connectome Matrices (fMRI)**:
  - Square symmetrical matrices (100×100) representing brain connectivity
  - Each cell indicates correlation between paired brain regions
  - Positive correlations show regions active together
  - Negative correlations show inversely active regions

3. **Quantitative Metadata**:
  - Parenting questionnaires: Alabama Parenting Questionnaire
  - Emotional assessments: Strengths and Difficulties Questionnaire
  - Behavioral measures: problems, hyperactivity, prosocial behavior

### Key Insights from EDA
Our exploratory analysis revealed several patterns:

- ADHD is most common among White/Caucasian participants in the dataset
- Males are overrepresented (70/30 split), with increasing male enrollment from 2015-2019
- Higher ADHD prevalence correlates with:
 - Increased behavioral difficulties scores
 - Higher emotional problem scores
 - Lower prosocial behavior scores
- Sex differences appear in:
 - Color vision scores (males showing more scattered outliers)
 - Conduct problems (males showing higher median scores)
 - Prosocial behavior (females showing higher scores)

### Preprocessing Challenges
- Extremely high dimensionality (~20,000 columns) requiring complex dimension reduction
- Handling the complex fMRI connectome matrices required specialized approaches
- Class imbalance between males and females required careful model evaluation
- Missing values in questionnaire responses needed appropriate imputation strategies

![Data Visualization showing ADHD distribution and feature correlations](https://github.com/user-attachments/assets/d14b43a2-d5a9-4491-add7-4e806fe9fe05)  
*Figure 1: Data Visualization showing ADHD distribution against categorical features*
![da30cda9-1ea4-4a14-a43e-ee070d37a8a4](https://github.com/user-attachments/assets/b4748c35-78e5-48dc-84f3-8db458681202)
*Figure 2: Data Visualization showing ADHD distribution against numerical features*

---

## 🧠 Model Development

### Model Architecture
We implemented several model approaches:
- **Primary Model**: XGBoost classifier for both ADHD and sex prediction
- **Preprocessing Pipeline**: Multiple preprocessing strategies tested including:
 - StandardScaler and MinMaxScaler for feature normalization
 - PCA for dimensionality reduction (found 1,007 components needed for 90% variance)
 - Custom feature engineering based on domain knowledge

### Feature Engineering
We created several engineered features:
- Professional status indicators from parent occupation
- Similarity measures between parent occupations
- Minority status indicators
- ADHD risk scores based on behavioral measures
- Interaction terms between parent education and occupation
- Clustered questionnaire features to capture latent patterns

### Training Approach
- 80/20 train/validation split for model development
- Balanced accuracy and F1-score used as primary evaluation metrics
- Baseline model established using logistic regression with minimal preprocessing
- Grid search attempted for hyperparameter optimization (limited by computational resources)
- Left Join + MinMax Scaler + XGBoost + PCA showed the best performance

(ADD image here) --> ![Model architecture and performance comparison](https://i.imgur.com/placeholder_image2.jpg)

---

## 📈 Results & Key Findings

### Performance Metrics
- **F1-score**: 0.75447
- **Kaggle Leaderboard Rank**: 111/543
- **ADHD Classification**: Higher accuracy than sex prediction

### Key Performance Insights
- Our model showed stronger predictive ability for ADHD than for sex classification
- Behavioral and emotional measures were more predictive than demographic features
- Feature importance analysis revealed that hyperactivity scores, conduct problems, and externalizing behavior were top predictors for ADHD
- Connectome data showed promising patterns but required complex processing to extract meaningful features

### Model Limitations
- Performance discrepancy between ADHD and sex prediction tasks
- Computational constraints limited full optimization potential
- Challenges interpreting the neurobiological significance of identified patterns

(ADD image here) --> ![Performance visualization and confusion matrix](https://i.imgur.com/placeholder_image3.jpg)

---

## 🖼️ Impact Narrative

### Brain Activity Patterns Associated with ADHD
Our analysis suggests that ADHD manifests in distinct brain connectivity patterns:

1. **Connectivity Differences**: 
  - ADHD subjects show altered connectivity in regions associated with attention regulation and impulse control
  - These patterns appear to differ between males and females, with males showing more pronounced connectivity alterations

2. **Sex-Based Differences**:
  - Males with ADHD demonstrate stronger hyperactivity indicators in both behavior measures and neural connectivity
  - Females with ADHD show more subtle patterns, potentially explaining underdiagnosis in female populations
  - The connectivity differences align with behavioral observations showing males with higher externalizing behaviors

3. **Demographic Interactions**:
  - Social and environmental factors (captured in parenting and social status measures) appear to interact with connectivity patterns
  - These interactions differ between sexes, suggesting different environmental vulnerability patterns

### Contribution to ADHD Research and Clinical Care
Our work contributes to ADHD research and clinical care by:

1. **Biomarker Development**:
  - Identifying potential neural biomarkers that could aid diagnosis
  - Highlighting sex-specific patterns that may improve diagnosis in underrepresented groups

2. **Clinical Applications**:
  - Suggesting objective measures that could supplement current diagnostic approaches
  - Providing quantitative connectivity patterns that could be monitored during treatment

3. **Research Directions**:
  - Creating a foundation for more detailed studies of sex-specific ADHD manifestations
  - Demonstrating the value of combining behavioral, demographic, and neuroimaging data

(ADD image here) --> ![Brain connectivity patterns associated with ADHD](https://i.imgur.com/placeholder_image4.jpg)

---
## **🚀 Next Steps & Future Improvements**

**Current Model Limitations**
- Our XGBoost model struggles with sex classification despite reasonable ADHD prediction accuracy
- Feature dimensionality challenges with nearly 20,000 columns requiring 1,007 principal components to capture 90% variance
- Limited ability to effectively process and extract meaningful patterns from complex fMRI connectome matrices
- Computational constraints when attempting full hyperparameter optimization with GridSearch

**With More Time/Resources We Would**
- Implement Graph Neural Networks specifically designed for brain connectivity data
- Compare PCA with UMAP for more effective non-linear dimensionality reduction
- Optimize classification thresholds through extensive cross-validation
- Apply deep learning approaches that can better capture the spatial relationships in brain connectivity
- Explore ensemble methods combining predictions from multiple model architectures

**Additional Datasets & Techniques**
- Incorporate longitudinal data to track ADHD manifestation changes over time
- Explore additional neuroimaging modalities beyond functional connectivity (structural MRI, DTI)
- Apply graph-theoretical measures to quantify brain network properties
- Investigate transfer learning from other neuroimaging studies
- Implement automated machine learning (AutoML) for more efficient hyperparameter tuning

---

## **📄 References & Additional Resources**

**1. Building an image classification model with Tensorflow vs. Pytorch:**

https://www.youtube.com/watch?v=ay1E1f8VqP8&list=WL&index=1&t=372s

Notebook From The Video: https://colab.research.google.com/drive/1UhZMd2u-hQjI-YmIojmZtEDA_jI-VWgo?usp=sharing

**2. Statistical Approaches on Vectorized Connectomes for Brain-Behavior Mapping**

https://www.youtube.com/watch?v=jbIsfVxuMWM&list=PLHAk3jHXWpxIqDNkF5olNdgCtYCecedsy&index=10

**3. Graph Neural Networks to Process Brain Connectomes**

https://www.youtube.com/watch?v=OkE3776GfWU&list=PLHAk3jHXWpxIqDNkF5olNdgCtYCecedsy&index=7 

---
