def calculate_area(radius: float) -> float:
    """
    Calculate area of a circle.

    Args:
        radius (float): Circle radius.

    Returns:
        float: Area of the circle.
    """
    return 3.14159 * radius * radius


def clean_column_name(raw_name: str) -> str:
    """
    Convert a raw column name into snake_case.
    """
    return raw_name.strip().lower().replace(" ", "_")


def format_currency(amount: float) -> str:
    """
    Format a number as currency with 2 decimals.
    """
    return f"${amount:.2f}"


if __name__ == "__main__":
    print(calculate_area(5.0))
    print(clean_column_name("First Name"))
    print(format_currency(12.5))
