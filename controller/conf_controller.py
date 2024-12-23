import os
from typing import Mapping, List, Union
from model.dsl_tree import DSLTree
from parser.parsing import parse_file
from error.controller_runtime_error import ConfNotFoundError
from error.parse_error import ParseError

class ConfController:
    '''
    配置文件控制器，用于管理配置文件
    '''
    def __init__(self, conf_dir='conf', end='czz'):
        '''
        初始化配置文件控制器
        :param conf_dir: 配置文件目录，默认为conf
        :param end: 配置文件后缀名，默认为czz
        '''
        # 扫描conf目录下的所有配置文件
        self.end = end
        self.conf_map: Mapping[str, Union[None, DSLTree]] = {}
        self.conf_dir = conf_dir
        for conf_file in os.listdir(self.conf_dir):
            if conf_file.endswith(self.end):
                # 删除后缀名
                self.conf_map[conf_file[:-len(self.end)-1]] = None
                
    def get_dsl_tree(self, conf_name: str) -> DSLTree:
        '''
        根据配置文件名获取DSL树
        :param conf_name: 配置文件名
        :return: DSL树
        '''
        if conf_name not in self.conf_map:
            raise ConfNotFoundError(f"Configuration file {conf_name} not found")
        try:
            self.conf_map[conf_name] = parse_file(os.path.join(self.conf_dir, conf_name + '.' + self.end))
        except ParseError as e:
            self.conf_map[conf_name] = None
            raise ParseError(f"Configuration file {conf_name} parse error: {e.message}")
        return self.conf_map[conf_name]

    def get_all_conf_name(self) -> List[str]:
        '''
        获取所有配置文件名
        :return: 所有配置文件名
        '''
        return list(self.conf_map.keys())