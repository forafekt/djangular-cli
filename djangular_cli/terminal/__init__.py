# -*- coding: utf-8 -*-

import os

from .utils import print_json, format_json
from .separator import Separator
from .prompts.common import default_style
from pygments.token import Token
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style


def here(p):
    """

    :param p:
    :return:
    """
    # TODO: Is this being used externally or deprecate?
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class PromptParameterException(ValueError):
    """
    prompt exception
    """

    def __init__(self, message, errors=None):
        # Call the base class constructor with the parameters it needs
        super().__init__('You must provide a `%s` value' % message, errors)


# The code below here is here because of backwards-compatibility. Before,
# people were using style_from_dict and importing it from here. It's better to
# use Style.from_dict, as recommended by prompt_toolkit now.


def style_from_dict(style_dict):
    """

    :param style_dict:
    :return:
    """
    # Deprecated function. Users should use Style.from_dict instead.
    # Keep this here for backwards-compatibility.
    return Style.from_dict({
        '.'.join(key).lower(): value for key, value in style_dict.items()
    })


__all__ = ["PromptParameterException", "style_from_dict", "Token", "Validator", "ValidationError"]
