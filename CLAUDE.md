# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Run all tests:
```
pytest
```

Run a single test function:
```
pytest test_utils.py::test_greet
```

## Architecture

Small Python utility library with two files:

- [utils.py](utils.py) — Pure functions (`greet`, `add`) with no dependencies.
- [test_utils.py](test_utils.py) — pytest tests for those functions, imported directly from `utils`.

No build step, no external dependencies beyond pytest.
