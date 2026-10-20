---
name: eval-case-design
description: Turn an agent or tool feature into a fixed evaluation set with structured pass/fail signals and a deterministic baseline. Use when you need to measure agent behavior, compare against a non-agent baseline, or produce evidence instead of a claim.
---

# Eval Case Design

Design the cases before you run them. A pass rate without fixed cases, structured signals, and a baseline is not evidence.

## When to use

- An agent or tool has a behavior you need to measure.
- You are about to claim "it works" and need something a reviewer can reproduce.
- You want to compare against a non-agent baseline.

## Core rules

- Fix the cases before running. Never edit expectations to make an implementation pass.
- Judge on structured signals: tool names and arguments, returned codes, final state.
- Do not use free-text similarity as the primary signal.
- One case per behavior; include at least one ambiguous or adversarial case.
- Fresh state per case (temporary database, reset fixture).
- Record raw results and keep failures.
- Always include a baseline; otherwise a pass rate means little.
- Report sample size, model, version, and date.

## Workflow

1. List behaviors: happy path, clarification, business rejection, invalid input, system failure.
2. For each, define the case fields below.
3. Build a checker that returns pass/fail plus reasons per case.
4. Run N times; report per-case pass counts and aggregates.
5. Add a deterministic baseline (rules or regex) and compare.
6. Write the report: method, results, failures, limitations.

## Case template

```python
{
    "id": "C01",
    "turns": ["..."],
    "required_tools": ["..."],
    "forbidden_tools": ["..."],
    "expected_codes": ["..."],
    "preview_args": {"...": 0},
    "text_contains_any": ["..."],
    "text_not_contains": ["..."],
    "expect_new_requests": 0,
}
```

## Completion standard

A reader can reproduce the run, see which cases failed and why, and knows the sample size and limitations.
