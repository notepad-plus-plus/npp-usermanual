# AGENTS.md

## Before making changes

- Read [Contribution Rules](CONTRIBUTION.md) and follow its requirements and recommendations.
- Check the relevant documentation and existing code patterns before editing.
- Keep changes focused and small, avoid unrelated refactoring or formatting.

## Project constraints

- Do not modify `.tests/` or `.github/` or `layouts/` or `themes/`.

## Validation

- If possible, ensure link verification passes locally before committing to your fork or submitting a PR from your fork:
    ```
    python -m pip install -r requirements.txt
    python -X utf8 .tests\check_links.py
    ```
- Enable GitHub Actions on your fork.
- Submit a PR only after all required workflows pass.

## PR instructions

- Disclose AI assistance, including the model. If possible also the prompt.
- Include AI agent as a co-author using a `Co-Authored-By` trailer.
- Contributors are encouraged to write their own PR descriptions.
- Comments and replies should be written by the contributors themselves.
