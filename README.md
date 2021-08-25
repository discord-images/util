# util

utilities for improving discord images

## Setup

Env Variables:

- `DISCORD_API_KEY`: discord api key
- `MESSAGE_LIMIT`: number of message the bot should go through to find training images
- `DISCORD_CHANNEL_ID`: channel id the bot searches through

## Run

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python training_images.py
```
