# Contract First

`contract-first` is a portable skill that writes a reviewable contract—scope, interface, error codes, acceptance, and non-goals—before any implementation, and stops until that contract is accepted.

中文说明：[README.zh-CN.md](README.zh-CN.md)

## What it does

It produces the agreement before any code:

- Restates the request in one sentence.
- Writes scope, non-goals, the interface, a stable code and category for each error, and acceptance checks that name a command, an input, and an expected output.
- Stops and waits for approval.
- Implements only what the accepted contract covers, then records the command and output for each acceptance item.
- If implementation exposes a gap, amends the contract and asks for approval again.

## Why use it

When "done" is still vague, an agent fills the gap with code. The contract is what gets reviewed; the implementation follows it. A reviewer can decide scope, inputs, outputs, and errors without reading the diff first.

## When to use

- A new feature, tool, API, or behavior change where "done" is ambiguous.
- The agent tends to implement before the interface is agreed.
- Another person or agent will review the result.

## How to use with a coding agent

1. Copy this folder into the skill location supported by your coding agent.
2. Describe the feature and ask the agent to use `contract-first`.
3. Review the contract. Accept it, or send it back with changes.
4. After acceptance, ask the agent to implement only the contract and verify each acceptance item.

Suggested prompt:

> Use the `contract-first` skill. Restate the request in one sentence, write the contract, and stop. Do not write implementation code until I accept it. If implementation later exposes a gap, amend the contract and ask again before continuing.

## Rules

- Do not write implementation code before the contract is accepted.
- The contract is the source of truth; code that conflicts with it is wrong.
- Make non-goals explicit. They prevent scope creep.
- Every error case needs a stable code and a category.
- Acceptance must be observable: a command, an input, and an expected output.
- If the request is ambiguous, ask. Do not invent requirements.
- If implementation reveals a contract gap, stop, amend the contract, and get re-approval.

## Repository layout

```text
contract-first/
├── SKILL.md
├── README.md
└── README.zh-CN.md
```

## License

MIT — see the repository [LICENSE](../../LICENSE).
