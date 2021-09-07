# Space Telegram

This script downloads images of latest SpaceX launcher by using  [SpaceX API Docs](https://docs.spacexdata.com) and images from [https://www.nasa.gov](https://www.nasa.gov). Then publishing the images in the Telegram chat every day.

### How to install

* Python3 should be already installed.

* Then create a virtual environment, and install all the dependencies:

```bash
pip install -r requirents.txt
```

* Then you should sign up for a [NASA developer key](https://api.nasa.gov/#apod)

* You should be registered in the Telegram. Create a bot there and get its API token. Also you need your own Telegram channel and its chat id (chat_id is a link to it). Make the bot a channel administrator

* Put them in file `.env` to folder with script like this:
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
