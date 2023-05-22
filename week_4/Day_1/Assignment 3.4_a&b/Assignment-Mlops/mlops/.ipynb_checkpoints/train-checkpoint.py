import fire
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.pipeline import make_pipeline
# from sklearn.metrics import f1_score  
from sklearn.model_selection import train_test_split


def split_data(wine_data):
    
    wine_x = wine_data.iloc[:,:6]
    wine_y = wine_data['quality']
    x_train, x_test, y_train, y_test = train_test_split(wine_x, wine_y, test_size=0.2)

    return x_train, x_test, y_train, y_test


def setup_rfc_pipeline(max_depth):
    rfc_model = RandomForestClassifier(max_depth)
    rfc_pipe = make_pipeline(StandardScaler(), rfc_model)
    return rfc_pipe


def track_with_mlflow(model, X_test, Y_test, mlflow, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("accuracy", model.score(X_test, Y_test))
    mlflow.sklearn.log_model(model, "rfc", registered_model_name="sklearn_rfc")

def main(file_name: str, max_depth: int):

    wine_data = pd.read_csv(file_name)
    x_train, x_test, y_train, y_test = split_data(wine_data)

    with mlflow.start_run():
        rfc_pipe = setup_rfc_pipeline(max_depth)
        rfc_pipe.fit(x_train, y_train)
        model_metadata = {"max_depth":max_depth}
        track_with_mlflow(rfc_pipe,x_test,y_test,mlflow,model_metadata)


if __name__ == "__main__":
    fire.Fire(main)

