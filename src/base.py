'''
Created on Jul 13, 2018

@author: wang
'''
from abc import ABCMeta
from abc import abstractmethod
import collections
import configparser
import json
import logging.config
import os

logger = logging.getLogger(__name__)


class ModulBase(metaclass=ABCMeta):
    
    def __init__(self):
        self.init_logging()
        self.cfg = self.init_ordered_configparser()
    
    def init_logging(self, default_path='../config/logging.json', default_level=logging.INFO):
        path = default_path
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            
    def init_ordered_configparser(self):
        confs = collections.OrderedDict()
        for root, dirs, files in os.walk("../config"):
            for name in files:
                if name.endswith('conf'):
                    parts = name.split('_')
                    confs[int(parts[0])] = os.path.join(root, name)
        config = configparser.ConfigParser()
        config.read(confs.values())
        logger.debug(config.sections())
        return config
    
    def retriev_current_name(self):
        return [e.strip() for e in self.cfg.get('modul_main', 'name').split(',')]
    


    @abstractmethod
    def exec_module(self):
        raise NotImplemented
    

