import os
import sys

if 'install' not in sys.argv and 'egg_info' not in sys.argv:
    from .chatterbot import ChatBot



