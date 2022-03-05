#!/usr/bin/python3
"""Represent Review."""

from .base_model import BaseModel


class Review(BaseModel):
    """Represent Review."""

    place_id = ""
    user_id = ""
    text = ""
