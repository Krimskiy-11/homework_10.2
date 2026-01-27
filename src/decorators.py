from functools import wraps
from time import time
from typing import Any


def log(filename: str) -> Any:
    def wrapper(function: Any):
        @wraps(function)
        def inner(*args: int, **kwargs: int):
            with open(filename, 'a', encoding='utf-8') as file:
                try:
                    time1 = time()
                    func_start = 'Function start'
                    result = function(*args, **kwargs)
                    func_stop = 'Function stop'
                    time2 = time()
                    log_message = (f"Start time: {time1}\n"
                                   f"{func_start}\n"
                                   f"Inputs: {args}, {kwargs}\n"
                                   f"Result: {result}\n"
                                   f"{func_stop}\n"
                                   f"End time: {time2}\n")
                    print(log_message)
                    file.write(f'{function.__name__} ok\n')
                    return result
                except Exception as e:
                    log_message_exception = f"Error: {e}. Inputs: {args}, {kwargs}"
                    print(log_message_exception)
                    file.write(log_message_exception)
        return inner
    return wrapper
