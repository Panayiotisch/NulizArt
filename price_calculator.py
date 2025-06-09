#!/usr/bin/env python3
"""Simple price calculator for NulizArt services."""

import argparse
import uuid
import os
from typing import List

# Predefined services and their prices
SERVICES = {
    "logo": 100.0,
    "full-illustration": 200.0,
    "concept-art": 150.0,
}

# Predefined add-ons and their prices
ADDONS = {
    "source-files": 30.0,
    "extra-revision": 20.0,
    "commercial-use": 50.0,
}

BOOKING_LINK = "https://example.com/free-meeting"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate service price.")
    parser.add_argument("service", choices=SERVICES.keys(), help="Service name")
    parser.add_argument(
        "--addons",
        nargs="*",
        choices=ADDONS.keys(),
        default=[],
        help="Optional add-ons",
    )
    parser.add_argument(
        "--invoice",
        metavar="PATH",
        help="Save the invoice to the given path (txt or pdf)",
    )
    return parser.parse_args()


def calculate_total(service: str, addons: List[str]) -> float:
    price = SERVICES[service]
    for addon in addons:
        price += ADDONS[addon]
    return price


def build_invoice(service: str, addons: List[str], total: float, quote_id: str) -> str:
    lines = [
        "NulizArt Invoice",
        f"Quote ID: {quote_id}",
        "",
        "Service:",
        f" - {service}: ${SERVICES[service]:.2f}",
    ]
    if addons:
        lines.append("Add-ons:")
        for addon in addons:
            lines.append(f" - {addon}: ${ADDONS[addon]:.2f}")
    lines.extend([
        "",
        f"Total: ${total:.2f}",
        "",
        "Book your free meeting:",
        BOOKING_LINK,
    ])
    return "\n".join(lines)


def save_invoice(path: str, content: str) -> None:
    if path.lower().endswith(".pdf"):
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
        except ImportError:
            raise SystemExit("reportlab is required to generate PDF invoices")
        c = canvas.Canvas(path, pagesize=letter)
        textobject = c.beginText(50, 750)
        for line in content.splitlines():
            textobject.textLine(line)
        c.drawText(textobject)
        c.showPage()
        c.save()
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def main() -> None:
    args = parse_args()
    quote_id = str(uuid.uuid4())
    total = calculate_total(args.service, args.addons)
    invoice_text = build_invoice(args.service, args.addons, total, quote_id)

    print(invoice_text)

    if args.invoice:
        save_invoice(args.invoice, invoice_text)
        print(f"Invoice saved to {args.invoice}")


if __name__ == "__main__":
    main()
