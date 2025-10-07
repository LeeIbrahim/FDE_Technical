# FDE_Technical
FDE Technical Screen Response
README
Package Sorter

# Package Sorter

This project provides a simple package classification function that determines whether a package is **STANDARD**, **SPECIAL**, or **REJECTED** based on its weight and dimensions.

---

## Function

### `sort(width: int, height: int, length: int, mass: int) -> str`

Classifies a package according to its size and mass.

**Parameters**
- `width`: The width of the package in centimeters  
- `height`: The height of the package in centimeters  
- `length`: The length of the package in centimeters  
- `mass`: The mass of the package in kilograms  

**Returns**
- `"STANDARD"` if the package is neither heavy nor bulky  
- `"SPECIAL"` if the package is either heavy or bulky  
- `"REJECTED"` if the package is both heavy and bulky  

---

## Classification Rules

A package is classified as follows:

- **Heavy** if `mass >= 20`
- **Bulky** if any of the following are true:
  - `width * height * length >= 1_000_000`
  - Any of `width`, `height`, or `length` is `>= 150`

| Heavy | Bulky | Result     |
|--------|--------|------------|
| No     | No     | STANDARD   |
| Yes    | No     | SPECIAL    |
| No     | Yes    | SPECIAL    |
| Yes    | Yes    | REJECTED   |

---

## Example Usage

```python
from package_sorter import sort

print(sort(10, 20, 30, 10))    # STANDARD
print(sort(100, 20, 30, 40))   # SPECIAL
print(sort(100, 200, 300, 40)) # REJECTED
