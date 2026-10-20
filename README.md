# agent-skills

Portable skills for coding agents that put evidence first.

A skill is a small folder with a `SKILL.md` (YAML frontmatter + instructions) plus optional references and scripts. Copy it into the skills directory your agent supports; the agent picks it up when the description matches the task.

## Skills

| Skill | What it does | Use when |
| --- | --- | --- |
| [agent-delivery-packet](skills/agent-delivery-packet) | Creates a reviewable handoff: original task, report, diff, verification, transcript, review questions, metadata | A coding task is done and will be reviewed by a human or another agent |
| [python-code-explainer](skills/python-code-explainer) | Produces an annotated `.py` that still compiles: functional header, block comments, improvement footer | You need to read, onboard, or archive Python and want intent-level commentary |
| [contract-first](skills/contract-first) | Writes the contract—scope, interface, error codes, acceptance, non-goals—before any implementation, and stops until accepted | Starting a feature where "done" is ambiguous, or the agent jumps straight to code |
| [eval-case-design](skills/eval-case-design) | Builds a fixed evaluation set with structured pass/fail signals and a deterministic baseline | You need to measure agent behavior, not claim it |

## Why this repo

Agents are good at saying "done". These skills make "done" inspectable:

- the original request is preserved verbatim;
- the diff is the evidence, not a prose summary;
- every "passed" has a command and an output;
- skipped checks and open risks are listed, not hidden;
- cases are fixed before running, and a baseline gives the pass rate meaning.

## Install

- **Claude Code**: copy the skill folder into `.claude/skills/<name>/` (project) or `~/.claude/skills/<name>/` (personal).
- **Other agents**: copy it into the skills directory they support, or paste `SKILL.md` as a rule/instruction file.
- **Verify**: ask the agent to use the skill by name.

## Anatomy of a skill

```text
skills/<name>/
├── SKILL.md          # frontmatter: name, description; then instructions
├── README.md         # English overview
├── README.zh-CN.md   # Chinese overview
├── references/       # optional: schemas, templates
└── scripts/          # optional: deterministic helpers
```

Frontmatter:

```yaml
---
name: skill-name
description: One sentence: what it does and when to use it.
---
```

## Design rules

1. **Evidence over claims** — no "done" without a command and its output.
2. **Portable** — no hardcoded paths; scripts take arguments.
3. **Human review** — skills assist; they do not approve.
4. **No secrets** — redact keys, tokens, cookies, and environment files.
5. **One job per skill** — if the description needs "and", split it.

## Adding a skill

1. Create `skills/<name>/SKILL.md` with the frontmatter above.
2. Make the description specific — it is the trigger.
3. Add `README.md` and `README.zh-CN.md`.
4. Put deterministic helpers in `scripts/`, templates in `references/`.
5. Test it on a real task before committing.

## License

MIT — see [LICENSE](LICENSE). Each skill is covered by the same license.