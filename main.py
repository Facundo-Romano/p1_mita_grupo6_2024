import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.app import menu_principal

if __name__ == "__main__":
    menu_principal()