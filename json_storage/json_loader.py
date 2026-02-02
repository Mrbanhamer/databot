import json
from pathlib import Path

JSON_PATH = Path(__file__).parent / "posts.json"

def save_titles(titles: list[str]) -> None:
    JSON_PATH.write_text(
        json.dumps(titles, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )