import os
from pathlib import Path
from typing import List, Union

from pathkit.process.reader import XMLReader


class PathList(list):
    def parent(self):
        parents = [p.parent if isinstance(p, Path) else Path(p).parent for p in self]
        parents = list(dict.fromkeys(parents))  # 保序去重
        return PathList(parents)

    def to_str(self) -> list[str]:
        return [str(p) for p in self]


class PurePath:
    """ 路径语义处理 """

    def __init__(self, path: Union[str, Path]):
        self.path = Path(path)

    def __str__(self):
        return str(self.path)

    @classmethod
    def join(cls, *args: Union[str, Path]) -> "PurePath":
        """ 路径拼接 """
        if not args:
            raise ValueError("join() requires at least one path segment")
        return cls(Path(*args))

    def normalize(self) -> "PurePath":
        """ 规范化分隔符 """
        return PurePath(self.path)

    def resolve(self) -> "PurePath":
        """ 基路径 -> 绝对路径 """
        return PurePath(self.path.resolve())

    def relative_other(self, other: Union[str, Path, "PurePath"]) -> "PurePath":
        """ 相对路径 """
        base = other.path if isinstance(other, PurePath) else Path(other)
        return PurePath(self.path.relative_to(base))

    @property
    def basename(self) -> str:
        """ 文件名 """
        return self.path.name

    @property
    def dirname(self) -> "PurePath":
        """ 父路径 """
        return PurePath(self.path.parent)

    @property
    def stem(self) -> str:
        """ 去扩展名文件名 """
        return self.path.stem

    @property
    def suffix(self) -> str:
        """ 扩展名 """
        return self.path.suffix

    @property
    def suffixes(self) -> List[str]:
        """ all 扩展名 """
        return self.path.suffixes

    @property
    def parts(self) -> tuple[str, ...]:
        """ 分层级取路径名 """
        return self.path.parts

    def with_suffix(self, suffix: str) -> "PurePath":
        """ 修改扩展名 """
        return PurePath(self.path.with_suffix(suffix))

    def with_name(self, name: str) -> "PurePath":
        """ 修改文件名 """
        return PurePath(self.path.with_name(name))

    def is_absolute(self) -> bool:
        """ 绝对路径 """
        return self.path.is_absolute()

    def common_path(self, *others: Union[str, Path, "PurePath"]) -> "PurePath":
        """ 共同父路径 """
        paths = [str(self.path)]
        for other in others:
            paths.append(str(other.path) if isinstance(other, PurePath) else str(Path(other)))
        return PurePath(os.path.commonpath(paths))

    def matches(self, pattern: str) -> bool:
        """ glob匹配 """
        return self.path.match(pattern)


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


if __name__ == "__main__":
    file = PurePath.join(r"D:\Projects\PyPathKit\pathkit\base\*.txt").parts
    print(file)
