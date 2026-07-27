from src.config import create_directories, load_config


def main():

    print("Запуск AutoKeyUA")

    create_directories()

    config = load_config()

    print(
        f"{config['app_name']} v{config['version']}"
    )

    print(
        "Система готова"
    )


if __name__ == "__main__":
    main()