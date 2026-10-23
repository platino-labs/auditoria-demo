from calculadora import restar, sumar


def test_sumar() -> None:
    assert sumar(2, 3) == 5


def test_restar() -> None:
    assert restar(5, 3) == 2
