# Function Composition

## In one sentence

Function composition means building a larger transformation by connecting smaller functions, usually by passing the output of one function into the input of the next.

## Where it appeared

- Kata: #002 Input Normalization Pipeline
- File: `katas/002-input-normalization-pipeline/solution.py`
- Situation: Normalizing a raw support ticket by applying small transformations to fields such as title, priority, email, and tags.

## Why it matters

Composition can make code easier to test and reason about because each step has a small, explicit responsibility.

It is especially useful when data moves through a sequence of transformations, validations, filters, enrichments, or formatting steps.

In Kata #002, the important design move was to stop thinking about normalization as one large operation and instead split it into field-specific transformations such as `normalize_title`, `normalize_priority`, `normalize_email`, and `normalize_tags`.

## Common traps

- Creating functions that are too tiny to carry meaning.
- Hiding important business logic inside a clever pipeline.
- Composing functions whose input and output types are unclear.
- Making debugging harder by removing useful intermediate names.

## Trade-offs

Composition tends to work well when each function has a clear contract and limited side effects.

It can be less helpful when the workflow depends heavily on shared state, branching behavior, I/O, or domain steps that need explicit names for readability.

## References

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python `functools`](https://docs.python.org/3/library/functools.html)
- [Python `itertools`](https://docs.python.org/3/library/itertools.html)
