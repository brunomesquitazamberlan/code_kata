# Engineering Kata #001 - Result Type

## Context

Operations do not always succeed.

A function may produce a valid value, or it may fail for an expected reason.

One common approach is to use exceptions for failures. However, not every failure is necessarily exceptional.

In this kata, the goal is to explore another way of representing operations that may succeed or fail.

## Challenge

Implement a generic `Result[T, E]` abstraction in Python.

A `Result` must represent exactly one of two possible states:

```python
Ok(value)
```

or:

```python
Err(error)
```

Where:

- `T` represents the successful value type.
- `E` represents the error type.

For example:

```python
result = Ok(42)

result.is_ok()
# True

result.unwrap()
# 42
```

And:

```python
result = Err("Patient not found")

result.is_ok()
# False

result.unwrap()
# What should happen here?
```

Deciding what should happen in the last example is part of the exercise.

## Expected Usage

Your implementation should make it possible to write:

```python
def divide(a: float, b: float) -> Result[float, str]:
    ...
```

With behavior equivalent to:

```python
divide(10, 2)
# Ok(5.0)

divide(10, 0)
# Err("division by zero")
```

## Design Decisions

There is intentionally no prescribed implementation.

Before or while coding, think about questions such as:

- How should `Ok` and `Err` be represented?
- What exactly is `Result`?
- Should it be a type alias, `Protocol`, base class, or something else?
- What should `unwrap()` do when called on `Err`?
- Is `is_ok()` enough, or should `is_err()` also exist?
- How should `T` and `E` be represented in Python's type system?
- Should `Ok` and `Err` be mutable?
- What should the public API expose?

These decisions are part of the kata.

## Constraints

For this first implementation:

- Do not use external libraries.
- Do not use Pydantic.
- Do not use `dataclass`.
- Do not look up existing Python implementations of `Result`.
- Do not use AI to generate the implementation.

Python documentation and language references are allowed.

Most importantly:

> Write the first implementation yourself.

## Out of Scope

Do **not** implement any of the following yet:

- `map`
- `map_err`
- `bind`
- `flat_map`
- `and_then`
- monadic composition helpers

They may become relevant in future katas.

Keep this implementation deliberately small.

## Timebox

Aim for approximately:

**15-30 minutes**

If you reach the timebox without finishing, stop and record where you got stuck.

Getting stuck is useful information.

## Definition of Done

The kata is complete when you have an implementation capable of expressing:

```python
def divide(a: float, b: float) -> Result[float, str]:
    ...
```

and can explain:

1. how you represented `Result`;
2. why you chose that representation;
3. what happens when `unwrap()` is called on an error;
4. whether your objects are mutable and why;
5. one thing about the implementation you are uncertain about.

Do not optimize for the most sophisticated solution.

Optimize for a solution you understand and can defend.

## After the First Attempt

Once the implementation is complete:

1. commit the first attempt;
2. request a code review;
3. discuss the design decisions;
4. refactor only after the review;
5. document the main lessons in `notes.md`.

Suggested first commit:

```text
kata-001: implement Result first attempt
```

The first commit should preserve your original reasoning, even if the implementation changes later.

