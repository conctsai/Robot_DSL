import pyparsing as pp
from parser.parse_basic_unit import whitespace, id, arrow

trans_expr = pp.Group(arrow
                      + whitespace
                      + id("trans"))