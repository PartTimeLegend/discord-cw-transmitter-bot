# Discord CW Transmitter Bot

This is a Discord bot that allows users with a specific role to transmit messages in CW (Continuous Wave) format via an ICOM IC-7300 radio.

## Features
- Transmits messages in CW via an ICOM IC-7300 radio.
- Users with a specific role ("tx") can use the command `!tx <frequency> <message>` to transmit messages.
- Messages are stored in a MariaDB database for logging and auditing purposes.

## Dependencies
- [discord.py](https://pypi.org/project/discord.py/): Python library for Discord bot development.
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/): MySQL driver for Python.
- [pyserial](https://pypi.org/project/pyserial/): Python library for accessing serial ports.

## Configuration
Before running the bot, make sure to set up the following configurations:
- Create a `config.ini` file with the database and Discord bot token configurations.
- Ensure the MariaDB server is running and accessible.
- Connect the ICOM IC-7300 radio to the computer via USB.

## Usage
1. Install dependencies using `pip install -r requirements.txt`.
2. Configure the `config.ini` file with the appropriate database and Discord bot token.
3. Connect the ICOM IC-7300 radio to the computer via USB.
4. Run the bot using `python main.py`.
5. Users with the "tx" role can now use the `!tx <frequency> <message>` command to transmit messages.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
