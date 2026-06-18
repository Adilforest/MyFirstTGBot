"""Fun commands: /roll (dice) and an inline keyboard menu."""

import logging
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

_SIDES = 6

# ── /roll ────────────────────────────────────────────────────────────────────


async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Roll a six-sided die and report the result."""
    result = random.randint(1, _SIDES)
    faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    logger.info(
        "User %s rolled %d",
        update.effective_user.id if update.effective_user else "?",
        result,
    )
    await update.message.reply_text(
        f"{faces[result - 1]}  You rolled a <b>{result}</b>!",
        parse_mode="HTML",
    )


# ── /menu (inline keyboard) ──────────────────────────────────────────────────


def _main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🎲 Roll a die", callback_data="roll"),
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
        ],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send an inline keyboard so the user can pick an action."""
    await update.message.reply_text(
        "Choose an option:", reply_markup=_main_menu_keyboard()
    )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses from the inline keyboard."""
    query = update.callback_query
    await query.answer()

    data = query.data
    logger.info(
        "Callback %r from user %s",
        data,
        update.effective_user.id if update.effective_user else "?",
    )

    if data == "roll":
        result = random.randint(1, _SIDES)
        faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        await query.edit_message_text(
            f"{faces[result - 1]}  You rolled a <b>{result}</b>!\n\n"
            "Press /menu to open the menu again.",
            parse_mode="HTML",
        )
    elif data == "about":
        await query.edit_message_text(
            "<b>MyFirstBot</b> — built with python-telegram-bot v21.\n"
            "Source: github.com/Adilforest/MyFirstTGBot\n\n"
            "Press /menu to go back.",
            parse_mode="HTML",
        )
    elif data == "help":
        await query.edit_message_text(
            "/start — welcome\n"
            "/help  — this list\n"
            "/about — about the bot\n"
            "/roll  — roll a die 🎲\n"
            "/menu  — this menu\n\n"
            "Or just send any text to echo it back.\n\n"
            "Press /menu to open the menu again."
        )
    else:
        await query.edit_message_text("Unknown option.")
