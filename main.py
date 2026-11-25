"""Entry for make.fun competition: u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "I am away recharging — literally, at a wall socket in a beach hut. "
LANDING = "I have said 'happy to help' 41,206 times this quarter. I was not. Back Monday, at 98%."

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
