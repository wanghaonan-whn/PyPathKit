from pathlib import Path

from flatbuffers import encode

from pathkit.file_reader import FileReader


class PathList(list):
    def parent(self):
        parents = [p.parent if isinstance(p, Path) else Path(p).parent for p in self]
        parents = list(dict.fromkeys(parents))  # 保序去重
        return PathList(parents)

    def to_str(self) -> list[str]:
        return [str(p) for p in self]


class PathKit:
    @staticmethod
    def get_file_with_suffix(src_path: str, suffix: str, is_recursion: bool = False) -> PathList:
        """ 获取路径下匹配后缀的文件列表 """
        suffix = suffix.lstrip(".")
        path = Path(src_path)
        pattern = f"*.{suffix}"
        iterator = path.rglob(pattern) if is_recursion else path.glob(pattern)
        return PathList(list(iterator))

    @staticmethod
    def get_keyword_with_xml_label(src_path: str, key_word: str, is_recursion: bool = False) -> PathList:
        path = Path(src_path)
        iterator = path.rglob("*.xml") if is_recursion else path.glob("*.xml")
        target_path = []
        for xml_path in iterator:
            if key_word in FileReader(xml_path).label_name:
                target_path.append(xml_path)
        return PathList(list(target_path))

    @staticmethod
    def save_txt(data: list[str], save_path: str) -> None:
        with open(save_path, "w", encoding="utf-8") as f:
            f.writelines(f"\"{line}\"," + "\n" for line in data)
