from pathlib import Path


class PathList(list):
    def parent(self, dedup: bool = False, as_str: bool = True):
        parents = [Path(p).parent for p in self]
        if dedup:
            parents = list(dict.fromkeys(parents))  # 保序去重
        if as_str:
            return PathList([str(p) for p in parents])
        return PathList(parents)


class PathKit:
    @staticmethod
    def get_file_with_suffix(src_path: str, suffix: str, is_recursion: bool = False) -> list[str]:
        """ 获取路径下匹配后缀的文件列表 """
        suffix = suffix.lstrip(".")
        path = Path(src_path)
        pattern = f"*.{suffix}"
        iterator = path.rglob(pattern) if is_recursion else path.glob(pattern)
        return [str(p) for p in iterator]

    @staticmethod
    def get_keyword_with_xml_label(src_path: str, is_recursion: bool = False) -> list[str]:
        raise NotImplementedError
