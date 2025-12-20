# Architecture

## Overview

Password Combo Generator is a Python-based tool for generating all possible case combinations and permutations of password strings. It's designed for security testing and password complexity analysis.

## System Architecture

### Core Components

1. **Main Generator** (`password_combo_generator.py`)
   - Case combination generation
   - Character permutation logic
   - Duplicate detection and removal
   - Output file management
   - Logging system

### Technical Implementation

#### Case Combination Algorithm

Generates all case variations:
- Identifies alphabetic characters
- Creates 2^n combinations (n = number of letters)
- Maintains character positions
- Preserves non-alphabetic characters

#### Permutation Algorithm

Creates character rearrangements:
- Full permutation generation
- Position swapping
- Factorial complexity (n!)
- Memory-efficient processing

#### Duplicate Removal

Ensures unique outputs:
- Set-based deduplication
- Hash-based comparison
- Memory optimization
- Efficient filtering

### Data Flow

```
Input Password → Case Combinations → Permutations → Deduplication → Output File
                          ↓
                  Progress Tracking
                          ↓
                    Logging System
```

### Logging System

Multi-level logging with rotation:
- Rotating file handler (1MB limit)
- Backup count (3 files)
- Configurable verbosity
- Progress indication
- Statistics tracking

## Performance Characteristics

### Complexity

- Case combinations: O(2^n) where n = letter count
- Permutations: O(n!) where n = string length
- Combined: Exponential growth with password length

### Optimization Techniques

1. **Set-based deduplication**: O(1) lookup
2. **Generator patterns**: Memory-efficient iteration
3. **Batch writing**: Reduced I/O operations
4. **Progress tracking**: User feedback for long operations

## Design Principles

1. **Security Focus**: Designed for authorized testing
2. **Efficiency**: Optimized for large result sets
3. **Usability**: Clear CLI interface
4. **Observability**: Comprehensive logging

---
Author: Kris Armstrong
