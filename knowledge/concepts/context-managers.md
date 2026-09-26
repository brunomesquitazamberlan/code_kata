# Context Managers

## In one sentence

A context manager is an object used with `with` to control what happens when entering and leaving a block of code.

## Where it appeared

- Kata: #001 Result Type
- File: `katas/001-result-type/test_solution.py`
- Situation: Testing that `Err.unwrap()` raises `RuntimeError` using `pytest.raises`.

- Kata: #002 Input Normalization Pipeline
- File: `katas/002-input-normalization-pipeline/test_solution.py`
- Situation: Testing that invalid priority raises `ValueError`.

## Why it mattered

The syntax:

```python
with pytest.raises(RuntimeError):
    result.unwrap()
```

means that the code inside the block is expected to raise `RuntimeError`.

If the expected exception is raised, the test passes. If no exception is raised, or the wrong exception is raised, the test fails.

## Common traps

- Thinking `with pytest.raises(...)` calls the function by itself. The function call must be inside the indented block.
- Putting assertions after the line that raises the exception inside the same block. Once the exception is raised, later lines in the block do not run.
- Using `pytest.raises` when the expected behavior is a returned error value rather than an exception.

## Trade-offs

Context managers are not only for testing. They also appear with files, locks, database transactions, and resource cleanup.

In these katas, the important idea is narrower: `pytest.raises` uses the context manager pattern to make expected exceptions explicit and readable.

## References

- [pytest: assertions about expected exceptions](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions)
- [Python reference: The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

