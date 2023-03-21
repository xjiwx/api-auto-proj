# 使用pytest收集所有的测试用例并运行，输出allure报告
import pytest
import os


# 生成JSON数据,加上--clean-alluredir解决JSON文件生成冗余问题
pytest.main(["-s", "--alluredir=allure-reports", "--clean-alluredir"])
# 命令：pytest -v -s --alluredir=allure --clean-alluredir

# 将JSON文件转换成HTML格式的测试报告（生成JSON文件路径：outputs/reports/allure; 生成HTML报告路径：outputs/reports/html）
os.system("allure generate allure-reports -o allure-reports/html --clean")
# 命令：allure generate outputs/reports/allure -o outputs/reports/html --clean
# 打开测试报告
os.system("allure serve allure-reports")
# 命令：allure serve outputs/reports/allure
