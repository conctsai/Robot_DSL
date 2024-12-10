from engine.string_operation import StringOperation
import pytest as ptt

class TestStringOperation:
    
    @ptt.fixture(params=[
        ("abc", "abc", True),
        ("abc", "def", False)
    ])
    def stub_equal_string(self, request):
        return request.param
    
    def test_equal_string(self, stub_equal_string):
        assert StringOperation.euqal_string(stub_equal_string[0], stub_equal_string[1]) == stub_equal_string[2]
    
    @ptt.fixture(params=[
        ("abc", "a.c", True),
        ("abc", "d.f", False),
        ("abc", "a.*c", True),
        ("abc", "d.*f", False),
        ("123", "[0-9]+", True),
        ("abc", "[0-9]+", False)
    ])
    def stub_regex_string(self, request):
        return request.param
    
    def test_regex_string(self, stub_regex_string):
        assert StringOperation.regex_string(stub_regex_string[0], stub_regex_string[1]) == stub_regex_string[2]
        
    
    @ptt.fixture(params=[
        ("1", "2", False),
        ("2", "1", True),
        ("1", "1", False),
        ("a", "b", False),
        ("aa", "a", True),
    ])
    def stub_greater_number(self, request):
        return request.param
    
    def test_greater_number(self, stub_greater_number):
        assert StringOperation.greater_number(stub_greater_number[0], stub_greater_number[1]) == stub_greater_number[2]
        
        
    @ptt.fixture(params=[
        ("1", "2", True),
        ("2", "1", False),
        ("1", "1", False),
        ("a", "b", True),
        ("aa", "a", False),
    ])
    def stub_less_number(self, request):
        return request.param
    
    def test_less_number(self, stub_less_number):
        assert StringOperation.less_number(stub_less_number[0], stub_less_number[1]) == stub_less_number[2]
        
        
    @ptt.fixture(params=[
        ("1", "2", False),
        ("2", "1", True),
        ("1", "1", True),
        ("a", "b", False),
        ("aa", "a", True),
    ])
    def stub_greater_equal_number(self, request):
        return request.param
    
    def test_greater_equal_number(self, stub_greater_equal_number):
        assert StringOperation.greater_equal_number(stub_greater_equal_number[0], stub_greater_equal_number[1]) == stub_greater_equal_number[2]
        
    
    @ptt.fixture(params=[
        ("1", "2", True),
        ("2", "1", False),
        ("1", "1", True),
        ("a", "b", True),
        ("aa", "a", False),
    ])
    def stub_less_equal_number(self, request):
        return request.param
    
    def test_less_equal_number(self, stub_less_equal_number):
        assert StringOperation.less_equal_number(stub_less_equal_number[0], stub_less_equal_number[1]) == stub_less_equal_number[2]
        
    @ptt.fixture(params=[
        ("1", "2", True),
        ("01", "1", False),
        ("a", "b", True),
        ("a", "a", False)
    ])
    def stub_not_equal_string(self, request):
        return request.param
    
    def test_not_equal_string(self, stub_not_equal_string):
        assert StringOperation.not_equal_string(stub_not_equal_string[0], stub_not_equal_string[1]) == stub_not_equal_string[2]