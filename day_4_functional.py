def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def clean_text(value: str) -> str:
    return value.strip().lower()

if __name__ == "__main__":
    print(celsius_to_fahrenheit(25.0))
    print(clean_text("  Hello World  "))
