from random import uniform
from os import remove, path

busher_logo = """
██████╗░██╗░░░██╗░██████╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░██║██╔════╝██║░░██║██╔════╝██╔══██╗
██████╦╝██║░░░██║╚█████╗░███████║█████╗░░██████╔╝
██╔══██╗██║░░░██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗
██████╦╝╚██████╔╝██████╔╝██║░░██║███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

social_links = """
Telegram channel: @CryptoKiddiesClub
Telegram chat: @CryptoKiddiesChat
Twitter: @CryptoBusher
"""


def remove_line(file_path: str, line_to_remove: str):
    with open(file_path, "r", encoding='utf-8') as _file:
        lines = [i.strip() for i in _file]

    with open(file_path, "w", encoding='utf-8') as _file:
        for line in lines:
            if line != line_to_remove:
                _file.write(line + '\n')


def probability_check_is_positive(probability: int | float) -> bool:
    return True if uniform(0, 1) < probability else False


def remove_files(rel_paths: list) -> None:
    for file_path in rel_paths:
        if path.exists(file_path):
            remove(file_path)
