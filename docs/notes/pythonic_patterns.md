## 8. PYTHONIC PATTERNS

- Use context managers (`with` statements) for resource management
- Prefer list/dict comprehensions over explicit loops (when readable)
- Use dataclasses or Pydantic models for structured data
- 🔴 FAIL: Getter/setter methods (this isn't Java)
- ✅ PASS: Properties with `@property` decorator when needed

## 9. IMPORT ORGANIZATION

- Follow PEP 8: stdlib, third-party, local imports
- Use absolute imports over relative imports
- Avoid wildcard imports (`from module import *`)
- 🔴 FAIL: Circular imports, mixed import styles
- ✅ PASS: Clean, organized imports with proper grouping

## 10. MODERN PYTHON FEATURES

- Use f-strings for string formatting (not % or .format())
- Leverage pattern matching (Python 3.10+) when appropriate
- Prefer `pathlib` over `os.path` for file operations