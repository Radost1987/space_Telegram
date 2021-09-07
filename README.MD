# Space Telegram

This script downloads images of latest SpaceX launcher by using  [SpaceX API Docs](https://docs.spacexdata.com) and images from [https://www.nasa.gov](https://www.nasa.gov). Then publishing the images in the Telegram chat every day.

### How to install

* Python3 should be already installed.

<<<<<<< Updated upstream
* Then create and active a virtual environment, and install all the dependencies:

```bash
=======
* Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
>>>>>>> Stashed changes
pip install -r requiments.txt
```

* Then you should sign up for a [NASA developer key](https://api.nasa.gov/#apod)

* You should be registered in the [Telegram](https://telegram.org). Create a bot there [https://telegram.me/BotFather](https://telegram.me/BotFather) and get its API token. Also you need your own Telegram channel and its chat id (chat_id is a link to it). Make the bot a channel administrator.

* Put NASA developer key, Telegram API token and  Telegram channel's chat id in file `.env` to folder with script like this:
```
NASA_API_KEY=lcCXd3eic8FgtIM
TELEGRAM_TOKEN=1975642396:AAGyWOXky56
TELEGRAM_CHAT_ID=-1111111111111
```

* Run the script in a terminal
```bash
python3 main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
