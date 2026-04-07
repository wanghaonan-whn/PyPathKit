# pathkit

pathkit is a lightweight path toolkit built on top of `pathlib`.

## Core Modules

- `PathEntry`: single path object wrapper
- `PathList`: path collection helper
- `PathUtils`: path scanning and filtering tools
- `process`: XML reader and file writer helpers

## PathEntry

`PathEntry` methods and properties:

- `join()`
- `joinpath()`
- `child()`
- `normalize()`
- `absolute()`
- `relative_to()`
- `relative_other()`
- `name`
- `dirname`
- `stem`
- `suffix`
- `suffixes`
- `parts`
- `parents`
- `with_suffix()`
- `with_name()`
- `is_absolute()`
- `common_path()`
- `matches()`
- `exists()`
- `is_file()`
- `is_dir()`
- `is_symlink()`
- `stat()`
- `as_posix()`
- `as_windows()`
- `as_uri()`
- `expanduser()`
- `samefile()`
- `drive`
- `anchor`

## PathList

`PathList` methods:

- `parent()`
- `to_str()`
- `counter_suffixes()`
- `suffix_list()`
- `filter_file()`
- `filter_dir()`
- `filter_exists()`
- `sort_by_name()`
- `sort_by_mtime()`
- `unique()`

## PathUtils

`PathUtils` methods:

- `iter_files()`
- `iter_dirs()`
- `glob_paths()`
- `rglob_paths()`
- `filter_name()`
- `get_file_paths_with_suffix()`
- `get_file_paths_with_suffixes()`
- `parse_file_with_suffix()`

## Process

`XMLReader` methods and properties:

- `read()`
- `get_root()`
- `find()`
- `findall()`
- `get_text()`
- `get_attr()`
- `label_name`

`FileWriter` methods:

- `save_txt()`

`AnnotationPathUtils` methods:

- `get_file_path_with_channel()`
- `get_keyword_with_xml_label()`

## Build Wheel

Install build tool:

```bash
python -m pip install build
```

Build wheel package in project root:

```bash
python -m build --wheel
```

After build completes, the wheel file will be generated in `dist/`.

## Error Rules

- query methods such as `exists()` return boolean values
- filesystem-dependent methods such as `stat()` and `samefile()` raise exceptions when paths do not exist
- `relative_to()` raises `ValueError` when the target path is not under the base path
- scanning methods default to `on_permission_error="skip"`
