import json
import os


HIGH_PATH = os.path.dirname(os.path.dirname(__file__))  # C:\projects\Project_Homework10.2
PATH_DATA = os.path.join(HIGH_PATH, "data")  # C:\projects\Project_Homework10.2\data


def get_transactions(json_file: str):

    try:
        path = os.path.join(PATH_DATA, json_file)
        with open(path, encoding='utf-8') as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                return []
            except ValueError:
                return []
            else:
                return transactions
    except FileNotFoundError:
        return []
