# -*- coding: utf-8 -*-
"""
Class BibReference is a dataclass that represents a reference.
@author: github.com/sunluelectric
"""

from enum import Enum
from dataclasses import dataclass

class PublicationType(Enum):
    """
    class PublicationType is an enum class for different publication categories.
    """
    BOOK = 1
    ARTICLE = 2
    INPROCEEDINGS = 3
    ONLINE = 4
    OTHERS = 5

from dataclasses import dataclass

@dataclass
class BibReference:
    """
    Class BibReference is a dataclass that represents a reference.

    Attributes:
    - enum_type (PublicationType): The type of publication.
    - str_type (str): The string representation of the publication type.
    - str_id (str): The ID of the reference.
    - str_title (str): The title of the reference.
    - str_author (str): The author(s) of the reference.
    - str_journal (str): The journal name (for articles and books).
    - str_volume (str): The volume number (for articles and books).
    - str_number (str): The number (for articles and books).
    - str_pages (str): The page numbers (for articles and books).
    - str_year (str): The year of publication.
    - str_publisher (str): The publisher (for books).
    - str_booktitle (str): The title of the book (for inproceedings).
    - str_organization (str): The organization (for inproceedings).
    - str_url (str): The URL of the reference (for online references).
    - str_urldate (str): The date when the URL was accessed (for online references).
    - hex_catid (int): The hexadecimal category ID (for bib management).
    """

    enum_type: PublicationType
    str_type: str
    str_id: str
    str_title: str
    str_author: str
    str_journal: str
    str_volume: str
    str_number: str
    str_pages: str
    str_year: str
    str_publisher: str
    str_booktitle: str
    str_organization: str
    str_url: str
    str_urldate: str
    hex_catid: int

    def __init__(self):
        self.enum_type = None
        self.str_type = None
        self.str_id = None
        self.str_title = None
        self.str_author = None
        # book and article
        self.str_journal = None
        self.str_volume = None
        self.str_number = None
        self.str_pages = None
        self.str_year = None
        self.str_publisher = None
        # inproceedings
        self.str_booktitle = None
        self.str_organization = None
        # online
        self.str_url = None
        self.str_urldate = None
        # bib management
        self.hex_catid = None

    def return_refs_printout(self):
        """
        return_refs_printout returns the reference information in a list with
        printout format.

        Returns:
        - list: A list containing the reference information in printout format.
        """
        if (self.str_id is not None) and (self.str_type is not None):
            lst_print = []
            str_print = '@' + self.str_type + '{' + self.str_id + ','
            lst_print.append(str_print)
            if self.str_title is not None:
                str_print = '  ' + 'title = {' + self.str_title + '},'
                lst_print.append(str_print)
            if self.str_author is not None:
                str_print = '  ' + 'author = {' + self.str_author + '},'
                lst_print.append(str_print)
            if self.str_journal is not None:
                str_print = '  ' + 'journal = {' + self.str_journal + '},'
                lst_print.append(str_print)
            if self.str_volume is not None:
                str_print = '  ' + 'volume = {' + self.str_volume + '},'
                lst_print.append(str_print)
            if self.str_number is not None:
                str_print = '  ' + 'number = {' + self.str_number + '},'
                lst_print.append(str_print)
            if self.str_pages is not None:
                str_print = '  ' + 'pages = {' + self.str_pages + '},'
                lst_print.append(str_print)
            if self.str_year is not None:
                str_print = '  ' + 'year = {' + self.str_year + '},'
                lst_print.append(str_print)
            if self.str_publisher is not None:
                str_print = '  ' + 'publisher = {' + self.str_publisher + '},'
                lst_print.append(str_print)
            if self.str_booktitle is not None:
                str_print = '  ' + 'booktitle = {' + self.str_booktitle + '},'
                lst_print.append(str_print)
            if self.str_organization is not None:
                str_print = '  ' + 'organization = {' + self.str_organization + '},'
                lst_print.append(str_print)
            if self.str_url is not None:
                str_print = '  ' + 'url = {' + self.str_url + '},'
                lst_print.append(str_print)
            if self.str_urldate is not None:
                str_print = '  ' + 'urldate = {' + self.str_urldate + '},'
                lst_print.append(str_print)
            if self.hex_catid is not None:
                str_print = '}' + ' % catid = ' + hex(self.hex_catid)
                lst_print.append(str_print)
            else:
                str_print = '}'
                lst_print.append(str_print)
            lst_print[-2] = lst_print[-2][:-1] # delete the comma in the last valid attribute
            return lst_print
        return None
    