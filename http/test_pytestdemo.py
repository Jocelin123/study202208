import pytest


def f():
    raise SystemExit("haha")
def test_mytest():
    with pytest.raises(IOError):
        f()