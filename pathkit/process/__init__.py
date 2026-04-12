from typing import TYPE_CHECKING

__all__ = ["AnnotationPathUtils", "XMLReader", "FileWriter"]

if TYPE_CHECKING:
    from pathkit.process.annotation import AnnotationPathUtils
    from pathkit.process.writer import FileWriter
    from pathkit.process.xmlreader import XMLReader


def __getattr__(name: str):
    if name == "AnnotationPathUtils":
        from pathkit.process.annotation import AnnotationPathUtils

        return AnnotationPathUtils
    if name == "XMLReader":
        from pathkit.process.xmlreader import XMLReader

        return XMLReader
    if name == "FileWriter":
        from pathkit.process.writer import FileWriter

        return FileWriter
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
