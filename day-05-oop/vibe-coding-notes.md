# Vibe Coding — Cleaned Notes

## What Is Vibe Coding?
A development approach where you **describe your goal clearly**, an AI coding assistant generates a draft, you **review and iterate**, then test and document. It's not about writing every line manually — it's about directing, reviewing, and refining AI-generated code.

## Core Workflow
```
Describe goal clearly → AI generates draft → Review → Iterate with follow-up prompts
        → Test it → Document
```

## Components of Vibe Coding

| Component | Role |
|---|---|
| **AI Coding Assistants** (Claude Code, GitHub Copilot) | Draft code, debug, guide implementation |
| **IDEs & Extensions** (Cursor, VS Code) | Platform where AI assists directly inside your editor |
| **NLP Models** | Understand your prompt, generate/refine/test/document code |
| **APIs & SDKs** | Let your AI-built app talk to other tools/services (build → test → deploy, iterative) |

## Why Use Vibe Coding
- **Speed** — faster first drafts
- **Learning partner** — good for understanding unfamiliar code/concepts
- **Debugging partner** — helps trace and explain errors

## How to Use It Well
1. Choose your AI coding assistant
2. Define your requirement clearly (vague prompts = vague code)
3. Review what it generates — don't blindly accept
4. Refine through follow-up prompts
5. Test it yourself before trusting it

## Key Features to Know
- **Natural language coding** — describe intent in plain English
- **Generative AI** — content/code creation from prompts
- **Instant generation** — first draft in seconds
- **Agentic AI** — multi-step workflows; AI agents that work toward a specific goal across several steps, not just one response
- **Iterative refinement** — no need to get the syntax right yourself, just describe what's wrong or what to change next
- **Real-time suggestions** — inline help as you type
- **Multi-file / multi-page awareness** — assistants that understand your whole project structure, not just one file

## Practical Reminders
- Build, deploy, debug, and test in a loop — not a single one-shot request
- Keep prompts specific and contextual (mention the app/interface, not just "fix this")
- Always document what was generated and why, so it's maintainable later — not just "it works"

## Related Concepts Covered Alongside (from your notes)
- **Exception handling**: `try` → attempt → `except` (handle, supports multiple exception types) → `else` (runs if no error occurs) → `finally` (always executes)
- **File organization**: modules, classes, files, aliases — e.g. `from x import y as z`
- **Database basics**: MySQL uses table-level and row-level locking; understanding locks matters when multiple processes access data at once
