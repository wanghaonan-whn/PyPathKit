from pathkit.base.path import PathEntry, PathList
from pathkit.base.utils import PathUtils
from pathkit.process.xmldocument import XMLDocument


class AnnotationPathUtils:
    """Helpers for annotation-style file discovery rules."""

    @staticmethod
    def get_file_path_with_channel(src_path: str, channel: list[int], suffix: str) -> PathList:
        file_paths = PathUtils.get_file_paths_with_suffix(src_path, suffix=suffix, is_recursion=True)
        filtered_paths_with_channel = [
            file_path for file_path in file_paths if int(file_path.name.split("--")[0][-1]) in channel
        ]
        return PathList(filtered_paths_with_channel)

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
    def get_keyword_with_xml_label(src_path: str, key_word: str, is_recursion: bool = False) -> PathList:
        """ 关键词查找对应的xml文件 """
        file_paths = PathUtils.get_file_paths_with_suffix(src_path, suffix="xml", is_recursion=is_recursion)
        target_path = []
        for xml_path in file_paths:
            if key_word in AnnotationPathUtils.get_xml_label_names(xml_path):
                target_path.append(xml_path)
        return PathList(target_path)
