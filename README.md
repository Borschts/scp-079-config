# SCP-079-CONFIG

This bot is used to manage settings for each bot.

## How to use

- See [this article](https://scp-079.org/config/) to build a bot by yourself
- Discuss [group](https://t.me/SCP_079_CHAT)

## To Do List

- [x] Support SCP-079-CAPTCHA
- [x] Support SCP-079-CLEAN
- [x] Support SCP-079-LANG
- [x] Support SCP-079-LONG
- [x] Support SCP-079-NOFLOOD
- [x] Support SCP-079-NOPORN
- [x] Support SCP-079-NOSPAM
- [x] Support SCP-079-TIP
- [x] Support SCP-079-USER
- [x] Support SCP-079-WARN
- [x] Support SCP-079-RECHECK

## Requirements

- Python 3.6 or higher
- pip: `pip install -r requirements.txt` or `pip install -U APScheduler pyAesCrypt pyrogram[fast]`

## Files

- plugins
    - functions
        - `channel.py` : Functions about channel
        - `config.py` : Generate config session message
        - `etc.py` : Miscellaneous
        - `filters.py` : Some filters
        - `receive.py` : Receive data from exchange channel
        - `telegram.py` : Some telegram functions
        - `timers.py` : Timer functions
    - handlers
        - `callback.py` : Handle callbacks
        - `command` : Handle commands
        - `message.py`: Handle messages
    - `glovar.py` : Global variables
- `.gitignore` : Ignore
- `config.ini.example` -> `config.ini` : Configuration
- `LICENSE` : GPLv3
- `main.py` : Start here
- `README.md` : This file
- `requirements.txt` : Managed by pip

## Contribute

Welcome to make this project even better. You can submit merge requests, or report issues.

## License

Licensed under the terms of the [GNU General Public License v3](LICENSE).
