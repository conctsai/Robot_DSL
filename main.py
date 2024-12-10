from parser.parse_state import state_token

print(state_token.parse_string(
            '''
            STATE INITIAL:
               ASK "你好，我是{robot}，请问我可以怎么称呼您？" -> name
               OUT "你好，{name}，很高兴为您服务！"
               -> HELP
            '''
        , parse_all=True))