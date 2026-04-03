class FileWriter:
    @staticmethod
    def save_txt(data: list[str], save_path: str) -> None:
        with open(save_path, "w", encoding="utf-8") as f:
            f.writelines(f"\"{line}\"," + "\n" for line in data)
