import os
import sys
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        param = {
            "Random Forest": {
                "n_estimators": [50, 100],
                "max_depth": [None, 10, 20]
            },
            "Decision Tree": {
                "max_depth": [5, 10, 20]
            },
            "Gradient Boosting": {
                "learning_rate": [0.01, 0.1],
                "n_estimators": [50, 100]
            },
            "Linear Regression": {},
            "KNN Regressor": {
                "n_neighbors": [3, 5, 7]
            },
            "XGB Regressor": {
                "n_estimators": [50, 100],
                "learning_rate": [0.01, 0.1]
            },
            "CatBoost Regressor": {},
            "AdaBoost Regressor": {
                "n_estimators": [50, 100],
                "learning_rate": [0.01, 0.1]
            }
        }
        for model_name, model in models.items():
            para = param[model_name]
            if para:
                gs = GridSearchCV(model, para, cv=3, n_jobs=-1, verbose=0)
                gs.fit(X_train, y_train)
                model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_score
        return report
    except Exception as e:
        raise CustomException(e, sys)