from src.soma import soma


def test_soma():
    num1 = 4
    num2 = 7
    result = soma(num1=num1, num2=num2)
    assert result == 11
