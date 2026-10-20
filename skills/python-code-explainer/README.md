# Python Code Explainer

`python-code-explainer` is a portable skill that interprets Python code and produces an annotated `.py` file with detailed Chinese comments. The annotated output **remains a valid, compilable Python file**, so it can still be read, diffed, and archived as documentation.

中文说明：[README.zh-CN.md](README.zh-CN.md)

## What it does

For any Python file (or a pasted snippet, or an entire project), the skill generates one annotated copy with a fixed three-part structure:

1. **Header — functional analysis.** A detailed Chinese introduction at the top of the file: one-line characterization, module responsibilities, key classes and functions, inputs/outputs, external dependencies, entry point, and key design decisions.
2. **Body — block-by-block comments.** Every minimal meaningful block (imports, constants, classes, functions, `if`/`for`/`try`/`with`, comprehensions, lambdas) is followed by a concrete Chinese comment explaining *why* and *what* — never paraphrasing the code.
3. **Footer — deficiencies and optimization.** A closing section listing concrete, actionable suggestions across readability, performance, robustness, security, testing, and compatibility.

## Why use it

- The output is **still a valid Python file** — comments only, original logic untouched, verified with `py_compile`.
- Comments explain intent, not syntax, so the annotated file doubles as documentation for reading and onboarding.
- Batch mode annotates every `.py` file in a project while skipping virtual environments, `__pycache__`, and already-annotated files.

## Current-folder mode (delete originals)

When the input code comes from an existing file on disk (especially a file in the current working folder), the skill **deletes the original file after the annotated version is written and passes syntax checks**. Safety rules:

- Deletion happens **only after** the annotated file is successfully written and `py_compile` passes; any failure keeps the original and reports to the user.
- Only the annotated source file is deleted — never any other file.
- The deletion result is reported to the user.

This mode keeps the folder clean, leaving only annotated copies for reading. If the originals must be kept, ask the agent to skip deletion.

## Use with a coding agent

1. Copy this folder into the skill location supported by your coding agent.
2. Ask the agent to interpret your Python code, or to annotate all code files in a project.
3. Review the generated `*_annotated.py` files.

Suggested prompt:

> Use the `python-code-explainer` skill to interpret `foo.py` and write `foo_annotated.py` in the same folder. After the annotated file passes syntax checks, delete the original file per the current-folder mode.

## Output example

Given `foo.py`, the skill produces `foo_annotated.py`:

```text
foo_annotated.py
├── header    # 《Python 代码解读》 — functional analysis (Chinese, UTF-8)
├── body      # original code + a Chinese comment after every minimal block
└── footer    # # === 代码不足与可优化方向 === deficiencies & optimization directions
```

## Repository layout

```text
python-code-explainer/
├── SKILL.md
├── README.md
└── README.zh-CN.md
```

## License

MIT — see the repository [LICENSE](../../LICENSE).
