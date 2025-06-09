# NulizArt

This repository provides a simple command line tool to estimate service costs and optionally generate an invoice.

## Usage

```
python price_calculator.py SERVICE [--addons ADDON [ADDON ...]] [--invoice PATH]
```

- `SERVICE` – one of the supported services listed in the script.
- `--addons` – optional list of add-on names.
- `--invoice` – if provided, saves a receipt-style invoice to the given path. The extension `.txt` writes a plain text file and `.pdf` writes a PDF file.

Each quote receives a unique ID. The generated invoice includes selected services, chosen add-ons, total price, the quote ID, and a booking link to schedule a free meeting.

Example:

```
python price_calculator.py logo --addons source-files extra-revision --invoice myquote.pdf
```
