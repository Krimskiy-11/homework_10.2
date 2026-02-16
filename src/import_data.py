import os

import pandas as pd

HIGH_PATH = os.path.dirname(os.path.dirname(__file__))  # C:\projects\Project_Homework10.2
PATH_DATA = os.path.join(HIGH_PATH, "data")  # C:\projects\Project_Homework10.2\data


def get_csv_data(file):
    """Функция для считывания финансовых операций из CSV-файла и
    выдает список словарей с транзакциями."""

    path_csv = os.path.join(PATH_DATA, file)  # ~\Project_Homework10.2\data\transactions.csv
    reading_file = pd.read_csv(path_csv, delimiter=";")
    return reading_file.to_json(orient="records", indent=4, force_ascii=False)


def get_excel_data(file):
    """Функция для считывания финансовых операций из Excel-файла и
    выдает список словарей с транзакциями."""

    path_xlsx = os.path.join(PATH_DATA, file)  # ~\Project_Homework10.2\data\transactions_excel.xlsx
    reading_file = pd.read_excel(path_xlsx)
    return reading_file.to_json(orient="records", indent=4, force_ascii=False)
