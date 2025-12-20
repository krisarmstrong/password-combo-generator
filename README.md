# Password Combo Generator

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green)

Generate case combinations and permutations of a password string for authorized security testing.

## Requirements

- Python 3.11+

## Install

```bash
git clone https://github.com/krisarmstrong/password-combo-generator
cd password-combo-generator
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python src/password_combo_generator.py --password "MyPass123" --output_file passwords.txt --verbose
```

Arguments:

- `--password` (required): Password to generate combinations and permutations for.
- `--output_file`: Output file for generated passwords (default: `passwords.txt`).
- `-v`, `--verbose`: Enable verbose logging.
- `--logfile`: Log file path (default: `password_combo_generator.log`).
- `--version`: Display version.

## Project Structure

- `src/password_combo_generator.py` — Main script.
- `tests/` — Pytest suite.
- `CHANGELOG.md` — Version history.
- `LICENSE` — MIT License.

## License

MIT. See `LICENSE` for details.
