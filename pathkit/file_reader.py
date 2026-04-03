import xml.etree.ElementTree as ET
from typing import Union, Any

from pathlib import Path


class FileReader:
    def __init__(self, path: Union[str, Path]):
        self.path = path
        self.__label_name = None

    def __read_xml_file(self) -> list[Union[str, None]]:
        tree = ET.parse(self.path)
        root = tree.getroot()
        return [obj.find("name").text for obj in root.findall("object")]

    @property
    def label_name(self) -> list[Union[str, None]]:
        if self.__label_name is None:
            self.__label_name = self.__read_xml_file()
        return self.__label_name
