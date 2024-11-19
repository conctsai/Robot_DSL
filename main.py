from parser.parsing import parse_file
from engine.running_engine import RunningEngine

if __name__ == "__main__":
    tree = parse_file("conf/conf.czz")
    RunningEngine(tree).run()