from typing import TYPE_CHECKING

__all__ = ["AnnotationPathUtils", "XMLDocument"]

if TYPE_CHECKING:
    from pathkit.process.annotation import AnnotationPathUtils
    from pathkit.process.xmldocument import XMLDocument


def __getattr__(name: str):
    if name == "AnnotationPathUtils":
        from pathkit.process.annotation import AnnotationPathUtils

        return AnnotationPathUtils
    if name == "XMLDocument":
        from pathkit.process.xmldocument import XMLDocument

        return XMLDocument
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
