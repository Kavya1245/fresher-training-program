# Demo Class 2 – Full Agile Process
**Session:** Pre-Demo Class 2
**Topic:** Agile Methodology – End-to-End Sprint Cycle

---

## The Full Cycle Covered Today

```
Requirement Gathering → Grooming → Planning → Scrum (daily) → Implementation
→ Quality Assurance → Deploy → Retrospective → (back to Requirement Gathering)
```

This is one full sprint. Agile repeats this loop every sprint (typically 1–4 weeks), continuously refining based on feedback. Problem/blocker discussions aren't a separate stage — they surface *inside* Grooming, Daily Scrum, and Retrospective, which is why those three exist.

---

## 1. Requirement Gathering
Identify stakeholders, define scope/objectives, build a Product Backlog, write User Stories with acceptance criteria. (Covered in detail below — see Product Backlog section.)

## 2. Grooming (Backlog Refinement)
A recurring meeting (usually mid-sprint, for the *next* sprint) where the team:
- Reviews upcoming backlog items for clarity
- Breaks large stories into smaller, sprint-sized tasks
- Estimates effort (often via Story Points or Planning Poker)
- Removes outdated or irrelevant backlog items
- Flags open questions/blockers before planning locks them in

**Why it matters:** without grooming, planning meetings turn into confusion — half the team doesn't understand what a story even means.

## 3. Planning
Held at the start of each sprint. Covers:
- **Architecture decisions** — how the feature fits into the existing system (e.g. new API endpoint vs. modifying an existing one)
- **Task division** — breaking user stories into individual dev/QA tasks
- **Resource identification** — who's available, who has the right skills, who owns what
- **Sprint goal** — one clear sentence describing what "success" looks like by sprint end

Output: a **Sprint Backlog** — the subset of the Product Backlog committed to for this sprint.

## 4. Scrum (Daily Standup)
A short (~15 min) daily sync. Each person answers:
1. What did I do yesterday?
2. What will I do today?
3. Any blockers?

**Key rule:** this is a status sync, not a problem-solving session. Blockers get *raised* here, then solved in a separate follow-up conversation right after.

## 5. Implementation
Actual development work — coding, following the architecture agreed in planning, committing to Git regularly, code reviews via pull requests.

## 6. Quality Assurance (QA)
Testing the implemented work:
- **Unit testing** — individual functions/components
- **Integration testing** — components working together
- **User Acceptance Testing (UAT)** — does it meet the original acceptance criteria from the user story?
- Bug reports go back to Implementation if issues are found (short feedback loop, not a big handoff)

## 7. Deploy
Releasing the tested work to production (or staging first, depending on process). In modern teams this is often automated via CI/CD pipelines.

## 8. Retrospective
Held at the *end* of the sprint. The team reflects on:
- What went well?
- What didn't go well?
- What will we change next sprint?

This is where recurring blockers or process problems get formally addressed — not just patched on the fly, but fixed at the root so they don't repeat every sprint.

---

## Where "Problem Discussion" Fits

| Stage | Type of problem discussed |
|---|---|
| Grooming | Unclear requirements, missing details |
| Daily Scrum | Immediate day-to-day blockers |
| QA | Bugs and defects |
| Retrospective | Process/team-level recurring issues |

---

## Original Requirement Gathering Detail

```
Requirement Gathering → Design → Development → Testing → Deployment → Review/Maintenance
        ^
   (this is stage 1, expanded below)
```

This is the first stage of every Agile cycle. Unlike Waterfall (where requirements are locked upfront), Agile revisits this stage every sprint as priorities shift.

---

## What Happens in This Stage

1. **Identify stakeholders** — clients, end users, business team, subject matter experts
2. **Define scope & objectives** — what problem the software is solving
3. **Estimate budget & schedule** — rough sizing, not exact
4. **Build a Product Backlog** — a running, prioritized list of everything that could be built
5. **Write User Stories** — small, specific pieces of the backlog written from the user's point of view
6. **Set Acceptance Criteria** — the conditions that must be true for a story to be marked "done"

---

## User Story Format

```
As a [type of user], I want [some goal], so that [some benefit].
```

**Example:**
> As a registered user, I want to reset my password, so that I can regain access if I forget it.

---

## Prioritization Technique: MoSCoW

| Category | Meaning |
|---|---|
| **M**ust have | Critical, non-negotiable for this release |
| **S**hould have | Important but not critical |
| **C**ould have | Nice to have if time permits |
| **W**on't have | Out of scope for now |

---

## Practical Demo Done

Built a sample **Product Backlog** for a small "Task Manager App" (see `product-backlog.md`), including:
- 6 user stories written in proper format
- Acceptance criteria for each
- MoSCoW priority tags
- A simple Kanban board (`kanban-board.html`) showing how these requirements move from To Do → In Progress → Done

This demonstrates how raw requirements get turned into structured, trackable work items — the actual output of the requirement gathering stage.

---

## Notes / Reflections
_(Add your own personal takeaways, doubts, or things to revisit here)_
