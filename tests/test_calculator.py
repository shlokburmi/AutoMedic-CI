import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import add

def test_add():
    assert add(2, 3) == 5