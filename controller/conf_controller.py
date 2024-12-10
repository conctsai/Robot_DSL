import os
from typing import Mapping, List, Union
from model.dsl_tree import DSLTree
from parser.parsing import parse_file
from error.controller_runtime_error import ConfNotFoundError
from error.parse_error import ParseError

class ConfController:
    def __init__(self, conf_dir='conf', end='czz'):
        # 扫描conf目录下的所有配置文件
        self.end = end
        self.conf_map: Mapping[str, Union[None, DSLTree]] = {}
        self.conf_dir = conf_dir
        for conf_file in os.listdir(self.conf_dir):
            if conf_file.endswith(self.end):
                # 删除后缀名
                self.conf_map[conf_file[:-len(self.end)-1]] = None
                
    def get_dsl_tree(self, conf_name: str) -> DSLTree:
        if conf_name not in self.conf_map:
            raise ConfNotFoundError(f"Configuration file {conf_name} not found")
        try:
            self.conf_map[conf_name] = parse_file(os.path.join(self.conf_dir, conf_name + '.' + self.end))
        except ParseError as e:
            self.conf_map[conf_name] = None
            raise ParseError(f"Configuration file {conf_name} parse error: {e.message}")
        return self.conf_map[conf_name]

    def get_all_conf_name(self) -> List[str]:
        return list(self.conf_map.keys())
            

if __name__ == '__main__':
    cc = ConfController()
    print(cc.get_all_conf_name())