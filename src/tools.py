def clean_column_name(raw_name: str) -> str:
    return raw_name.strip().lower().replace(" ", "_")
