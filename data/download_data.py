import openml
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import os
openml.config.cache_directory = os.path.expanduser(os.getcwd() + "/openml_cache")

def save_suite(suite_id, dir_name, save_categorical_indicator=False, regression=True):
    benchmark_suite = openml.study.get_suite(suite_id)
    # [DEV] Iterate over only two tasks. Just enough to preview the dataset columns and categories.
    for task_id in benchmark_suite.tasks[:1]:
        task = openml.tasks.get_task(task_id)
        dataset = task.get_dataset()
        print(f"Downloading dataset {dataset.name}")

        X, y, categorical_indicator, _attribute_names = dataset.get_data(
            dataset_format="dataframe", target=dataset.default_target_attribute
        )

        print(f"Type of `X`: {type(X)}")
        print(f"Sample of `X`: {X.iloc[0]}")
        print(f"Type of `y`: {type(y)}")
        print(f"Sample of `y`: {y[0]}")
        print(f"Type of `categorical_indicator`: {type(categorical_indicator)}")
        print(f"Sample `categorical_indicator`: {categorical_indicator[0]}")

        # At this point, `X` and `y` are `pandas.DataFrame`s.
        # `categorical_indicator` is a `List[bool]`.
        # TODO: Store `X` and `y` into a Postgres database.
                
suites_id = {"numerical_regression": 297,
          "numerical_classification": 298,
          "categorical_regression": 299,
          "categorical_classification": 304}

# print("Saving datasets from suite: {}".format("numerical_regression"))
# save_suite(suites_id["numerical_regression"],
#            "data/numerical_only/regression",
#            save_categorical_indicator=False)

# print("Saving datasets from suite: {}".format("numerical_classification"))
# save_suite(suites_id["numerical_classification"],
#            "data/numerical_only/balanced",
#            save_categorical_indicator=False,
#            regression=False)

# print("Saving datasets from suite: {}".format("categorical_regression"))
# save_suite(suites_id["categorical_regression"],
#            "data/num_and_cat/regression",
#            save_categorical_indicator=True)

print("Saving datasets from suite: {}".format("categorical_classification"))
save_suite(suites_id["categorical_classification"],
           "data/num_and_cat/balanced",
           save_categorical_indicator=True,
           regression=False)