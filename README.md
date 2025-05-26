# Unitz

A simple and test-friendly unit conversion library for Python 🧪📏

## Features

- ✅ Convert between metric and imperial units
- ✅ Handle unit aliases like "m", "km", "lbs"
- ✅ Easy to expand with more units and categories
- ✅ Great for practicing unit testing and CI workflows

## Install

```bash
pip install unitz
```

## Usage

```python
from unitz.converter import convert

meters = convert(10, "foot", "meter")  # 3.048
```

## Supported Categories

- Length: meters, feet, inches, kilometers, miles
- Mass: grams, kilograms, pounds, ounces

## Contributing

Contributions are welcome! Submit a pull request or open an issue.

## License

MIT