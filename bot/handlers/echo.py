"""Echo handler: repeat any plain-text message back to the user."""

import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user's message back with a light acknowledgement prefix."""
    text = update.message.text or ""
    logger.debug(
        "Echo for user %s: %r",
        update.effective_user.id if update.effective_user else "?",
        text[:80],
    )
    await update.message.reply_text(f"You said: {text}")
