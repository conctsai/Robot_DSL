import pyhocon
import os
import datetime

def update_file(config, file):
    config = pyhocon.HOCONConverter.to_hocon(config)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(config)
    return pyhocon.ConfigFactory.parse_file(file)




current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
os.environ['current_time'] = current_time

main = pyhocon.ConfigFactory.parse_file('robot.d/main.cconf', resolve=False)

# op = main['status']['start']['operation'][0]

# print(op)

# print(op.items())

# param = pyhocon.ConfigFactory.parse_file('robot.d/param.cconf')

# print(param)

# param['param']['username'] = '张三'

# param = update_file(param, 'robot.d/param.cconf')

# print(param)

# main = pyhocon.ConfigFactory.parse_file('robot.d/main.cconf')

# print(main)




