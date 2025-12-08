import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):

        # 🔥 ADD THESE 3 LINES HERE
        #os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/Codewtithdips/end-to-end-ml-pipeline.mlflow"
        #os.environ["MLFLOW_TRACKING_USERNAME"] = "Codewtithdips"
        #os.environ["MLFLOW_TRACKING_PASSWORD"] = "1f2ce87caa99243e1f28b650b8e95967bc9a5048"

        # Load test data + model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=self.config.metric_file_name, data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # Save model as artifact (no registry!)
            joblib.dump(model, "model.joblib")
            mlflow.log_artifact("model.joblib", artifact_path="model")
