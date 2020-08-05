import pytest,allure
#针对类级别
class Test_03:
    def setup_class(self):
        print("------setup_class")

    def teardown_class(self):
        print("-------teardown_class")

    def test_a(self):
        print("test_a-----")

    def test_b(self):
        print("test_b-----")

    @pytest.mark.parametrize("a",[1,2,3])  #参数
    @allure.step('我是测试步骤001')     #步骤
    @allure.severity(allure.severity_level.BLOCKER)
    def test_al(self,a):
          allure.attach("描述","我是测试步骤001的描述")
          assert a!=2

if __name__ == '__main__':
    pytest.main(["-s","Test_03.py"])