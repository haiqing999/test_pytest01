import pytest
from pytestcode.cal import Calculater

@pytest.fixture()
def testcal():
    cal = Calculater()
    print("开始计算")
    yield cal
    print("结束计算")
