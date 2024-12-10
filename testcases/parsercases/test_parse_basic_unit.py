from parser.parse_basic_unit import id, equals, whitespace, colon, comma, arrow, equal, reg, string
import pytest as ptt
import pyparsing as pp

class TestBasicUnit:
    @ptt.fixture(params=[
        ('abc_123', ['abc_123']),
        ('_abc_123', ['_abc_123']),
        ('123abc', pp.exceptions.ParseException)
    ])
    def stub_id(self, request):
        return request.param
    
    def test_id(self, stub_id):
        s, expected = stub_id
        if isinstance(expected, list):
            result = id.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                id.parseString(s, parse_all=True)
                
    @ptt.fixture(params=[
        ('=', []),
        ('==', pp.exceptions.ParseException)
    ])
    def stub_equals(self, request):
        return request.param
            
    def test_equals(self, stub_equals):
        s, expected = stub_equals
        if isinstance(expected, list):
            result = equals.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                equals.parseString(s, parse_all=True)
                
                
    @ptt.fixture(params=[
        (':', []),
        ('::', pp.exceptions.ParseException)
    ])
    def stub_colon(self, request):
        return request.param
            
    def test_colon(self, stub_colon):
        s, expected = stub_colon
        if isinstance(expected, list):
            result = colon.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                colon.parseString(s, parse_all=True)
            
            
            
    @ptt.fixture(params=[
        (';', []),
        (';;', pp.exceptions.ParseException)
    ])
    def stub_comma(self, request):
        return request.param
    def test_comma(self, stub_comma):
        s, expected = stub_comma
        if isinstance(expected, list):
            result = comma.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                comma.parseString(s, parse_all=True)
                
                
    @ptt.fixture(params=[
        ('->', []),
        ('-->', pp.exceptions.ParseException)
    ])
    def stub_arrow(self, request):
        return request.param
            
    def test_arrow(self, stub_arrow):
        s, expected = stub_arrow
        if isinstance(expected, list):
            result = arrow.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                arrow.parseString(s, parse_all=True)
                
                
    @ptt.fixture(params=[
        ('==', ['==']),
        ('=', pp.exceptions.ParseException)
    ])
    def stub_equal(self, request):
        return request.param
            
    def test_equal(self, stub_equal):
        s, expected = stub_equal
        if isinstance(expected, list):
            result = equal.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                equal.parseString(s, parse_all=True)
                
                
    @ptt.fixture(params=[
        ('~=', ['~=']),
        ('~', pp.exceptions.ParseException)
    ])
    def stub_reg(self, request):
        return request.param
    def test_reg(self, stub_reg):
        s, expected = stub_reg
        if isinstance(expected, list):
            result = reg.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                reg.parseString(s, parse_all=True)
                
                
    @ptt.fixture(params=[
        ("'abc'", ["abc"]),
        ('"abc"', ["abc"]),
        (r"'a\'bc'", ["a'bc"]),
        (r'"a\"bc"', ["a\"bc"]),
        ("'abc", pp.exceptions.ParseException),
        ('"abc', pp.exceptions.ParseException),
        (r"'a\'bc", pp.exceptions.ParseException),
    ])
    def stub_string(self, request):
        return request.param
            
    def test_string(self, stub_string):
        s, expected = stub_string
        if isinstance(expected, list):
            result = string.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                string.parseString(s, parse_all=True)