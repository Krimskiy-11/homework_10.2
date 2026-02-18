import json
import logging
import os

HIGH_PATH = os.path.dirname(os.path.dirname(__file__))  # C:\projects\Project_Homework10.2
PATH_DATA = os.path.join(HIGH_PATH, "data")  # C:\projects\Project_Homework10.2\data
PATH_LOGS = os.path.join(HIGH_PATH, "logs")  # C:\projects\Project_Homework10.2\logs

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    filename=os.path.join(PATH_LOGS, "utils.log"),
    filemode="w",
)

logger = logging.getLogger("utils")


def get_transactions(json_file: str):

    try:
        path = os.path.join(PATH_DATA, json_file)
        with open(path, encoding="utf-8") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                logger.error("Incorrect data entry")
                return []
            except ValueError:
                logger.error("Incorrect data entry")
                return []
            else:
                logger.info("The recording was completed successfully")
                return transactions
    except FileNotFoundError:
        logger.error("File not found")
        return []
