"""Simple package price calculator.

Select any combination of services and the tool will recommend one of the
predefined packages. Pricing roughly mirrors the structure used on the NulizArt
website. For convenience, short identifiers are used for the services.
"""

# Individual service prices (used only for reference)
SERVICES = {
    "support": 500,
    "design": 850,
    "marketing": 950,
    "automation": 1200,
    "ecommerce": 1500,
}

# Package definitions used to determine pricing based on number of services
PACKAGES = [
    {
        "name": "Launch Pad",
        "id": "launch",
        "price": 1250,
        "min_services": 1,
        "max_services": 1,
    },
    {
        "name": "Growth Engine",
        "id": "growth",
        "price": 2950,
        "min_services": 2,
        "max_services": 2,
    },
    {
        "name": "Scale & Sustain",
        "id": "scale",
        "price": 5800,
        "min_services": 3,
        "max_services": len(SERVICES),
    },
]


def recommended_package(service_count):
    """Return the package dictionary that fits ``service_count``."""
    for pkg in PACKAGES:
        if pkg["min_services"] <= service_count <= pkg["max_services"]:
            return pkg
    # Fallback to the most expensive tier if nothing matched
    return PACKAGES[-1]


def calculate_price(selected_services):
    """Calculate package price for the given services.

    Parameters
    ----------
    selected_services : iterable[str]
        Identifiers for the chosen services.

    Returns
    -------
    tuple[str, int]
        ``(package_name, price)``.
    """

    # Validate service names
    for svc in selected_services:
        if svc not in SERVICES:
            raise KeyError(f"Unknown service: {svc}")

    pkg = recommended_package(len(selected_services))
    return pkg["name"], pkg["price"]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Package price calculator")
    parser.add_argument(
        "services",
        nargs="*",
        help=f"Selected services ({', '.join(SERVICES.keys())})",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available services and exit",
    )

    args = parser.parse_args()

    if args.list:
        print("Available services:")
        for name in SERVICES:
            print(f"- {name}")
        exit(0)

    if not args.services:
        parser.print_help()
        exit(1)

    try:
        package, price = calculate_price(args.services)
        print(f"Recommended package: {package}\nTotal price: ${price}")
    except KeyError as exc:
        print(exc)
        parser.print_help()
        exit(1)

