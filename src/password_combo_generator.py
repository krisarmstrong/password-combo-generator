#!/usr/bin/env python3
"""
Project Title: PasswordComboGenerator

Generates all case combinations and permutations of a password, saving results to an output file.

Author: Kris Armstrong
"""
import argparse
import logging
import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version
from itertools import permutations, product
from logging.handlers import RotatingFileHandler
from pathlib import Path


def _find_pyproject(start: Path) -> Path | None:
    for parent in (start, *start.parents):
        candidate = parent / "pyproject.toml"
        if candidate.is_file():
            return candidate
    return None


def _read_pyproject_version() -> str:
    try:
        import tomllib  # Python 3.11+
    except ModuleNotFoundError:
        return "0.0.0"

    pyproject = _find_pyproject(Path(__file__).resolve())
    if not pyproject:
        return "0.0.0"
    try:
        data = tomllib.loads(pyproject.read_text())
    except Exception:
        return "0.0.0"
    return data.get("project", {}).get("version", "0.0.0")


_pyproject_version = _read_pyproject_version()
if _pyproject_version != "0.0.0":
    __version__ = _pyproject_version
else:
    try:
        __version__ = _pkg_version("password-combo-generator")
    except PackageNotFoundError:
        __version__ = "0.0.0"


class Config:
    """Global constants for PasswordComboGenerator."""

    LOG_FILE: str = "password_combo_generator.log"
    ENCODING: str = "utf-8"


def setup_logging(verbose: bool, logfile: str = Config.LOG_FILE) -> None:
    """Configure logging with rotating file handler.

    Args:
        verbose: Enable DEBUG level logging if True.
        logfile: Path to log file.

    Raises:
        PermissionError: If log file cannot be written.
    """
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(logfile, maxBytes=1048576, backupCount=3),
            logging.StreamHandler(),
        ],
    )


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed arguments.

    Raises:
        SystemExit: If arguments are invalid.
    """
    parser = argparse.ArgumentParser(
        description="Generate password case combinations and permutations.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--password",
        required=True,
        help="Password to generate combinations and permutations for",
    )
    parser.add_argument(
        "--output_file",
        default="passwords.txt",
        help="Output file for generated passwords",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--logfile", default=Config.LOG_FILE, help="Log file path")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser.parse_args()


def generate_combinations(password: str) -> list[str]:
    """Generate all combinations of upper and lower case for the letters.

    Args:
        password: Input password string.

    Returns:
        List of all case combinations.
    """
    chars = [(char.lower(), char.upper()) if char.isalpha() else (char,) for char in password]
    return ["".join(combination) for combination in product(*chars)]


def generate_permutations(combinations: list[str]) -> set[str]:
    """Generate all permutations of each combination.

    Args:
        combinations: List of case combinations.

    Returns:
        Set of unique permuted passwords.
    """
    permuted_passwords: set[str] = set()
    for combination in combinations:
        perms = permutations(combination)
        for perm in perms:
            permuted_passwords.add("".join(perm))
    return permuted_passwords


def save_passwords(passwords: set[str], output_file: str) -> None:
    """Save generated passwords to the output file.

    Args:
        passwords: Set of generated passwords.
        output_file: Path to output file.

    Raises:
        PermissionError: If output file cannot be written.
        IOError: If file write operation fails.
    """
    logging.info("Saving %d passwords to %s", len(passwords), output_file)
    try:
        with open(output_file, "w", encoding=Config.ENCODING) as f:
            for password in sorted(passwords):
                f.write(password + "\n")
        logging.info("Successfully wrote passwords to %s", output_file)
    except PermissionError as e:
        logging.error("Cannot write to output file %s: %s", output_file, e)
        raise
    except OSError as e:
        logging.error("Error writing to output file %s: %s", output_file, e)
        raise


def main() -> int:
    """Main entry point for PasswordComboGenerator.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    args = parse_args()
    setup_logging(args.verbose, args.logfile)

    # Validate password
    if not args.password:
        logging.error("Password cannot be empty")
        print("Error: Password cannot be empty")
        return 1

    try:
        combinations = generate_combinations(args.password)
        logging.debug("Generated %d case combinations", len(combinations))
        permutations_set = generate_permutations(combinations)
        logging.debug("Generated %d unique permutations", len(permutations_set))
        save_passwords(permutations_set, args.output_file)
        print(f"Generated {len(permutations_set)} passwords, saved to {args.output_file}")
        return 0
    except KeyboardInterrupt:
        logging.info("Cancelled by user")
        print("Cancelled by user")
        return 0
    except Exception as e:
        logging.error("Error: %s", e)
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
