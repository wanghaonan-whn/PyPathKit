import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Union
from pathkit.process.base.abc import BaseReader


class XMLReader(BaseReader):
    def __init__(self, path: str | Path) -> None:
        super().__init__(path)
        self.__tree = ET.parse(self.path)
        self.__root = self.__tree.getroot()

    def read(self) -> str:
        return ET.tostring(self.__root, encoding="unicode")

    def get_root(self) -> str:
        return self.__root.tag

    def find(self, xpath: str) -> Union[ET.Element, None]:
        return self.__root.find(xpath)

    def findall(self, xpath: str) -> list[ET.Element]:
        return self.__root.findall(xpath)

    def get_text(self, xpath: str) -> Union[str, None]:
        """ 获取节点文本 """
        node = self.find(xpath)
        return node.text if node is not None else None

    def get_attr(self, xpath: str, attr_name: str, default=None) -> Union[str, None]:
        """ 获取节点属性 """
        node = self.find(xpath)
        return node.attrib.get(attr_name, default) if node is not None else default

    @property
    def label_name(self) -> list[Union[str, None]]:
        label_name = [obj.find("name").text for obj in self.__root.findall("object")]
        return label_name

