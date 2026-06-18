"""Core command handlers: /start, /help, /about."""

import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

_HELP_TEXT = (
    "Here is what I can do:\n\n"
    "/start — welcome message\n"
    "/help  — show this help\n"
    "/about — info about this bot\n"
    "/roll  — roll a six-sided die 🎲\n"
    "/menu  — open an inline keyboard menu\n\n"
    "Or just send me any text and I will echo it back."
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greet the user and give a quick overview."""
    user = update.effective_user
    first_name = user.first_name if user else "there"
    logger.info("User %s triggered /start", user.id if user else "unknown")
    await update.message.reply_html(
        f"👋 Hi, <b>{first_name}</b>! I am <b>MyFirstBot</b>.\n\n"
        "Type /help to see everything I can do."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the help text."""
    await update.message.reply_text(_HELP_TEXT)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Describe the bot."""
    await update.message.reply_html(
        "<b>MyFirstBot</b>\n\n"
        "A small Telegram bot built with <a href='https://python-telegram-bot.org'>"
        "python-telegram-bot</a> v21 (async).\n\n"
        "Source: github.com/Adilforest/MyFirstTGBot"
    )
