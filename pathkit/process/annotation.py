from typing import List

from pathkit.base.path import PathEntry, PathList
from pathkit.base.utils import PathUtils
from pathkit.process.xmldocument import XMLDocument


class AnnotationUtils:
    """
        XML 工具
    """

    @staticmethod
    def get_xml_label_names(xml_path: str | PathEntry) -> list[str]:
        """获取标注 XML 中所有 object/name 文本"""
        document = XMLDocument(xml_path)
        return [
            node.text
            for node in document.findall("object/name")
            if node.text is not None
        ]

    @staticmethod
    def get_xmls_label_names(xmls_path: str | PathEntry) -> list[str]:
        xmls_path_list = PathUtils.glob_paths(xmls_path, "*.xml")
        label_names = [
            node.text
            for document in xmls_path_list
            for node in XMLDocument(document).findall("object/name")
            if node.text is not None
        ]
        return PathList(label_names).unique().to_str()

    @staticmethod
    def get_keyword_with_xml_label(src_path: str, keyword: str, is_recursion: bool = False) -> PathList:
        """ 关键词查找对应的xml文件 """
        file_paths = PathUtils.get_file_paths_with_suffix(src_path, suffix="xml", is_recursion=is_recursion)
        target_path = []
        for file_path in file_paths:
            if keyword in AnnotationUtils.get_xml_label_names(file_path):
                target_path.append(file_path)
        return PathList(target_path)

    @staticmethod
    def parse_xml(src_path: str | PathEntry) -> List:
        document = XMLDocument(src_path)
        parse_list = []
        for node in document.findall("object"):
            name = node.find("name").text
            bbox = node.find("bndbox")
            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)
            parse_list.append(
                [xmin, ymin, xmax, ymax, name]
            )
        return parse_list


if __name__ == "__main__":
    xmls_path = "/mnt/8T/TF/上拉杆窜出/赛马/datasets/xml"
    label_name = AnnotationUtils.get_xmls_label_names(xmls_path)
    keyword = "zjb__<slg>__cuanchu"
    xml_path_with_keyword = AnnotationUtils.get_keyword_with_xml_label(xmls_path, keyword).to_str()
    xml_path = "/mnt/8T/TF/上拉杆窜出/赛马/datasets/xml/上拉杆窜出_0__Q63F06F01_20260410_074441_35__C70__16_3_10.xml"
    parse_doc = AnnotationUtils.parse_xml(xml_path)
    print(parse_doc)
