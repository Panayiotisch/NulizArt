SERVICES = {
    'design': 500,
    'development': 1000,
    'marketing': 750,
    'support': 300,
}


def calculate_price(selected_services):
    """Calculate total price for the selected services.

    Parameters
    ----------
    selected_services : iterable of str
        The names of services chosen by the client.

    Returns
    -------
    int
        The total price in dollars.

    Raises
    ------
    KeyError
        If any service in ``selected_services`` is not defined.
    """
    total = 0
    for svc in selected_services:
        if svc not in SERVICES:
            raise KeyError(f"Unknown service: {svc}")
        total += SERVICES[svc]
    return total


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Package price calculator")
    parser.add_argument(
        'services',
        nargs='+',
        help=f"Selected services ({', '.join(SERVICES.keys())})",
    )
    args = parser.parse_args()

    try:
        price = calculate_price(args.services)
        print(f"Total price: ${price}")
    except KeyError as exc:
        print(exc)
        parser.print_help()
        exit(1)

