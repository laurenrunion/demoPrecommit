import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app import add


def test_add():
    assert add(2, 2) == 4, "Expected add(2, 2) to equal 4"
    assert add(0, 0) == 0, "Expected add(0, 0) to equal 0"
    print("All tests passed!")


if __name__ == "__main__":
    try:
        test_add()
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
