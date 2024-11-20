from parser.parse_basic_unit import id, equals, whitespace, colon, comma, arrow, equal, reg, string
import pytest as ptt
import pyparsing as pp

class TestBasicUnit:
    def test_id(self):
        s = 'abc_123'
        result = id.parseString(s, parse_all=True).as_list()
        assert result == ['abc_123']
        
        s = '_abc_123'
        result = id.parseString(s, parse_all=True).as_list()
        assert result == ['_abc_123']
        
        with ptt.raises(pp.exceptions.ParseException):
            s = '123abc'
            id.parseString(s, parse_all=True)
            
    def test_equals(self):
        s = '='
        result = equals.parseString(s, parse_all=True).as_list()
        assert result == []
        
        with ptt.raises(pp.exceptions.ParseException):
            s = '=='
            equals.parseString(s, parse_all=True)
            
    def test_colon(self):
        s = ':'
        result = colon.parseString(s, parse_all=True).as_list()
        assert result == []
        
        with ptt.raises(pp.exceptions.ParseException):
            s = '::'
            colon.parseString(s, parse_all=True)
            
    def test_comma(self):
        s = ';'
        result = comma.parseString(s, parse_all=True).as_list()
        assert result == []
        
        with ptt.raises(pp.exceptions.ParseException):
            s = ';;'
            comma.parseString(s, parse_all=True)
            
    def test_arrow(self):
        s = '->'
        result = arrow.parseString(s, parse_all=True).as_list()
        assert result == []
        
        with ptt.raises(pp.exceptions.ParseException):
            s = '-->'
            arrow.parseString(s, parse_all=True)
            
    def test_equal(self):
        s = '=='
        result = equal.parseString(s, parse_all=True).as_list()
        assert result == ['==']
        
        with ptt.raises(pp.exceptions.ParseException):
            s = '='
            equal.parseString(s, parse_all=True)
            
    def test_reg(self):
        s = '~='
        result = reg.parseString(s, parse_all=True).as_list()
        assert result == ['~=']
        
        with ptt.raises(pp.exceptions.ParseException):
            s = '=='
            reg.parseString(s, parse_all=True)
            
    def test_string_with_single_quotation(self):
        s = "'abc'"
        result = string.parseString(s, parse_all=True).as_list()
        assert result == ["abc"]
        
        with ptt.raises(pp.exceptions.ParseException):
            s = "'abc"
            string.parseString(s, parse_all=True)
            
    def test_string_with_double_quotation(self):
        s = '"abc"'
        result = string.parseString(s, parse_all=True).as_list()
        assert result == ["abc"]

        with ptt.raises(pp.exceptions.ParseException):
            s = '"abc'
            string.parseString(s, parse_all=True)
            
    def test_string_escape(self):
        s = r"'a\'bc'"
        result = string.parseString(s, parse_all=True).as_list()
        assert result == ["a'bc"]
        
        s = r'"a\"bc"'
        result = string.parseString(s, parse_all=True).as_list()
        assert result == ["a\"bc"]
        
        with ptt.raises(pp.exceptions.ParseException):
            s = r"'a\'bc"
            string.parseString(s, parse_all=True)