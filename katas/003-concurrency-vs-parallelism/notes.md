# Notes - Kata #003 Concurrency vs Parallelism

## Before Coding
Should I use asyncio.sleep ou "regular" sleep in fetch_profile()?

What means time.perf_counter()?

## During Coding

ThreadPoolExecutor with context manager
- submit
- map

Max Workers could be the lenght of the input_list


Max_workers is different from the number os executions

## After First Attempt

What is the difference between append submit methods? as_completed, map?

I can use ThreadPoolExecutor with or without Futures. When I need more control, I should use Futures. In this case, I didn't need them. The only requirement was to preserve the order.

Be careful to avoid misunderstandings between `async def` and `def`.

Concurrency means to orchestrate tasks
Parallelism means executing something at the same moment
Generally:
- ThreadPoolExecutor means Concurrency
- ProcessPoolExecutor means Parallelism
