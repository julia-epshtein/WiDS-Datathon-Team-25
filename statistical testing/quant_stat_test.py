from scipy.stats import chi2_contingency
import pandas as pd

#edit paths as needed: i am not very good with OS, i prefer to just hard code the paths so replace it with the actual path to the data OR help me fix hehe
train_quant = pd.read_excel('C:/Users/linds/OneDrive/Desktop/WIDS/WiDS-Datathon-Team-25/data/raw/TRAIN/TRAIN_QUANTITATIVE_METADATA.xlsx')
train_sex = pd.read_excel('C:/Users/linds/OneDrive/Desktop/WIDS/WiDS-Datathon-Team-25/data/raw/TRAIN/TRAINING_SOLUTIONS.xlsx')
combined_df = pd.merge(train_quant, train_sex, on='participant_id')
# print(combined_df.head())


#CHI SQUARE TEST OF ADHD_OUTCOME AND EVERY VARIABLE, PRINTING CHI SQ AND P VALUE

# List of numerical columns (excluding participant_id & ADHD_Outcome)
num_columns = [col for col in combined_df.columns if col not in ['participant_id', 'ADHD_Outcome']]
print("Chi-Square test of numerical variables and adhd outcome")
# Loop through numerica; variables and run Chi-Square test
significant_num = {}
for col in num_columns:
    contingency_table = pd.crosstab(combined_df[col], combined_df['ADHD_Outcome'])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    print(f"{col}: Chi-Square = {chi2:.3f}, p-value = {p:.5f}")
    if p < 0.05:
        significant_num[col] = p
print("-----------------------")
print("Significant Numerical Features with ADHD Outcome (p < 0.05):")
for col, p in significant_num.items():
    print(f"{col}: p-value = {p:.5f}")


'''
repeat the process but use gender instead of adhd_outcome 
'''
# List of  numerical columns (excluding participant_id & Sex_F)
num_columns = [col for col in combined_df.columns if combined_df[col].nunique() < 10 and col not in ['participant_id', 'Sex_F']]
print("Chi-Square test of demographic variables and sex")
# Loop through categorical variables and run Chi-Square test
significant_num2 = {}
for col in num_columns:
    contingency_table = pd.crosstab(combined_df[col], combined_df['Sex_F'])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    print(f"{col}: Chi-Square = {chi2:.3f}, p-value = {p:.5f}")
    if p < 0.05:
        significant_num2[col] = p
print("-----------------------")
print("Significant Numerical Features with Sex (p < 0.05):")
for col, p in significant_num2.items():
    print(f"{col}: p-value = {p:.5f}")