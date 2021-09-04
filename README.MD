# Space Telegram

This script downloads images of latest SpaceX launcher by using  [SpaceX API Docs](https://docs.spacexdata.com) and images from [https://www.nasa.gov](https://www.nasa.gov). Then publishing the images in the Telegram chat every day.

### How to install

* Python3 should be already installed.

* Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
* Then you should sign up for a [NASA developer key](https://api.nasa.gov/#apod)

* You should be registered in the Telegram. Create a bot there and get its API token

* Put them in file `.env` to folder with script like this:
```
NASA_API_KEY=lcCXd3eic8FgtIM
TELEGRAM_TOKEN=1975642396:AAGyWOXky56
```
* Run the script in a terminal
```
python3 main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
