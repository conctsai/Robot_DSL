from parser.parsing import parse
from model.dsl_tree import serialize

print(
   serialize(
      parse.parse_string(
                '''
                STATE INITIAL:
                    ASK "你好，我是{robot}，请问我可以怎么称呼您？" -> name
                    OUT "你好，{name}，很高兴为您服务！"
                    -> HELP

                STATE HELP:
                    ASK "请问有什么可以帮助您的？(天气/温度/灯光/安全/清扫)" -> task

                    IF task == "天气":
                        -> WEATHER_UPDATE
                    ELIF task == "温度":
                        -> TEMPERATURE_CONTROL
                    ELIF task == "灯光":
                        -> LIGHT_CONTROL
                    ELIF task == "安全":
                        -> SECURITY_CHECK
                    ELSE:
                        -> CLEANING_CONTROL
                    ;
                ''', parse_all=True
            ).as_dict()
   ).__str__()
   
)