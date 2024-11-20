from parser.parse_out import out_expr

class TestParseOut:
    def test_parse_out_uppercase(self):
        s = 'OUT "hello world"'
        result = out_expr.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'out'
        assert result[0][1] == 'hello world'
        
    def test_parse_out_lowercase(self):
        s = 'out "hello world"'
        result = out_expr.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'out'
        assert result[0][1] == 'hello world'
        
    def test_parse_out_mixedcase(self):
        s = 'oUt "hello world"'
        result = out_expr.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'out'
        assert result[0][1] == 'hello world'