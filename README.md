# Drug Discovery using Regression Models on SMILES
---------------------------------------------------------------------
### About:
This project leverages **machine learning**, specifically regression models, to streamline the process of drug discovery. By training machine learning models on the SMILES (`Simplified Molecular Input Line Entry System`) representations of molecules, we aim to predict key molecular properties such as lipophilicity (`AlogP`) and ligand interaction metrics (`BEI`, `LLE`, `LE`, `SEI`) using the Circular Fingerprint.

Using ML, this approach helps **reduce** the high cost, time, and complexity associated with traditional drug development, thus making the process faster and more efficient compared to the latter approach.

---------------------------------------------------------------------
### Machine Learning Models Used:
1. AdaBoost Regressor
2. Decision Tree
3. Gradient Boosting
4. Huber Regressor
5. KNN Regressor
6. Random Forest
7. SVM Regressor
8. XGBoost Regressor
----------------------------------------------------------------------
### Repository Structure:
```
├── Frontend/              # Streamlit web interface
├── Train_Model/           # .pkl files of trained ML models
├── Train_Notebook/        # Jupyter notebooks containing the trained ML models
├── scripts/               # Automation scripts
├── evaluate_model.py      # Script to evaluate trained regression models
├── requirements.py        # Required dependencies list
├── README.md              # Repository documentation
```
------------------------------------------------------------------------
### Getting Started:
**Prerequisites**:
All required dependencies are mentioned in `requirements.txt`. Use the command:
```
pip install -r requirements.txt
```

**Running the project**:
This project includes several shell scripts for automating tasks:

- `run.sh`: Automates copying trained models to the frontend and launches the Streamlit app.
- `file_management.sh`: Organizes output and removes unnecessary files.

To run any of the scripts, use the following commands:

```
chmod +x scripts/train_model.sh
./scripts/train_model.sh 
```
-------------------------------------------------------------------------
### Features of the project:
1. Parses `SMILES` string which contains molecular information.
2. Predicts molecular properties such as `AlogP`, `BEI`, `LLE`, `LE`, and `SEI` using `Circular Fingerprint`.
3. Trains multiple regression models.
4. Evaluation with metrics such as `MSE`, `MAE` and `R2-Score`.
5. Scripted automation for training and evaluation.
--------------------------------------------------------------------------
### Author and Contributors:
- [Lakshay Sharma](https://github.com/lakshay-sharma-2024)
- [Manan Tandel](https://github.com/manan3044)
- [Deven Dhake](https://github.com/Devendhake18)
- [Madhusudan Hasbe](https://github.com/madhusudanhasbe)
