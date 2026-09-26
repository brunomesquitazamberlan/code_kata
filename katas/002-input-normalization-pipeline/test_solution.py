import pytest

from solution import normalize_ticket


def test_normalize_ticket_example():
    raw_ticket = {
        "title": "  PAYMENT FAILED ",
        "priority": "High",
        "customer_email": " USER@Example.COM ",
        "tags": " billing, urgent ,, payments ",
    }

    assert normalize_ticket(raw_ticket) == {
        "title": "Payment failed",
        "priority": "high",
        "customer_email": "user@example.com",
        "tags": ["billing", "urgent", "payments"],
    }


def test_normalize_ticket_collapses_title_whitespace():
    raw_ticket = {
        "title": "  PAYMENT   FAILED  ",
        "priority": "medium",
        "customer_email": "user@example.com",
        "tags": "billing",
    }

    result = normalize_ticket(raw_ticket)

    assert result["title"] == "Payment failed"


def test_normalize_ticket_rejects_invalid_priority():
    raw_ticket = {
        "title": "Payment failed",
        "priority": "critical",
        "customer_email": "user@example.com",
        "tags": "billing",
    }

    with pytest.raises(ValueError):
        normalize_ticket(raw_ticket)


def test_normalize_ticket_does_not_mutate_input():
    raw_ticket = {
        "title": "  PAYMENT FAILED ",
        "priority": "High",
        "customer_email": " USER@Example.COM ",
        "tags": " billing, urgent ,, payments ",
    }

    normalize_ticket(raw_ticket)

    assert raw_ticket == {
        "title": "  PAYMENT FAILED ",
        "priority": "High",
        "customer_email": " USER@Example.COM ",
        "tags": " billing, urgent ,, payments ",
    }
