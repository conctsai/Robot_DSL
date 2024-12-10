import pytest as ptt

def run_test():
    # -v: 冗长输出，-s: 输出到控制台，-W: 忽略pytest警告
    return ptt.main(['-v', '-s' ,'-W','ignore:Module already imported:pytest.PytestWarning'])

    
if __name__ == '__main__':
    run_test()