# Delivery Packet Schema

Use the smallest amount of text that preserves evidence. Keep any sensitive value redacted as `[REDACTED]` and explain the redaction only when it changes the review.

## `task.md`

```markdown
# Task

## Original instruction

<verbatim user request>

## Accepted scope

- In scope:
- Out of scope:
- Acceptance criteria:
```

## `agent-report.md`

```markdown
# Agent Report

## Implementation plan used

## Key decisions and reasons

## Changed behavior

## Known limitations and risks

## Claims requiring reviewer verification
```

Do not state that a test passed here unless `verification.md` records the evidence.

## `changes.diff`

Store the actual diff generated after the task, preferably from Git. If there is no repository or baseline, write:

```markdown
# Diff unavailable

Reason:

Changed files:
- path/to/file: concise description

Alternative evidence supplied:
```

Only attach source snapshots when a reviewer cannot reasonably inspect the changed files through the original project.

## `verification.md`

```markdown
# Verification

## Environment

- OS / runtime / relevant tool version:

## Checks run

### <check name>

Command:
```text
<exact command, with secrets redacted>
```

Exit status: <number>

Output:
```text
<raw output or a faithful excerpt, noting any omitted lines>
```

## Checks not run

- <check and reason>
```

## `transcript.md`

```markdown
# Conversation Record

Record type: verbatim export | selected verbatim excerpts | agent-written summary

## Record

<content>

## Omissions and redactions

- <what was omitted or redacted and why>
```

Never label an agent-written summary as a verbatim conversation record.

## `review-request.md`

```markdown
# Review Request

Please inspect:

1. <specific correctness, safety, or design question>
2. <specific missing test or boundary condition>

Known uncertainty:

Decision needed from reviewer:
```

## `metadata.json`

Use valid JSON. Do not include credentials or full sensitive prompts.

```json
{
  "task_slug": "example-task",
  "created_at": "2026-09-01T00:00:00+08:00",
  "agent": {
    "product": "Cursor",
    "model": "unknown",
    "version": "unknown"
  },
  "environment": {
    "os": "Windows",
    "repository_revision": "optional commit or null"
  },
  "record_type": "selected verbatim excerpts",
  "redactions_applied": true
}
```
