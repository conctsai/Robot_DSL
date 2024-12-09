import os
from typing import Mapping
from model.dsl_tree import DSLTree
from parser.parsing import parse_file
from error.controller_runtime_error import ConfNotFoundError

class ConfController:
    def __init__(self, conf_dir='conf', end='czz'):
        # 扫描conf目录下的所有配置文件
        self.end = end
        self.conf_map: Mapping[str, DSLTree] = {}
        conf_dir = conf_dir
        for conf_file in os.listdir(conf_dir):
            if conf_file.endswith(self.end):
                # 删除后缀名
                self.conf_map[conf_file[:-len(self.end)-1]] = parse_file(os.path.join(conf_dir, conf_file))
                
    def get_dsl_tree(self, conf_name: str) -> DSLTree:
        if conf_name not in self.conf_map:
            raise ConfNotFoundError(f"Configuration file {conf_name} not found")
        return self.conf_map[conf_name]
            

if __name__ == '__main__':
    cc = ConfController()
    print(cc.conf_map['conf'])