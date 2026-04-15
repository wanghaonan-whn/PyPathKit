import xml.etree.ElementTree as ET
from pathkit import PathEntry
from pathkit.process.base.abc import BaseReader


class XMLDocument(BaseReader):
    def __init__(self, path: str | PathEntry) -> None:
        super().__init__(path)
        self._tree = ET.parse(self.path)
        self._root = self._tree.getroot()

    def read(self) -> str:
        return ET.tostring(self._root, encoding="unicode")

    def get_root(self) -> str:
        return self._root.tag

    def find(self, xpath: str) -> ET.Element | None:
        return self._root.find(xpath)

    def findall(self, xpath: str) -> list[ET.Element]:
        return self._root.findall(xpath)

    def get_text(self, xpath: str) -> str | None:
        """获取节点文本"""
        node = self.find(xpath)
        return node.text if node is not None else None

    def get_attr(self, xpath: str, attr_name: str, default: str | None = None) -> str | None:
        """获取节点属性"""
        node = self.find(xpath)
        return node.attrib.get(attr_name, default) if node is not None else default

    def update_value(self, xpath: str, new_value: str) -> None:
        """更新节点文本"""
        node = self.find(xpath)
        if node is not None:
            node.text = new_value

    def save(self, path: str | PathEntry | None = None) -> None:
        """保存 XML 到指定路径，默认覆盖原文件"""
        target = self.path if path is None else (path.path if isinstance(path, PathEntry) else path)
        self._tree.write(target, encoding="utf-8", xml_declaration=True)

    @property
    def label_name(self) -> list[str | None]:
        label_names = []
        for obj in self._root.findall("object"):
            name_node = obj.find("name")
            label_names.append(name_node.text if name_node is not None else None)
        return label_names
