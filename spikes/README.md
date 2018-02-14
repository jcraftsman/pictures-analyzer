# OCR based on tesseract library

## Synopsis

This spike describes the simplest implementation of optical character recognition based on tesseract. 

Find this implementation in `ocr.py`.

```python
from PIL import Image
from pytesseract import image_to_string

print(image_to_string(Image.open('cfp_accepted.png')))

```

## Usage
```bash
python ocr.py
```

## Prerequisites

### Tesseract binary

This ocr solution requires [tesseract library](https://github.com/tesseract-ocr).

[Tesseract](https://en.wikipedia.org/wiki/Tesseract_(software)) is a free software sponsored by Google.
It is considered to be one of the most accurate ocr engine to date.

To use it, it is necessary to install the binary on the target system.


For mac OS:
```bash
brew install tesseract
```
For linux ubuntu:
```bash
sudo apt-get install tesseract-ocr
```

/!\ Not recommended for windows!

Only an unofficial 32-bit installer is available.

See [tesseract documentation](https://github.com/tesseract-ocr/tesseract/wiki#windows), for installation instructions.

### pytesseract and pillow libraries
To interface your python program with tesseract, you need to install `pytesseract` and `pillow` libraries.

- Manual install:
```bash
pip install pytesseract
pip install pillow
```
- Declaring dependencies: 

Modify your `setup.py` file as follows:
```python
setup(
    install_requires=[
            'pillow',
            'pytesseract'
    ]
)
```
