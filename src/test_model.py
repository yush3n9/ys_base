'''
Created on Jul 18, 2018

@author: wang
'''
from base import ModulBase


class TestModul(ModulBase):

    def exec_module(self):
        print(self.retriev_current_name())

if __name__ == '__main__':
    TestModul().exec_module()