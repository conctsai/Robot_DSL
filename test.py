import pytest as ptt

def run_test():
    ptt.main(['-v', '-s' ,'-W','ignore:Module already imported:pytest.PytestWarning'])

    
if __name__ == '__main__':
    run_test()