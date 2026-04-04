import os
from pathlib import Path
from typing import List, Union


class PathList(list):
    def parent(self):
        parents = [p.parent if isinstance(p, Path) else Path(p).parent for p in self]
        parents = list(dict.fromkeys(parents))  # 保序去重
        return PathList(parents)

    def to_str(self) -> list[str]:
        return [str(p) for p in self]


class PathEntry:
    """路径语义处理"""

    def __init__(self, path: Union[str, Path]):
        self.path = Path(path)

    def __str__(self):
        return str(self.path)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.path!s})"

    @classmethod
    def join(cls, *args: Union[str, Path]) -> "PathEntry":
        """路径拼接"""
        if not args:
            raise ValueError("join() requires at least one path segment")
        return cls(Path(*args))

    def normalize(self) -> "PathEntry":
        """规范化分隔符"""
        return PathEntry(os.path.normpath(str(self.path)))

    def resolve(self) -> "PathEntry":
        """基路径 -> 绝对路径"""
        return PathEntry(self.path.resolve())

    def relative_to(self, other: Union[str, Path, "PathEntry"]) -> "PathEntry":
        """相对路径"""
        base = other.path if isinstance(other, PathEntry) else Path(other)
        return PathEntry(self.path.relative_to(base))

    def relative_other(self, other: Union[str, Path, "PathEntry"]) -> "PathEntry":
        return self.relative_to(other)

    @property
    def basename(self) -> str:
        """文件名"""
        return self.path.name

    @property
    def dirname(self) -> "PathEntry":
        """父路径"""
        return PathEntry(self.path.parent)

    @property
    def stem(self) -> str:
        """去扩展名文件名"""
        return self.path.stem

    @property
    def suffix(self) -> str:
        """扩展名"""
        return self.path.suffix

    @property
    def suffixes(self) -> List[str]:
        """all 扩展名"""
        return self.path.suffixes

    @property
    def parts(self) -> tuple[str, ...]:
        """ """
        return self.path.parts

    def with_suffix(self, suffix: str) -> "PathEntry":
        """修改扩展名"""
        return PathEntry(self.path.with_suffix(suffix))

    def with_name(self, name: str) -> "PathEntry":
        """修改文件名"""
        return PathEntry(self.path.with_name(name))

    def is_absolute(self) -> bool:
        """绝对路径"""
        return self.path.is_absolute()

    def common_path(self, *others: Union[str, Path, "PathEntry"]) -> "PathEntry":
        """共同父路径"""
        paths = [str(self.path)]
        for other in others:
            paths.append(
                str(other.path) if isinstance(other, PathEntry) else str(Path(other))
            )
        return PathEntry(os.path.commonpath(paths))

    def matches(self, pattern: str) -> bool:
        """glob匹配"""
        return self.path.match(pattern)

    def exists(self) -> bool:
        return self.path.exists()

    def is_file(self) -> bool:
        return self.path.is_file()

    def is_dir(self) -> bool:
        return self.path.is_dir()

    def is_symlink(self) -> bool:
        return self.path.is_symlink()
