# WiDS-Datathon-Team-25

Building a model to predict both an individual's SEX and ADHD diagnosis.

## Project Organization

```
WiDS-Datathon-2025/
├── Makefile               <- The Makefile with convenience commands like `make data` or `make train`
├── README.md              <- The top-level README for developers using this project.
├── .env                   <- Environment configuration file (you may want to put secrets here)
├── .gitignore             <- The .gitignore file to exclude unwanted files/folders from version control
├── pyproject.toml         <- Configuration file for Python projects
├── requirements.txt       <- The requirements file for reproducing the analysis environment
├── setup.cfg              <- Configuration file for setuptools
│
├── data/
│   ├── raw/               <- Original data files
│   ├── processed/         <- Processed data
│   │   ├── regular/       <- Regular preprocessed data
│   │   │   ├── X_train.csv
│   │   │   ├── X_test.csv
│   │   │   ├── y_train.csv
│   │   ├── normalized/    <- Normalized data
│   │   │   ├── X_train.csv
│   │   │   ├── X_test.csv
│   │   ├── pca/           <- PCA transformed data
│   │   │   ├── X_train.csv
│   │   │   ├── X_test.csv
│   │   ├── pca_normalized/ <- PCA + Normalized data
│   │   │   ├── X_train.csv
│   │   │   ├── X_test.csv
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
