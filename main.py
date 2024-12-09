from parser.parsing import parse_file
from controller.engine_controller import EngineController

if __name__ == "__main__":
    tree = parse_file("conf/conf.czz")
    ec = EngineController(tree)
    input_ = []
    flag = False
    while True:
        flag, output = ec.get_output(input_)
        for item in output:
            print(item)
        input_ = []
        if flag:
            break
        input_.append(input())
                