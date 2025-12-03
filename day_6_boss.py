from typing import List, Dict, Any

def process_data(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Clean transaction data and compute total revenue.

    Args:
        data: List of raw transaction dicts
              e.g. [{'price': ' $10.50 ', 'qty': 5}]

    Returns:
        dict: {'total_revenue': float}
    """
    total = 0.0
    for row in data:
        raw_price = str(row["price"]).strip().replace("$", "").replace(" ", "")
        price = float(raw_price)
        qty = int(row.get("qty", 1))
        total += price * qty

    return {"total_revenue": total}


if __name__ == "__main__":
    sample = [
        {"price": " $10.50 ", "qty": 5},
        {"price": "$3.00", "qty": 2},
    ]
    summary = process_data(sample)
    print(summary)
