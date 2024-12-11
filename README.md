# Sia

Sia serialization for Python

## What is Sia?

Sia is the serialization library used by [Unchained](https://github.com/TimeleapLabs/unchained). Check more details on [Sia's official documentation](https://timeleap.swiss/docs/products/sia).

## Installation

```bash
pip install sia
```

## Usage

```python
from sia import Sia

sia = Sia()
sia.add_string8("Hello")
sia.add_uint8(25)
sia.add_ascii("World")

print(sia.content)
```
