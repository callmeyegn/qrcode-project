# QR Code Project

Generate and decode QR codes with Python.

## Install

```
pip install "qrcode[pil]"
pip install pyzbar Pillow
```

## Files

- `simple_qr.py` - simplest way to make a QR code (saves `simple_qr.png`)
- `generate_qr.py` - QR code with custom settings (saves `generated_qrcodes/wikipedia_qr.png`)
- `decode_qr.py` - reads a QR code image and prints the link inside it

## Run

```
python simple_qr.py
python generate_qr.py
python decode_qr.py
```

The test link in this version is https://www.wikipedia.org
