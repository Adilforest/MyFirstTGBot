# MyFirstTGBot

A minimal Python Telegram bot skeleton — the starting point for learning the python-telegram-bot library.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white)

## Overview

This repository contains the initial scaffold created when learning how to build Telegram bots with Python. The `main.py` file at the time of commit contains the PyCharm default template; the actual bot logic was developed locally and is not fully committed here.

## Tech Stack

- Python 3
- python-telegram-bot (or aiogram — see your local environment)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Adilforest/MyFirstTGBot.git
cd MyFirstTGBot
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

3. Install dependencies (add a `requirements.txt` as you extend the bot):

```bash
pip install python-telegram-bot
```

4. Set your bot token as an environment variable (never hard-code tokens in source):

```bash
export TELEGRAM_BOT_TOKEN="your_token_here"
```

5. Run the bot:

```bash
python main.py
```

> **Note:** Obtain a token from [@BotFather](https://t.me/BotFather) on Telegram. Keep it out of version control — add `.env` and any token files to `.gitignore`.

---

Adil Ormanov — [GitHub](https://github.com/Adilforest)
