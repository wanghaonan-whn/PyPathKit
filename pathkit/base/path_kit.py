from pathlib import Path
from typing import List

from pathkit.process.reader import XMLReader


class PathList(list):
    def parent(self):
        parents = [p.parent if isinstance(p, Path) else Path(p).parent for p in self]
        parents = list(dict.fromkeys(parents))  # 保序去重
        return PathList(parents)

    def to_str(self) -> list[str]:
        return [str(p) for p in self]


class PathKit:
    """ 路径语义处理 """

    def join(self):
        """ 路径拼接 """
        pass

    def normalize(self):
        """ 规范化分隔符 """
        pass

    def resolve(self):
        """ 基路径 -> 绝对路径 """
        pass

    def relative(self):
        """ 相对路径 """
        pass

    def basename(self):
        """ 文件名 """
        pass

    def dirname(self):
        """ 父路径 """
        pass

    def stem(self):
        """ 去扩展名文件名 """
        pass

    def suffix(self):
        """ 扩展名 """
        pass

    def suffixes(self):
        """ all 扩展名 """
        pass

    def with_suffix(self, suffix: str):
        """ 修改扩展名 """
        pass

    def with_name(self, name: str):
        """ 修改文件名 """
        pass

    def is_absolute(self):
        """ 绝对路径 """
        pass

    def is_relative(self):
        """ 相对路径 """
        pass

    def common_path(self):
        """ 共同父路径 """
        pass

    def matches(self):
        """ glob匹配 """
        pass

    def parts(self):
        """  """
        pass


class PathUtils:
    def get_file_path_with_channel(self, src_path: str, channel: List[int], suffix: str) -> PathList:
        file_paths = self.get_file_path_with_suffix(src_path, suffix=suffix, is_recursion=True)
        filtered_paths_with_channel = [
            file_path for file_path in file_paths if int(file_path.name.split('--')[0][-1]) in channel
        ]
        return PathList(filtered_paths_with_channel)

    @staticmethod
    def parse_file_with_suffix(src_path: str, is_recursion: bool = False) -> PathList:
        """ 获取路径下所有文件后缀 """
        path = Path(src_path)
        file_paths = path.rglob("*") if is_recursion else path.glob("*")
        suffix = set([file.suffix.lstrip(".") for file in file_paths])
        return PathList(list(suffix))

    @staticmethod
    def get_file_path_with_suffix(src_path: str, suffix: str, is_recursion: bool = False) -> PathList:
        """ 获取路径下匹配后缀的文件列表 """
        suffix = suffix.lstrip(".")
        path = Path(src_path)
        pattern = f"*.{suffix}"
        iterator = path.rglob(pattern) if is_recursion else path.glob(pattern)
        return PathList(list(iterator))

    @staticmethod
    def get_keyword_with_xml_label(src_path: str, key_word: str, is_recursion: bool = False) -> PathList:
        """ 关键词查找对应的xml文件 """
        path = Path(src_path)
        iterator = path.rglob("*.xml") if is_recursion else path.glob("*.xml")
        target_path = []
        for xml_path in iterator:
            if key_word in XMLReader(xml_path).label_name:
                target_path.append(xml_path)
        return PathList(list(target_path))
