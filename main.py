"""Entry point — configure logging, read token, start polling."""

import logging
import sys

from bot.app import build_application
from bot.config import BOT_TOKEN


def configure_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        level=logging.INFO,
        stream=sys.stdout,
    )
    # Reduce noise from the library's internal HTTP layer
    logging.getLogger("httpx").setLevel(logging.WARNING)


def main() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting bot…")

    app = build_application(BOT_TOKEN)
    # run_polling blocks until the process is interrupted (Ctrl-C / SIGTERM)
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
