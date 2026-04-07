# pathkit

pathkit is a lightweight path toolkit built on top of `pathlib`.

## Core Modules

- `PathEntry`: single path object wrapper
- `PathList`: path collection helper
- `PathUtils`: path scanning and filtering tools
- `process`: XML reader and file writer helpers

## PathEntry

```python
from pathkit import PathEntry

root = PathEntry("data")
file_path = root.child("images", "cat.jpg")

print(file_path.exists())
print(file_path.name)
print(file_path.as_posix())
print(file_path.relative_to("data"))
```

## PathList

```python
from pathlib import Path

from pathkit import PathList

paths = PathList([Path("a.txt"), Path("b.txt"), Path("folder")])

print(paths.filter_file())
print(paths.filter_exists())
print(paths.sort_by_name())
```

## PathUtils

```python
from pathkit import PathUtils

print(PathUtils.iter_files("data"))
print(PathUtils.glob_paths("data", "*.txt"))
print(PathUtils.filter_name("data", "cat"))
print(PathUtils.get_file_paths_with_suffixes("data", ["jpg", "png", "xml", "json"]))
print(PathUtils.parse_file_with_suffix("data", include_empty=True))
```

## Process

```python
from pathkit.process import XMLReader, FileWriter, AnnotationPathUtils

xml_reader = XMLReader("example.xml")
print(xml_reader.get_root())

FileWriter.save_txt(["cat", "dog"], "labels.txt")
print(AnnotationPathUtils.get_keyword_with_xml_label("annotations", "cat"))
```

## Error Rules

- query methods such as `exists()` return boolean values
- filesystem-dependent methods such as `stat()` and `samefile()` raise exceptions when paths do not exist
- `relative_to()` raises `ValueError` when the target path is not under the base path
- scanning methods default to `on_permission_error="skip"`
