# Eval Case Design

`eval-case-design` is a portable skill that turns an agent or tool behavior into a fixed evaluation set with structured pass/fail signals and a deterministic baseline, so a reported pass rate can be reproduced.

中文说明：[README.zh-CN.md](README.zh-CN.md)

## What it does

- Lists the behaviors under test: happy path, clarification, business rejection, invalid input, and system failure.
- Fixes one case per behavior before any run, including at least one ambiguous or adversarial case.
- Scores tool names, arguments, returned codes, and final state. Free-text similarity is not the primary signal.
- Gives each case a fresh state, keeps the raw results, and keeps the failures.
- Runs the set N times and reports per-case pass counts, aggregates, sample size, model, version, and date.
- Compares those results with a deterministic baseline built from rules or regular expressions.

## Why use it

A pass rate is not evidence until the cases are fixed, the signals are structured, and a baseline sits beside the agent. Writing the cases first also keeps expectations from being rewritten until an implementation looks successful.

## When to use

- An agent or tool has a behavior you need to measure.
- You are about to claim "it works" and need something a reviewer can reproduce.
- You want to compare against a non-agent baseline.

## How to use with a coding agent

1. Copy this folder into the skill location supported by your coding agent.
2. Name the behavior and ask the agent to use `eval-case-design` to write the cases before running them.
3. Review the case set. After that, expectations stay fixed.
4. Ask for a checker, N runs, the baseline comparison, and a report that keeps the failures.

Suggested prompt:

> Use the `eval-case-design` skill. List the behaviors and write one fixed case for each, including an ambiguous or adversarial case. Stop before running. After I accept the cases, build a checker on structured signals, run it N times against a fresh state per case, add a deterministic baseline, and report sample size, model, version, date, failures, and limitations.

## Rules

- Fix the cases before running. Never edit expectations to make an implementation pass.
- Judge on structured signals: tool names and arguments, returned codes, final state.
- Do not use free-text similarity as the primary signal.
- One case per behavior; include at least one ambiguous or adversarial case.
- Fresh state per case (temporary database, reset fixture).
- Record raw results and keep failures.
- Always include a baseline; otherwise a pass rate means little.
- Report sample size, model, version, and date.

## Repository layout

```text
eval-case-design/
├── SKILL.md
├── README.md
└── README.zh-CN.md
```

## License

MIT — see the repository [LICENSE](../../LICENSE).
