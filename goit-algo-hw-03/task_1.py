import sys
from pathlib import Path
import shutil


def process_directory(source: Path, destination: Path):
    """
    Recursively traverse the source directory and copy each file into a subdirectory
    in the destination directory, named by file extension.
    """
    try:
        for item in source.iterdir():
            if item.is_dir():
                process_directory(item, destination)
            elif item.is_file():
                extension = item.suffix.lower().lstrip('.') or 'no_extension'
                ext_dir = destination / extension
                ext_dir.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy2(item, ext_dir / item.name)
                    print(f"Copied: {item} -> {ext_dir}")
                except (OSError, PermissionError) as e:
                    print(f"Failed to copy {item}: {e}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error accessing directory {source}: {e}")


def main():
    """
    Entry point. Requires 1 or 2 command-line arguments:
    - source directory (required)
    - destination directory (optional, defaults to 'dist')
    """
    if len(sys.argv) < 2:
        print("Usage: python task_1.py <source_directory> [destination_directory]")
        sys.exit(1)

    source = Path(sys.argv[1]).resolve()
    destination = Path(sys.argv[2]).resolve() if len(sys.argv) >= 3 else Path("dist").resolve()

    if not source.exists() or not source.is_dir():
        print(f"Error: Source directory '{source}' does not exist or is not a directory.")
        sys.exit(1)

    destination.mkdir(parents=True, exist_ok=True)

    print(f"Source directory: {source}")
    print(f"Destination directory: {destination}")

    process_directory(source, destination)
    print("File copying and sorting completed.")


if __name__ == "__main__":
    main()
