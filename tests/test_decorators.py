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
        (1, 0, "Error: division by zero. Inputs: (1, 0), {}\n"),
        (1, "1", "Error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (1, '1'), " "{}\n"),
        ("1", "1", "Error: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('1', " "'1'), {}\n"),
        (1, None, "Error: unsupported operand type(s) for /: 'int' and 'NoneType'. Inputs: (1, " "None), {}\n"),
    ],
)
def test_log(capsys, a, b, result):
    my_function(a, b)
    captured = capsys.readouterr()
    assert captured.out == result

