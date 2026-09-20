# Engineering Kata #002 - Input Normalization Pipeline

## Context

Real systems often receive messy input.

External forms, APIs, CSV files, and human-entered data may contain extra spaces, inconsistent casing, missing values, unexpected options, or fields that need to be transformed before the rest of the system can use them.

In this kata, the goal is to practice building a small normalization pipeline using simple Python functions.

The emphasis is not on clever code.

The emphasis is on:

- breaking a transformation into understandable steps;
- deciding what should be validated;
- keeping behavior explicit;
- writing small tests around data transformations.

## Challenge

Implement a function that normalizes a raw support ticket submission.

The main function should be:

```python
def normalize_ticket(raw: dict) -> dict:
    ...
```

Given a raw input like:

```python
raw_ticket = {
    "title": "  PAYMENT FAILED ",
    "priority": "High",
    "customer_email": " USER@Example.COM ",
    "tags": " billing, urgent ,, payments ",
}
```

It should produce:

```python
{
    "title": "Payment failed",
    "priority": "high",
    "customer_email": "user@example.com",
    "tags": ["billing", "urgent", "payments"],
}
```

## Required Behavior

Normalize the following fields:

### `title`

- Strip leading and trailing spaces.
- Collapse repeated internal whitespace into a single space.
- Convert to sentence-style casing.

Example:

```python
"  PAYMENT   FAILED  " -> "Payment failed"
```

### `priority`

- Strip spaces.
- Convert to lowercase.
- Accept only:
  - `"low"`
  - `"medium"`
  - `"high"`

### `customer_email`

- Strip spaces.
- Convert to lowercase.

This kata does **not** require full email validation.

### `tags`

- Receive tags as a comma-separated string.
- Split by comma.
- Strip spaces around each tag.
- Convert each tag to lowercase.
- Drop empty tags.

Example:

```python
" billing, urgent ,, payments " -> ["billing", "urgent", "payments"]
```

## Design Decisions

There is intentionally no prescribed implementation.

Before or while coding, think about questions such as:

- Should `normalize_ticket` call small helper functions?
- Should each field have its own normalization function?
- What should happen when a required field is missing?
- What should happen when `priority` has an invalid value?
- Should invalid input raise an exception, return a special value, or produce an error structure?
- Should this kata reuse the `Result` idea from Kata #001, or stay simpler?
- Which parts are pure transformations, and which parts are validation?

These decisions are part of the kata.

## Constraints

For this first implementation:

- Do not use external libraries.
- Do not use Pydantic.
- Do not use `dataclass`.
- Do not use AI to generate the implementation.
- Prefer the Python standard library.

Python documentation and language references are allowed.

## Out of Scope

Do **not** implement:

- full email validation;
- persistence;
- API endpoints;
- CLI parsing;
- fuzzy priority matching;
- automatic correction of misspelled fields.

Keep this deliberately small.

## Timebox

Aim for approximately:

**20-25 minutes**

If you reach the timebox without finishing, stop and record where you got stuck.

## Definition of Done

The kata is complete when you have:

1. an implementation of `normalize_ticket`;
2. at least three tests;
3. behavior for invalid or missing `priority`;
4. notes explaining:
   - how you decomposed the transformation;
   - how you handled invalid input;
   - whether your approach felt more functional or object-oriented;
   - one thing you would improve after review.

Do not optimize for a perfect validation framework.

Optimize for a solution you understand and can defend.

## After the First Attempt

Once the implementation is complete:

1. commit the first attempt;
2. request a code review;
3. discuss the design decisions;
4. refactor only after the review;
5. document reusable concepts in the knowledge base.

Suggested first commit:

```text
kata-002: implement input normalization first attempt
```

