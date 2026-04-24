import pytest

from main import show_supported_platforms


def test_show_supported() -> None:
    with pytest.raises(Exception):
        show_supported_platforms()
