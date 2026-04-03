from pathlib import Path

from pathkit.process.reader import XMLReader


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
        """ 关键词查找对应的xml文件 """
        path = Path(src_path)
        iterator = path.rglob("*.xml") if is_recursion else path.glob("*.xml")
        target_path = []
        for xml_path in iterator:
            if key_word in XMLReader(xml_path).label_name:
                target_path.append(xml_path)
        return PathList(list(target_path))

pathkit = PathKit()
print(pathkit.get_keyword_with_xml_label(
    "/mnt/8T/TE/datasets/实车/download-2026-03-17_16-22-18/teds/转向架/车轮/PS_20260306_TEDS_车轮注油堵脱落_基于cat_CRH1A_23处/CHANGSHASUOHKJ_20250412232443_6_CRH1A-1101_1/xml",
    "dibuzxj__<lundui_lunpan>-<zyk>__diushi"
))