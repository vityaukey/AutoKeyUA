from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backups"
LOG_DIR = BASE_DIR / "logs"

CONFIG_FILE = BASE_DIR / "config.json"


def create_directories():
    folders = [
        DATA_DIR,
        BACKUP_DIR,
        LOG_DIR,
    ]

    for folder in folders:
        folder.mkdir(
            exist_ok=True,
            parents=True
        )


def load_config():

    if not CONFIG_FILE.exists():

        config = {
            "app_name": "AutoKeyUA",
            "version": "0.1.0",
            "language": "uk-UA"
        }

        CONFIG_FILE.write_text(
            json.dumps(
                config,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

        return config

    return json.loads(
        CONFIG_FILE.read_text(
            encoding="utf-8"
        )
    )