import os

DEBUG = True  # خليها True مؤقتًا علشان نعرف الخطأ

ALLOWED_HOSTS = ["*"]

# Logging عشان يظهر أي Exception في الـ console بتاع Vercel
import logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
