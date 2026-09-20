# Practice Workflow

This repository is organized around short, deliberate practice sessions.

Default session length: **15-20 minutes**.

## Session rhythm

1. **Challenge**
   - Codex proposes a focused kata.
   - The prompt should explain the problem, constraints, expected behavior, and deliverables.
   - It should not reveal the intended implementation unless the exercise explicitly allows AI assistance.

2. **Clarification**
   - I can ask questions before coding.
   - For ambiguous or FDE-style katas, Codex may answer as a stakeholder with incomplete requirements.

3. **First attempt**
   - I write the first implementation.
   - Codex avoids implementing the solution unless I explicitly ask for it.

4. **Review**
   - Codex reviews the attempt as a real code review.
   - The review distinguishes bugs, design concerns, suggestions, style preferences, and missing tests.

5. **Discussion**
   - We discuss trade-offs, alternative designs, failure modes, and production implications when relevant.

6. **Refactor**
   - I perform the refactor when possible.
   - Codex may guide with hints, examples, or targeted suggestions.

7. **Knowledge capture**
   - We update `notes.md` inside the kata.
   - We update the shared knowledge base when a reusable concept appears.

## Knowledge base rule

When a kata exercises a reusable concept, record it in `knowledge/concepts/`.

Each concept note should capture:

- what the concept means;
- where it appeared in the kata;
- why it helped or hurt;
- common mistakes;
- trade-offs;
- references for later study.

The goal is not to create encyclopedic notes. The goal is to build a personal map of concepts that came from practice.

## Paradigm practice

Functional programming is a strength to keep developing, especially when a problem benefits from pure functions, composition, explicit data flow, and small transformations.

Object-oriented programming should also be practiced deliberately. When the kata's expected API or domain model naturally points to objects, classes, methods, protocols, or encapsulation, the exercise should lean into those ideas instead of avoiding them.

The aim is to choose a paradigm because it fits the problem, not because it feels most comfortable.
