# Pytest And Assertions

## In one sentence

`assert` expresses an expectation, while `pytest` discovers test functions, runs them, and reports useful failure details.

## Where it appeared

- Kata: #001 Result Type
- File: `katas/001-result-type/test_solution.py`
- Situation: Testing `divide`, `Ok`, `Err`, and `Err.unwrap()`.

- Kata: #002 Input Normalization Pipeline
- File: `katas/002-input-normalization-pipeline/test_solution.py`
- Situation: Testing normalized ticket output, invalid priority, and input mutation behavior.

## Why it mattered

Manual `print` helped inspect behavior, but `assert` turned expectations into executable checks.

`pytest` made those checks repeatable. Instead of manually calling test functions, pytest discovered functions named `test_*`, ran them, and reported pass/fail results.

## Common traps

- Writing `assert` by itself. It needs an expression, such as `assert result.is_ok() is True`.
- Trying to assign `assert` to a variable. `assert` is a statement, not a value-producing expression.
- Testing internal details too early, such as checking `.value` when the public behavior is `unwrap()`.
- Forgetting that a test with only `pass` is discovered by pytest but does not verify behavior.

## Trade-offs

`print` is useful while exploring and learning.

`assert` is better for repeatable verification.

`pytest` becomes valuable when tests need to be discovered, organized, and run consistently.

## References

- [pytest: How to write and report assertions in tests](https://docs.pytest.org/en/stable/how-to/assert.html)
- [Python reference: The `assert` statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)

