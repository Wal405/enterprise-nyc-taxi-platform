from pathlib import Path


ROOT = Path(__file__).resolve().parent

STRUCTURE = {
    "synapse": [
        "linkedService",
        "dataset",
        "pipeline",
        "notebook",
        "sqlscript",
        "trigger"
    ],
    "config": [
        "environments",
        "datasets",
        "schemas",
        "quality_rules"
    ],
    "src": [
        "nyctaxi"
    ],
    "infrastructure": [
        "modules",
        "parameters"
    ],
    "tests": [
        "unit",
        "integration"
    ],
    "docs": [
        "architecture",
        "data_dictionary",
        "runbooks"
    ],
    ".github": [
        "workflows"
    ]
}


def create_repository_structure(root, structure):
    """Create the repository directory structure safely."""

    for parent, subdirectories in structure.items():

        for subdirectory in subdirectories:

            directory = root / parent / subdirectory

            directory.mkdir(
                parents=True,
                exist_ok=True
            )

            if not any(directory.iterdir()):
                (directory / ".gitkeep").touch(
                    exist_ok=True
                )

            print(f"PASS: {directory.relative_to(root)}")


def create_root_files(root):
    """Create missing project files without overwriting."""

    files = [
        "README.md",
        ".gitignore",
        "src/nyctaxi/__init__.py"
    ]

    for filename in files:

        path = root / filename

        if not path.exists():
            path.touch()

        print(f"PASS: {filename}")


def main():

    create_repository_structure(ROOT, STRUCTURE)

    create_root_files(ROOT)

    print("\nRepository structure created successfully.")


if __name__ == "__main__":
    main()
