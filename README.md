# End to End Data Science Project

### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py

Entire Workflow executed through
```sh
main.py


Project Structure 

.
├── app.py
├── main.py
├── config/
│   ├── config.yaml
│   ├── params.yaml
│   └── schema.yaml
├── artifacts/
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
├── src/
│   └── datascience/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
├── templates/
│   ├── index.html
│   └── results.html
└── requirements.txt

Architecture Diagram

        ┌────────────────────┐
        │   Data Ingestion   │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │   Data Validation   │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │ Data Transformation │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │   Model Training    │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │  Model Evaluation   │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │      Prediction     │
        └─────────────────────┘

main.py  
│
├── Data Ingestion Pipeline
├── Data Validation Pipeline
├── Data Transformation Pipeline
├── Model Trainer Pipeline
└── Model Evaluation Pipeline


Install Requirements 

main.py  
│
├── Data Ingestion Pipeline
├── Data Validation Pipeline
├── Data Transformation Pipeline
├── Model Trainer Pipeline
└── Model Evaluation Pipeline



Run Full ML Pipeline

python main.py


Run Flask Web App

python app.py


This App Runs At 

http://localhost:8080

Pipeline Stages Explained

Data Ingestion

Data Stored in ----- artifacts/data_ingestion/

Data Validation 

Checks if CSV columns match expected schema 
Writes results too : artifacts/data_validation/status.txt


Data Transformation

Performs train test split Saves :
Train.csv 
Test.csv

Model trainer
Saved Trained Model at : artifacts/model_trainer/model.joblib

Model Evaluation
SAVES JSON FILE AT ---- artifacts/model_evaluation/metrics.json


Flask Web Application:


/train --- Run the entire ML pipeline

/predict --- Takes user input ----> return predicted win quality

Templates located 

/templates/index.html
/templates/results.html

```








