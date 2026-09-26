VALID_PRIORITIES = {"low", "medium", "high"}


def collapse_whitespace(input_string: str) -> str:
    return " ".join(input_string.split())


def normalize_title(input_string: str) -> str:
    cleaned_title = collapse_whitespace(input_string)
    return cleaned_title.capitalize()


def normalize_priority(input_string: str) -> str:
    priority = input_string.strip().lower()

    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Invalid priority: {input_string}")

    return priority


def normalize_email(input_string: str) -> str:
    return input_string.strip().lower()


def split_tags(input_string: str) -> list[str]:
    return input_string.split(",")


def normalize_tags(input_string: str) -> list[str]:
    tags = split_tags(input_string)

    normalized_tags = []

    for tag in tags:
        normalized_tag = tag.strip().lower()

        if normalized_tag:
            normalized_tags.append(normalized_tag)

    return normalized_tags


def normalize_ticket(raw: dict) -> dict:
    return {
        "title": normalize_title(raw["title"]),
        "priority": normalize_priority(raw["priority"]),
        "customer_email": normalize_email(raw["customer_email"]),
        "tags": normalize_tags(raw["tags"]),
    }


if __name__ == "__main__":
    raw_ticket = {
        "title": "  PAYMENT FAILED ",
        "priority": "High",
        "customer_email": " USER@Example.COM ",
        "tags": " billing, urgent ,, payments ",
    }

    print(normalize_ticket(raw_ticket))
