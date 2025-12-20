# API Documentation

## Main Application

**Script**: `password_combo_generator.py`

Generate case combinations and permutations of password strings.

### Usage

```bash
python password_combo_generator.py --password <password> [OPTIONS]
```

**Required Arguments**:
- `--password <string>`: Password to generate combinations for

**Options**:
- `--output_file <path>`: Output file path (default: passwords.txt)
- `--verbose`: Enable verbose logging
- `--logfile <path>`: Log file path (default: password_combo_generator.log)
- `--version`: Display version information

**Examples**:
```bash
# Basic usage
python password_combo_generator.py --password "MyPass123"

# Custom output file
python password_combo_generator.py --password "Test" --output_file results.txt

# Verbose logging
python password_combo_generator.py --password "Secret" --verbose
```

## Generation Algorithms

### Case Combinations

Generates all possible case variations of alphabetic characters.

**Example**:
- Input: "abc"
- Output: abc, Abc, aBc, abC, ABc, AbC, aBC, ABC

**Complexity**: O(2^n) where n = number of letters

### Permutations

Generates all character rearrangements.

**Example**:
- Input: "abc"
- Output: abc, acb, bac, bca, cab, cba

**Complexity**: O(n!) where n = string length

### Combined Output

The tool combines both algorithms:
1. Generate case combinations
2. For each combination, generate permutations
3. Remove duplicates
4. Write unique results to file

## Output Format

Plain text file with one password variation per line:
```
Password1
password1
PASSWORD1
Pass1word
...
```

## Logging

### Log Levels

- **INFO**: Progress updates, statistics (verbose mode)
- **WARNING**: Non-critical issues
- **ERROR**: Failures and exceptions

### Log Rotation

- Max file size: 1 MB
- Backup count: 3 files
- Auto-rotation on size limit

## Performance Considerations

### Result Set Size

Password length affects output size:
- 4 characters: ~24-576 combinations
- 6 characters: ~720-46,656 combinations
- 8 characters: ~40,320-16,777,216 combinations

### Memory Usage

- Deduplication uses set storage
- Large passwords consume significant memory
- Consider batch processing for long passwords

### Execution Time

Scales exponentially with password length:
- Short passwords (4-6 chars): Seconds
- Medium passwords (7-8 chars): Minutes
- Long passwords (9+ chars): Hours or more

## Warning

This tool can generate extremely large result sets. Use with caution:
- Start with short passwords for testing
- Monitor disk space and memory
- Use for authorized security testing only

## Return Codes

- `0`: Success
- `1`: Invalid arguments
- `2`: Output file error
- `3`: Generation error

---
Author: Kris Armstrong
