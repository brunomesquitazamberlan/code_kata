# Engineering Katas 🥋

This repository is my space for **deliberate software engineering practice**.

The idea is simple: regularly set aside a small amount of focused time to write code, revisit fundamentals, and sharpen engineering judgment through small, focused challenges — **Engineering Katas**.

## What is a Kata?

The term *kata* comes from Japanese martial arts, where it refers to a sequence of movements practiced repeatedly to develop technique, precision, and fluency.

The idea translates surprisingly well to software engineering.

A kata doesn't need to solve a large problem or result in a complete application. Instead, it creates a small, controlled environment in which to practice a particular skill.

The goal is not only to reach a working solution, but to pay attention to **how that solution is designed and built**.

## How it works

Most katas start with a relatively small challenge, usually designed for an initial **15–30 minutes of focused practice**.

The basic workflow is:

1. **Receive the problem**
2. **Build a first solution without AI assistance**
3. **Review the code**
4. **Discuss decisions and alternatives**
5. **Refactor when appropriate**
6. **Document what I learned**

AI participates primarily as an **engineering sparring partner and code reviewer**, rather than as the author of the initial solution.

This is intentional. The part I want to practice is precisely the difficult one: turning a problem into code.

Some challenges may explicitly allow or require AI assistance. In those cases, using AI effectively — while still understanding, testing, and taking responsibility for the resulting code — becomes part of the exercise itself.

## What am I practicing?

The katas explore different areas of software engineering, including:

* data modeling;
* functions and composition;
* type systems;
* error handling;
* functional programming;
* testing;
* APIs and integrations;
* concurrency and asynchronous programming;
* persistence;
* software architecture;
* observability;
* debugging;
* refactoring;
* interface and contract design;
* reliability and failure handling.

Some exercises may evolve across multiple katas.

A small implementation may later receive new requirements, encounter production-like failures, need better tests, or become the foundation for exploring another engineering concept.

## Beyond coding exercises

Not every kata will be a fully specified programming problem.

Some challenges will intentionally include **ambiguity, incomplete requirements, messy data, failing systems, external integrations, or operational constraints**.

In those cases, the exercise is not simply to write code.

It is also to:

* ask the right questions;
* identify assumptions;
* decompose an ambiguous problem;
* make reasonable engineering trade-offs;
* build something useful with incomplete information;
* debug unfamiliar systems;
* reason about failure modes;
* move from prototype to production-quality thinking.

These challenges are particularly inspired by the kind of engineering work found in **Forward Deployed Engineering**, where understanding a real-world problem and turning it into a working system is often as important as the implementation itself.

## Some rules

There is no expectation that the first solution will be perfect.

In fact, part of the purpose of this repository is to make the learning process visible.

The general principle is:

> **First I try. Then I research. Then I refactor.**

Whenever useful, I keep track of decisions, mistakes, feedback, and changes in my understanding.

There is also no commitment to a particular paradigm.

Functional programming, object-oriented programming, type systems, design patterns, frameworks, and libraries are tools to explore — not goals by themselves.

The goal is to understand **when a tool helps, what trade-offs it introduces, and how it affects the resulting software**.

## Repository structure

Each kata has its own directory:

```text
engineering-katas/
├── README.md
├── AGENTS.md
├── PRACTICE.md
├── KATAS.md
├── katas/
│   ├── 001-result-type/
│   │   ├── README.md
│   │   ├── solution.py
│   │   ├── test_solution.py
│   │   └── notes.md
│   └── 002-...
└── knowledge/
    ├── README.md
    └── concepts/
        └── ...
```

`KATAS.md` is the index of challenges, status, and concepts practiced.

The kata `README` describes the challenge.

`solution.py` contains my implementation.

`test_solution.py` contains focused tests when the kata calls for them.

`notes.md` records decisions, difficulties, review feedback, refactorings, and lessons learned.

The `knowledge/` directory contains reusable concepts that emerged from practice, with references for later study.

The structure itself may evolve as the practice evolves.

## Why make this public?

Because software engineering is not only about writing code.

It is also about being able to **reason about systems, explain engineering decisions, evaluate trade-offs, and learn from imperfect solutions**.

This repository is not intended to be a collection of reference implementations or perfect answers.

It is a public record of deliberate practice: code I wrote, decisions I made, mistakes I discovered, ideas I changed my mind about, and concepts I am still trying to understand better.

In other words:

> **This is not a showcase of perfect code. It is a record of deliberate engineering practice.**

🥋 Let's practice.
