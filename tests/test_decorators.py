from typing import Any

import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> Any:
    """Функция деления для проверки декораторов"""
    return x / y


@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 0, "Error: ZeroDivisionError. Inputs: (1, 0), {}\n"),
        (1, "1", "Error: TypeError. Inputs: (1, '1'), " "{}\n"),
        ("1", "1", "Error: TypeError. Inputs: ('1', " "'1'), {}\n"),
        (1, None, "Error: TypeError. Inputs: (1, " "None), {}\n")
    ],
)
def test_log_negative(capsys, a, b, result):
    my_function(a, b)
    captured = capsys.readouterr()
    assert captured.out == result


@pytest.mark.parametrize(
    "a, b, result",
    [
        (10, 2, "my_function ok\n"),
        (1, 1, "my_function ok\n"),
        (200, 300, "my_function ok\n"),
        (132415, 0, "Error: ZeroDivisionError. Inputs: (132415, 0), {}")
    ]
)
def test_log_positive(a, b, result):
    with open("mylog.txt", "w") as file:
        file.write("")
    my_function(a, b)
    with open("mylog.txt", "r") as file:
        read_file = file.read()
    assert read_file == result
