import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Union

from base.abc import BaseReader


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


xml_path = "/mnt/8T/TE/datasets/实车/download-2026-04-10_20-32-04/teds/转向架/未区分项点/PS_20260312_TEDS_定位节点螺栓松脱_CR400AF_30处/CHANGSHASUOHKJ_20250422024354_4_CR400AF-1016_1/xml/1_3.xml"
xmlreader = XMLReader(xml_path)
print(xmlreader.findall("folder"))