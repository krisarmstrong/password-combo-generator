# Contributing to Password Combo Generator

## Welcome

Thank you for your interest in contributing to Password Combo Generator!

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip package manager
- Git

### Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Development Workflow

### Making Changes

1. Create a new branch for your feature or fix
2. Make your changes in the `src/` directory
3. Add or update tests in `tests/`
4. Test thoroughly with various password lengths
5. Update documentation as needed
6. Commit with clear, descriptive messages

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints where applicable
- Write docstrings for functions
- Optimize for memory efficiency
- Consider performance implications

### Testing

Run the test suite:
```bash
python -m pytest tests/
```

Test with sample passwords:
```bash
# Short password (fast)
python src/password_combo_generator.py --password "test" --verbose

# Medium password (moderate time)
python src/password_combo_generator.py --password "Pass123" --verbose
```

### Performance Testing

Test with various password lengths:
- Short (4-5 characters)
- Medium (6-7 characters)
- Long (8+ characters) - use with caution

Monitor:
- Execution time
- Memory usage
- Output file size
- CPU utilization

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Test performance impact
4. Update CHANGELOG
5. Submit PR with clear description

## Security Considerations

This tool is for authorized security testing only. Contributors should:
- Include appropriate warnings in documentation
- Consider rate limiting for API versions
- Document responsible use cases
- Avoid malicious feature additions

## Questions?

Feel free to open an issue for questions or discussions.

---
Author: Kris Armstrong
