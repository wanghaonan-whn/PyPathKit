from pathlib import Path

from pathkit.base.path import PathList


class PathUtils:
    """Generic helpers for path scanning and suffix-based filtering."""

    @staticmethod
    def parse_file_with_suffix(src_path: str, is_recursion: bool = False) -> PathList:
        """ 获取路径下所有文件后缀 """
        path = Path(src_path)
        file_paths = path.rglob("*") if is_recursion else path.glob("*")
        suffix = {file.suffix.lstrip(".") for file in file_paths}
        return PathList(list(suffix))

    @staticmethod
    def get_file_path_with_suffix(src_path: str, suffix: str, is_recursion: bool = False) -> PathList:
        """ 获取路径下匹配后缀的文件列表 """
        suffix = suffix.lstrip(".")
        path = Path(src_path)
        pattern = f"*.{suffix}"
        iterator = path.rglob(pattern) if is_recursion else path.glob(pattern)
        return PathList(list(iterator))
