# Data Normalization Pipeline

## In one sentence

A data normalization pipeline turns messy input into predictable internal data through a sequence of small transformation and validation steps.

## Where it appeared

- Kata: #002 Input Normalization Pipeline
- File: `katas/002-input-normalization-pipeline/solution.py`
- Situation: Normalizing raw support ticket fields such as `title`, `priority`, `customer_email`, and `tags`.

## Why it mattered

The raw input was inconsistent:

- casing varied;
- strings had extra spaces;
- tags arrived as a comma-separated string;
- priority needed validation.

Breaking the logic into small functions made the behavior easier to inspect and test:

- `normalize_title`
- `normalize_priority`
- `normalize_email`
- `normalize_tags`

## Common traps

- Mutating the input dictionary without noticing.
- Only testing the happy path from the README.
- Forgetting edge cases such as repeated internal whitespace.
- Mixing transformation and validation without making the behavior explicit.
- Returning cleaned data even when a required field is invalid.

## Trade-offs

Small functions make transformations easier to test and reason about.

Too many tiny functions can become noisy if they do not carry meaningful domain intent.

For this kata, field-specific functions were useful because each field had different rules.

## References

- [Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python data structures: dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

