# -*- coding: utf-8 -*-
"""
Class BibTableOfContents is a dataclass use to contain the metadata for
table of contents information used in class BibManager.
@author: sunlu
"""

from dataclasses import dataclass
from self_error import GeneralErrorMessage

@dataclass
class BibTableOfContents:
    """
    Class BibTableOfContents is a dataclass use to contain the metadata for
    table of contents information used in class BibManager.
    """
    hex_current_index : int
    int_current_layer_pointer : int
    dict_talbe_of_contents : dict
    def __init__(self):
        self.hex_current_index = 0x00000000
        self.int_current_layer_pointer = 0
        self.dict_table_of_contents = {}
    def create_table_of_contents(self, lst_table_of_contents : list):
        """
        create_table_of_contents_from_list creates the table of contents from a
        multi-dimention list.
        """
        self.hex_current_index = 0x00000000
        self.int_current_layer_pointer = 0
        self.dict_table_of_contents = {}
        self.__creat_sublayer_from_list(lst_table_of_contents)
    def __creat_sublayer_from_list(self, lst_single_list : list):
        """
        __read_list reads a single list and create a sub-layer accordingly. 
        """
        self.change_layer(1)
        for iter_item in lst_single_list:
            if isinstance(iter_item, list):
                self.__creat_sublayer_from_list(iter_item)
            else:
                self.add_item(iter_item)
        self.change_layer(-1)
    def add_item(self, str_item_name : str):
        """
        __add_item adds a new (sub)section to the current layer
        """
        int_current_layer_index = self.__get_current_layer_index()
        if (1<= int_current_layer_index + 1 <= 15):
            self.hex_current_index = \
                self.hex_current_index + 16**(8-self.int_current_layer_pointer)
            self.hex_current_index = \
                self.hex_current_index - \
                (self.hex_current_index % 16**(8-self.int_current_layer_pointer))
        else:
            GeneralErrorMessage("Variable int_current_layer_index overflow.")
        self.dict_table_of_contents[self.hex_current_index] =  str_item_name
    def change_layer(self, int_change_layer : int):
        """
        change_layer changes the layer of the index of the talbe of contents
        """
        if (0 <= self.int_current_layer_pointer + int_change_layer <= 8):
            self.int_current_layer_pointer = self.int_current_layer_pointer + int_change_layer
        else:
            GeneralErrorMessage("Variable int_current_layer_pointer overflow.")
    def __get_current_layer_index(self):
        """
        __get_current_layer_index calculates the current layer index from
        self.hex_current_index and self.int_current_layer_pointer
        """
        d1 = (16**(8-self.int_current_layer_pointer+1))
        d2 = (16**(8-self.int_current_layer_pointer))
        return (self.hex_current_index % d1) // d2