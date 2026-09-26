# Engineering Kata #003 - Concurrency vs Parallelism

## Context

Some programs wait a lot.

They wait for network responses, disk reads, APIs, databases, queues, files, user input, or external services.

Other programs compute a lot.

They spend most of their time using the CPU: parsing large datasets, compressing files, processing images, running simulations, or calculating expensive results.

Concurrency and parallelism are related, but they are not the same idea.

In this kata, the goal is to build a practical mental model for both concepts in Python.

## Session Goal

Spend about **30 minutes** understanding and applying:

- what concurrency means;
- what parallelism means;
- why I/O-bound and CPU-bound work behave differently;
- how `ThreadPoolExecutor` can help with I/O-bound concurrency;
- why faster code is not the only goal of concurrent design.

## Theory Primer

### Concurrency

Concurrency is about dealing with multiple tasks whose lifetimes overlap.

The tasks may not literally run at the exact same instant, but the program can make progress on more than one task over time.

Example:

```text
Start request A
While A is waiting, start request B
While B is waiting, start request C
Collect results as they finish
```

### Parallelism

Parallelism is about doing multiple things at the exact same time, usually on multiple CPU cores.

Example:

```text
Core 1 computes task A
Core 2 computes task B
Core 3 computes task C
```

### I/O-bound work

I/O-bound work spends much of its time waiting outside the CPU.

Examples:

- HTTP requests;
- database queries;
- file reads;
- calls to external APIs.

Concurrency often helps here because one task can wait while another task starts.

### CPU-bound work

CPU-bound work spends most of its time actively computing.

Examples:

- image processing;
- compression;
- simulations;
- large numeric calculations;
- parsing huge files.

Parallelism may help here, but the right Python tool may be different.

## Challenge

Implement a small experiment that compares sequential execution with concurrent execution for fake I/O-bound work.

The fake I/O function should simulate waiting with `time.sleep`.

You should implement:

```python
def fetch_profile(user_id: int) -> dict:
    ...


def fetch_profiles_sequential(user_ids: list[int]) -> list[dict]:
    ...


def fetch_profiles_concurrent(user_ids: list[int]) -> list[dict]:
    ...
```

Expected shape:

```python
fetch_profile(1)
# {"id": 1, "name": "User 1"}
```

For this kata, `fetch_profile` does not call a real API. It only simulates latency.

## Required Behavior

### `fetch_profile`

- Receive a `user_id`.
- Sleep for a small amount of time, such as `0.2` seconds.
- Return a dictionary:

```python
{"id": user_id, "name": f"User {user_id}"}
```

### `fetch_profiles_sequential`

- Receive a list of user IDs.
- Fetch each profile one at a time.
- Preserve the input order.

### `fetch_profiles_concurrent`

- Receive a list of user IDs.
- Fetch profiles using `concurrent.futures.ThreadPoolExecutor`.
- Preserve the input order.

## Measurement

Add a small manual timing block using:

```python
time.perf_counter()
```

Compare:

```python
fetch_profiles_sequential([1, 2, 3, 4, 5])
fetch_profiles_concurrent([1, 2, 3, 4, 5])
```

Do not write fragile tests that assert exact timing.

Timing is for observation, not correctness.

## Tests

Write tests that verify:

1. `fetch_profile(1)` returns the expected dictionary.
2. sequential fetching returns the expected list of profiles.
3. concurrent fetching returns the same result as sequential fetching.
4. both sequential and concurrent versions preserve input order.

## Design Decisions

Think about:

- Where should timing code live?
- Should timing be tested?
- How do you preserve order when tasks run concurrently?
- What happens if one task raises an exception?
- Why is this example concurrent but not necessarily parallel?
- Would threads help the same way for CPU-bound work?

## Constraints

For this kata:

- Use only the Python standard library.
- Do not use external libraries.
- Do not use real HTTP requests.
- Do not use AI to generate the first implementation.
- Keep the implementation small.

Allowed documentation:

- Python docs for `concurrent.futures`;
- Python docs for `time`;
- Python docs for `threading` or `multiprocessing` if you want context.

## Out of Scope

Do **not** implement yet:

- `asyncio`;
- real API calls;
- retries;
- cancellation;
- timeouts;
- process pools;
- queues;
- worker supervision.

Those can become future katas.

## Timebox

Aim for approximately:

**30 minutes**

Suggested split:

1. 10 minutes: read and write a short theory note.
2. 15 minutes: implement sequential and concurrent versions.
3. 5 minutes: run tests and record what surprised you.

## Definition of Done

The kata is complete when you have:

1. `solution.py` with sequential and concurrent implementations;
2. `test_solution.py` with the required behavior tests;
3. a short manual timing comparison;
4. notes explaining:
   - concurrency in your own words;
   - parallelism in your own words;
   - why this kata is I/O-bound;
   - why `ThreadPoolExecutor` helps here;
   - one question you still have.

## After the First Attempt

Once the implementation is complete:

1. commit the first attempt;
2. request a code review;
3. discuss the design decisions;
4. document reusable concepts in the knowledge base.

Suggested first commit:

```text
kata-003: implement concurrency experiment first attempt
```

