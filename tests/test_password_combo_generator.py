#!/usr/bin/env python3
"""
Tests for PasswordComboGenerator.
"""

import pytest

from password_combo_generator import (
    Config,
    __version__,
    generate_combinations,
    generate_permutations,
    save_passwords,
)


@pytest.fixture
def tmp_output_file(tmp_path):
    """Create a temporary output file path."""
    return tmp_path / "passwords.txt"


def test_version() -> None:
    """Test version format."""
    assert __version__ == "1.0.1"


def test_generate_combinations():
    """Test generating case combinations."""
    password = "ab1"
    combos = generate_combinations(password)
    expected = ["ab1", "Ab1", "aB1", "AB1"]
    assert sorted(combos) == sorted(expected)


def test_generate_permutations():
    """Test generating permutations of combinations."""
    combos = ["ab1", "Ab1"]
    perms = generate_permutations(combos)
    expected = {
        "ab1",
        "a1b",
        "ba1",
        "b1a",
        "1ab",
        "1ba",
        "Ab1",
        "A1b",
        "bA1",
        "b1A",
        "1Ab",
        "1bA",
    }
    assert perms == expected


def test_save_passwords(tmp_output_file):
    """Test saving passwords to a file."""
    passwords = {"ab1", "Ab1", "1ba"}
    save_passwords(passwords, str(tmp_output_file))
    with open(tmp_output_file, "r", encoding=Config.ENCODING) as f:
        content = f.read().strip().split("\n")
    assert sorted(content) == ["1ba", "Ab1", "ab1"]


def test_save_passwords_permission_denied(tmp_path, monkeypatch):
    """Test saving passwords with permission denied."""
    tmp_file = tmp_path / "noperm.txt"
    tmp_file.touch()

    def mock_open(*args, **kwargs):
        raise PermissionError("Permission denied")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(PermissionError):
        save_passwords({"ab1"}, str(tmp_file))
