# openclaw-review-testbed

Test repository for **OpenClaw** github-reviewer agent.

Create a PR from each branch to `main` to trigger the webhook:

| Branch | File | Issues |
|--------|------|--------|
| `feat/critical-issues` | `auth.py` | 🔴 Critical ×6 |
| `feat/high-issues` | `file_handler.py` | 🔴 Critical ×5 (security) |
| `feat/medium-issues` | `order_service.py` | 🟡 Warning ×7 |
| `feat/low-issues` | `utils.py` | 🔵 Suggestion ×5 |
