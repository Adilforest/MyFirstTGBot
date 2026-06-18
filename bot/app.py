"""Bot application factory: wire up all handlers and return the Application."""

import logging

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from bot.handlers.core import about, help_command, start
from bot.handlers.echo import echo
from bot.handlers.fun import menu, menu_callback, roll

logger = logging.getLogger(__name__)


def build_application(token: str) -> Application:
    """Create and configure the Application instance."""
    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("roll", roll))
    app.add_handler(CommandHandler("menu", menu))

    # Inline keyboard callbacks
    app.add_handler(CallbackQueryHandler(menu_callback))

    # Fallback: echo any non-command text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("All handlers registered")
    return app
