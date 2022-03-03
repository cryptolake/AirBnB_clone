#!/usr/bin/python3
"""Models to represent everything from users to cities."""

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
