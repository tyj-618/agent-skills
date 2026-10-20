---
name: contract-first
description: Turn a feature request into a reviewable contract (scope, interface, error codes, acceptance, non-goals) before writing implementation code, and stop until the contract is accepted. Use when correctness or reviewability matters, or when a coding agent tends to jump straight to code.
---

# Contract First

Write the contract before the code. The contract is the artifact a reviewer approves; the implementation is downstream of it.

## When to use

- A new feature, tool, API, or behavior change where "done" is ambiguous.
- The agent tends to implement before the interface is agreed.
- Another person or agent will review the result.

## Core rules

- Do not write implementation code before the contract is accepted.
- The contract is the source of truth; code that conflicts with it is wrong.
- Make non-goals explicit. They prevent scope creep.
- Every error case needs a stable code and a category.
- Acceptance must be observable: a command, an input, and an expected output.
- If the request is ambiguous, ask. Do not invent requirements.
- If implementation reveals a contract gap, stop, amend the contract, and get re-approval.

## Workflow

1. Restate the request in one sentence.
2. Write the contract using the template below.
3. Stop and ask for approval.
4. Implement only what the contract covers.
5. Verify each acceptance item and record the command and output.
6. Report contract changes and uncovered work explicitly.

## Contract template

```markdown
# <Feature> contract

## Goal
One sentence.

## Scope
- ...

## Non-goals
- ...

## Interface
| Item | Input | Output |
| --- | --- | --- |

## Errors
| Category | Code | When |
| --- | --- | --- |

## Acceptance
| # | Given | When | Then | Checked by |
| --- | --- | --- | --- | --- |

## Open questions
- ...
```

## Completion standard

A reviewer can answer without reading the implementation:

- What is in scope, and what is explicitly out?
- What are the exact inputs and outputs?
- Which errors exist, and how are they categorized?
- How is each acceptance item checked?
