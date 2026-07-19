# Pre-Demo Class Notes – Fresher Training Program
**Session:** Pre-Demo Class (before official Day 1)
**Topic:** Foundational Concepts – Architecture, Agile, URLs, Auth

---

## 1. Three-Tier Architecture

Software applications (including everything we'll build in this program) are typically split into three layers:

| Layer | Role | Example |
|---|---|---|
| **Presentation Layer** | What the user sees and interacts with | React UI, Tailwind CSS, forms, buttons |
| **Business Layer** | Processes logic, rules, and validation | FastAPI backend, API endpoints, auth checks |
| **Storage Layer** | Stores and retrieves data permanently | PostgreSQL database |

**Key idea:** each layer only communicates with the layer next to it. The presentation layer never talks to the database directly — it goes through the business layer.

---

## 2. Agile Methodology

Agile is a way of managing projects by breaking them into small, repeatable cycles instead of one big launch.

**Core values (Agile Manifesto):**
- People/collaboration over rigid process
- Working software over heavy documentation
- Customer collaboration over fixed contracts
- Responding to change over following a strict plan

**12 Principles (summarized):**
1. Deliver value early and often
2. Welcome changing requirements
3. Frequent delivery (short cycles)
4. Daily collaboration between business & devs
5. Motivated, trusted individuals
6. Face-to-face communication preferred
7. Working software = real measure of progress
8. Sustainable, consistent pace
9. Technical excellence & good design
10. Simplicity — do only what's needed
11. Self-organizing teams
12. Regular reflection & continuous improvement

**Agile SDLC stages:** Requirement Gathering → Design → Development → Testing → Deployment → Review/Maintenance

**Common Agile frameworks:**
- **Scrum** – fixed-length sprints, defined roles (Scrum Master, Product Owner)
- **Kanban** – visual board (To Do / Doing / Done), limits work-in-progress
- **XP (Extreme Programming)** – pair programming, test-driven development, continuous integration
- **Lean, APF, DSDM, FDD** – other variants for different project needs

**Agile vs Waterfall:** Waterfall = fixed requirements, sequential phases, no changes mid-way. Agile = iterative, flexible, embraces change.

**Tools used in industry:** Jira, Trello, Asana, ClickUp, Monday.com

---

## 3. URL (Uniform Resource Locator)

A URL is the address used to locate a resource on the web.

```
https://www.geeksforgeeks.org/dsa/array-data-structure-guide/#what-is-array
```

| Part | Example | Meaning |
|---|---|---|
| Scheme/Protocol | `https` | Communication method (HTTP, HTTPS, FTP) |
| Domain | `www.geeksforgeeks.org` | Server/website address |
| Port | (optional, e.g. `:8080`) | Network port used |
| Path | `/dsa/array-data-structure-guide/` | Location of the specific resource |
| Query | (optional, e.g. `?id=5`) | Extra data sent to the server |
| Fragment | `#what-is-array` | Jumps to a section within the page |

---

## 4. Authentication vs Authorization

| | Authentication | Authorization |
|---|---|---|
| **Question answered** | Who are you? | What are you allowed to do? |
| **When it happens** | First (verifying identity) | After authentication |
| **Example** | Logging in with username/password, JWT validation | Checking if a logged-in user has admin rights to delete a record |

Authentication confirms *identity*; authorization confirms *permissions*. One always precedes the other.

---

---

## 5. Practical Demo Done

Built a small working 3-tier app (`demo-3tier/`) to see the concept live instead of just reading about it:

- **presentation/index.html** – registration form (Presentation Layer)
- **business/server.js** – Node.js server that validates input (Business Layer)
- **storage/data.json** – flat file where valid records get saved (Storage Layer)

Ran it locally with `node server.js` and confirmed:
- Invalid inputs get rejected by the business layer before reaching storage
- Valid inputs get saved to `data.json` and persist even after restarting the server
- The presentation layer has no direct access to the data file — it only calls the server's `/submit` and `/data` endpoints

This made the "layers only talk to their neighbor" rule concrete instead of theoretical.

---

## Notes / Reflections
_(Add your own personal takeaways, doubts, or things to revisit here)_

