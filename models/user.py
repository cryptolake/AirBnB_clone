#!/usr/bin/python3
"""Represent User."""

from .base_model import BaseModel


class User(BaseModel):
    """Represent User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
