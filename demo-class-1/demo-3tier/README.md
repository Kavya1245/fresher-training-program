# 3-Tier Architecture Demo

A tiny working example showing how the three layers connect in a real running app.

```
demo-3tier/
├── presentation/
│   └── index.html      → Presentation Layer (form UI)
├── business/
│   └── server.js        → Business Layer (validation + routing logic)
└── storage/
    └── data.json         → Storage Layer (saved records)
```

## What Each Layer Does Here

- **Presentation** (`index.html`): shows a registration form and a table of saved users. Talks only to the business layer via `fetch()`.
- **Business** (`server.js`): a plain Node.js server. Validates name/email (business rule: no empty name, valid email format), then decides whether to save.
- **Storage** (`data.json`): a flat JSON file the business layer reads from and writes to. In a real project this would be a database like PostgreSQL, but a JSON file is enough to demonstrate the concept.

## How to Run It

**Requirement:** Node.js installed (check with `node -v`; no other downloads needed — no npm packages used).

```bash
cd demo-3tier/business
node server.js
```

Then open your browser at:
```
http://localhost:3000
```

Fill the form and submit — watch the record appear in the table below, and check `storage/data.json` to see it actually got written to disk.

## What To Notice (for your notes/demo talk)

- The presentation layer **never touches the file system directly** — it only calls `/submit` and `/data`.
- The business layer is the **only one** that decides what's valid and what gets saved.
- If you shut the server down and restart it, your data is still there — because storage is separate from the running app logic.

## Try Breaking It (optional, deepens understanding)

- Submit an invalid email (e.g. `abc`) → business layer rejects it, storage layer never gets touched.
- Manually edit `data.json` and refresh the page → presentation layer just displays whatever storage has, proving it doesn't hold its own data.
