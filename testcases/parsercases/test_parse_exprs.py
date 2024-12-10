from parser.parse_exprs import exprs
import pytest as ptt

class TestParseExprs:
    @ptt.fixture(params=[
        (
            '''
            ASK "是否需要检查家中安全系统？(是/否)" -> security_check
            IF security_check == "是":
               OUT "正在检查安全系统……"
               IF system_status == "正常":
                     OUT "安全系统运行正常，无需担心。"
               ELSE:
                     OUT "发现异常！建议检查报警装置和监控系统。"
               ;
            ELSE:
               OUT "好的，跳过安全检查。"
            ;

            ASK "是否需要开启夜间防护模式？(是/否)" -> night_mode
            IF night_mode == "是":
               OUT "夜间防护模式已开启，所有门窗已锁定，监控已启用。"
            ELSE:
               OUT "保持正常模式。"
            ;
            -> FOLLOW_UP
            ''',
            [['ask', '是否需要检查家中安全系统？(是/否)', 'security_check'], [['if', ['security_check', '==', '是'], ['out', '正在检查安全系统……'], [['if', ['system_status', '==', '正常'], ['out', '安全系统运行正常，无需担心。']], ['else', ['out', '发现异常！建议检查报警装置和监控系统。']]]], ['else', ['out', '好的，跳过安全检查。']]], ['ask', '是否需要开启夜间防护模式？(是/否)', 'night_mode'], [['if', ['night_mode', '==', '是'], ['out', '夜间防护模式已开启，所有门窗已锁定，监控已启用。']], ['else', ['out', '保持正常模式。']]], ['FOLLOW_UP']]
        )
    ])
    def stub_input(self, request):
        return request.param
    
    def test_parse_exprs(self, stub_input):
        s, expected = stub_input
        result = exprs.parse_string(s, parse_all=True).as_list()
        assert result == expected