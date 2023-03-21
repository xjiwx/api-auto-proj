from testFunctions.read_excel import ExcelUtil

def get_td():
    filepath = r"D:\api proj\testFile\test.xls"
    sheetName = "test_login"
    data = ExcelUtil(filepath, sheetName)
    td = data.dict_data()
    return td

print(get_td())