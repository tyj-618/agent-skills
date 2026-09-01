"""Create an empty Agent Delivery Packet without overwriting existing evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATES = {
    "task.md": "# Task\n\n## Original instruction\n\n<!-- Paste the verbatim user instruction here. -->\n\n## Accepted scope\n\n- In scope:\n- Out of scope:\n- Acceptance criteria:\n",
    "agent-report.md": "# Agent Report\n\n## Implementation plan used\n\n## Key decisions and reasons\n\n## Changed behavior\n\n## Known limitations and risks\n\n## Claims requiring reviewer verification\n",
    "changes.diff": "# Diff pending\n\n<!-- Replace with the actual diff, or explain why no diff is available. -->\n",
    "verification.md": "# Verification\n\n## Environment\n\n## Checks run\n\n## Checks not run\n",
    "transcript.md": "# Conversation Record\n\nRecord type: selected verbatim excerpts\n\n## Record\n\n## Omissions and redactions\n",
    "review-request.md": "# Review Request\n\nPlease inspect:\n\n1. \n\nKnown uncertainty:\n\nDecision needed from reviewer:\n",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create an empty Agent Delivery Packet.")
    parser.add_argument("target", type=Path, help="New empty packet directory")
    parser.add_argument("--task-slug", default="unknown-task")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target
    if target.exists() and any(target.iterdir()):
        print(f"Refusing to overwrite non-empty directory: {target}")
        return 1

    target.mkdir(parents=True, exist_ok=True)
    for filename, content in TEMPLATES.items():
        (target / filename).write_text(content, encoding="utf-8")

    metadata = {
        "task_slug": args.task_slug,
        "created_at": None,
        "agent": {"product": "unknown", "model": "unknown", "version": "unknown"},
        "environment": {"os": "unknown", "repository_revision": None},
        "record_type": "selected verbatim excerpts",
        "redactions_applied": False,
    }
    (target / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Created delivery packet scaffold: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
