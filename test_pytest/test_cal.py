"""
课后作业：
1、补全计算器（加减乘除）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、conftest.py中创建fixture 完成setup和teardown
4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""
import pytest
import yaml

class TestCal:

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("cal_data.yml", "rb"))["add"],
                             ids=["int", "bignum", "float", "negative"])
    def test_add(self, testcal, a, b, result):
        assert result == testcal.add(a, b)

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("cal_data.yml", "rb"))["sub"],
                             ids=["int", "bignum", "float", "negative"])
    def test_sub(self, testcal, a, b, result):
        assert result == testcal.sub(a, b)

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("cal_data.yml", "rb"))["mul"],
                             ids=["int", "bignum", "float", "negative"])
    def test_mul(self, testcal, a, b, result):
        assert result == testcal.mul(a, b)

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("cal_data.yml", "rb"))["div"],
                             ids=["int", "bignum", "float", "negative", "div=0"])
    def test_div(self, testcal, a, b, result):
        if b == 0:
            print("除数不能为0")
        else:
            assert result == testcal.div(a, b)
