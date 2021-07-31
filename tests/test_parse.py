import pytest
from peck.collection import Collection
from peck.config_parser import ConParser
from sys import argv
from peck.full_entry import FullEntry
from peck.title_entry import TitleEntry
from peck.first_entry import FirstEntry
from peck.second_entry import SecondEntry
from peck.tag_entry import TagEntry
from peck.modify_strats import *
import peck.info_and_paths as c
import peck.commands as cmd
import peck.errors as e
from os import path, listdir
from pathlib import Path
from peck.file_handle import FileHandle


class TestConfig:
    def test_ini_parse(self):
        tester = ConParser().parse("tests/idl.ini")
        assert tester["end_marker"] == "#*#*#*#*#*#*#*#*#*#*#*#"
        assert tester["date_underline"] == "-----------------------"
        assert tester["jtitle"] == "idl.txt"
        assert tester["btitle"] == "backup.txt"
        assert tester["first"] == "test_first"
        assert tester["second"] == "test_second"
        assert tester["textbox_use"] == False

class TestFile:
    def test_file_parse(self):
        test = Collection(None, "tests/collection.txt")
        assert len(test.collection) == 3

class TestView:
    def test_printout(self):
        # TODO: make sure things print correctly
        pass
