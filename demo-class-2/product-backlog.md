# Product Backlog – Task Manager App (Sample Project)

This is a sample backlog created to practice the Requirement Gathering stage of Agile.

## Stakeholders
- End users (people managing daily tasks)
- Product Owner (prioritizes backlog)
- Development team

## Project Objective
Build a simple app where users can create, track, and complete personal tasks.

---

## User Stories

### 1. [MUST HAVE] User Registration
**As a** new user, **I want** to create an account, **so that** my tasks are saved under my name.
**Acceptance Criteria:**
- User can sign up with name, email, password
- Duplicate emails are rejected
- Password must be at least 8 characters

### 2. [MUST HAVE] Add a Task
**As a** logged-in user, **I want** to add a new task with a title, **so that** I can track things I need to do.
**Acceptance Criteria:**
- Task title cannot be empty
- Task appears in the "To Do" list immediately after adding

### 3. [MUST HAVE] Mark Task as Complete
**As a** logged-in user, **I want** to mark a task as done, **so that** I can track my progress.
**Acceptance Criteria:**
- Completed tasks move to a "Done" section
- Completed tasks show a checkmark or strikethrough

### 4. [SHOULD HAVE] Edit a Task
**As a** logged-in user, **I want** to edit a task's title, **so that** I can fix mistakes or update details.
**Acceptance Criteria:**
- Clicking "Edit" opens an editable field
- Changes save without needing to reload the page

### 5. [SHOULD HAVE] Delete a Task
**As a** logged-in user, **I want** to delete a task, **so that** I can remove things I no longer need.
**Acceptance Criteria:**
- A confirmation prompt appears before deletion
- Deleted tasks are removed from all views

### 6. [COULD HAVE] Task Due Dates
**As a** logged-in user, **I want** to set a due date on a task, **so that** I know when it needs to be finished.
**Acceptance Criteria:**
- Due date is optional
- Tasks past their due date are visually highlighted

### Not in Scope for This Release
**[WON'T HAVE]** Team/shared task boards — planned for a future release, not this sprint.

---

## Priority Summary (MoSCoW)

| Priority | Stories |
|---|---|
| Must Have | Registration, Add Task, Mark Complete |
| Should Have | Edit Task, Delete Task |
| Could Have | Due Dates |
| Won't Have (this release) | Shared/team boards |
