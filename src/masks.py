import logging
import os

HIGH_PATH = os.path.dirname(os.path.dirname(__file__))  # C:\projects\Project_Homework10.2
PATH_LOGS = os.path.join(HIGH_PATH, "logs")  # C:\projects\Project_Homework10.2\logs

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    filename=os.path.join(PATH_LOGS, "masks.log"),
    filemode="w",
)

logger = logging.getLogger("masks")


def get_mask_card_number(card_num: [str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    if card_num is None:
        logger.error("Incorrect data entry")
        return "Incorrect data entry"
    else:
        str_card_num = str(card_num)

        if str_card_num.__len__() != 16:
            logger.error("Incorrect data entry")
            return "Incorrect data entry"

        mask = str_card_num.replace(str_card_num[6:12], "******")

        space_card_num = ""
        for i in mask:
            space_card_num += i
            if len(space_card_num) == 4 or len(space_card_num) == 9 or len(space_card_num) == 14:
                space_card_num += " "

        logger.info("The disguise was successfully applied")
        return space_card_num


def get_mask_account(total_num: [str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""

    if total_num is None:
        logger.error("Incorrect data entry")
        return "Incorrect data entry"
    else:
        str_total_num = str(total_num)

        if str_total_num.__len__() != 20:
            logger.error("Incorrect data entry")
            return "Incorrect data entry"

        mask = str_total_num.replace(str_total_num[:-4], "**")

        logger.info("The disguise was successfully applied")
        return mask
