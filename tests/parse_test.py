import pytest
from models.collection.collection import Collection
from controllers.parsers.config_parser import ConParser
from sys import argv
from models.entry_types.full_entry import FullEntry
from models.entry_types.title_entry import TitleEntry
from models.entry_types.first_entry import FirstEntry
from models.entry_types.second_entry import SecondEntry
from models.entry_types.tag_entry import TagEntry
from models.collection.collection import Collection
from controllers.strategies import modify_strats, view_strats
import constants.info_and_paths as c
import constants.commands as cmd
import constants.errors as e
from os import path, listdir
from pathlib import Path
from controllers.file_handle import FileHandle
from app import call_entry


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
