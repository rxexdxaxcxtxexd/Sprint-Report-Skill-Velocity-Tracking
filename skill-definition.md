---
name: admin-velocity
description: Generate sprint reports - Admin Web App Epic velocity analysis OR full sprint-wide status report with team contributions and blockers
---

# Admin Velocity & Sprint Reporting Skill

## Purpose
**Dual-mode sprint reporting:**
1. **Admin Epic Mode** (default): Velocity analysis for Admin Web App V2 Epic (BOPS-3515)
2. **Full Sprint Mode** (--full-sprint): Complete sprint report covering all issues, team capacity, and executive summary

## When to Use

### Admin Epic Mode
- **Sprint reviews** (end of sprint) - Admin Web App epic focus
- **Mid-sprint checkpoints** (velocity checks) - Boat/Barge Admin progress
- **Executive reporting** (prepare presentation materials) - Gamma slides
- **Forecasting updates** (after validation milestones) - Velocity projections

### Full Sprint Mode
- **Sprint retrospectives** (complete sprint summary)
- **Stakeholder updates** (all work streams, not just Admin)
- **Team capacity planning** (who worked on what)
- **Blocker escalation** (identify risks across entire sprint)

## What This Skill Does

## MODE 1: Admin Epic Analysis (Default)

### 1. Fetch Current Jira Data
- Get epic BOPS-3515 and all child issues
- Get Boat Admin (BOPS-3533) with all 28+ subtasks and current statuses
- Get Barge Admin (BOPS-3517) with all subtasks and demo issues
- Get remaining 5 admin screens (BOPS-3516, 3522, 3532, 3534, 3535)
- Capture current sprint information from board

### 2. Calculate Velocity Metrics

**Boat Admin Baseline (Historical):**
- Total days active (from Nov 7, 2025 to current date)
- Tasks completed ÷ days active = baseline velocity
- Sprint-by-sprint breakdown (Sprint 10, 11, 12, etc.)
- Peak velocity (Sprint 11: 0.93 tasks/day)
- Blended average (currently: 0.56 tasks/day baseline)

**Current Sprint Velocity:**
- Tasks completed since last checkpoint ÷ days elapsed
- Compare to baseline and previous sprint
- Flag acceleration or deceleration trends

**Projected Velocity (for incomplete screens):**
- Apply improvement factors:
  - +30% from AI process locked
  - +40% from team expansion (Derrick onboarded)
  - -50% QA issues (from preventative checklist)
- Calculate three scenarios: Conservative (0.85/day), Realistic (0.90/day), Optimistic (1.0/day)

### 3. Load Previous Sprint Data
- Check for previous checkpoint: `.claude-sessions/admin-velocity-*.json`
- If found, load for comparison
- Calculate deltas: subtasks added/removed, velocity changes, completion progress

### 4. Generate Reports

**Report A: Simple Progress Table** (`Admin-Screens-Progress-Sprint-{N}.md`)
Format matching original Sprint 11 PDF:
```
| Admin Screen | Issue Key | Subtasks | Done | Remaining |
|-------------|-----------|----------|------|-----------|
| 🚤 Boat Admin | BOPS-3533 | X | Y | Z (N in-flight) |
```

**Report B: Velocity Analysis** (`Admin-Velocity-Analysis-Sprint-{N}.md`)
Full narrative including:
- Executive summary with key metrics
- Boat Admin baseline velocity analysis
- Current focus screen (Barge Admin or next) deep dive
- Velocity projections with scenarios
- Conservative forecasting rationale
- Sprint goals and critical dates
- Sprint-over-sprint comparison (if previous checkpoint exists)

**Report C: Gamma Presentation Slides** (`Admin-Velocity-Gamma-Sprint-{N}.md`)
10-slide deck with explicit Gamma rendering instructions:
1. Executive Summary - Epic progress snapshot
2. Admin Screens Velocity Dashboard
3. Boat Admin Baseline Timeline
4. Process Improvements (before/after)
5. Current Focus Screen Analysis (Barge Admin or next)
6. Velocity Projection Methodology
7. Validation Gate Criteria (if applicable)
8. Conservative Forecasting Approach
9. Sprint Goals - Next 3 Weeks
10. Next Steps & Key Takeaways

### 5. Save Checkpoint (Admin Mode)
Create timestamped checkpoint: `.claude-sessions/admin-velocity-{YYYY-MM-DD}.json`

**Checkpoint Schema:**
```json
{
  "timestamp": "2025-12-28T10:30:00",
  "sprint": 13,
  "analysis_date": "2025-12-28",
  "boat_admin": {
    "subtasks": 28,
    "completed": 15,
    "in_progress": 4,
    "remaining": 9,
    "completion_pct": 54,
    "days_active": 51,
    "velocity": 0.56
  },
  "barge_admin": {
    "subtasks": 21,
    "completed": 1,
    "remaining": 20,
    "completion_pct": 5,
    "demo_issues": 17,
    "velocity": null
  },
  "epic_total": {
    "subtasks": 64,
    "completed": 16,
    "remaining": 48,
    "completion_pct": 25
  },
  "velocity_trends": {
    "sprint_11": 0.93,
    "sprint_12": 0.23,
    "baseline": 0.56
  }
}
```

---

## MODE 2: Full Sprint Report (--full-sprint)

### 1. Fetch Sprint Data from Board
- Get active sprint from BargeOps Agile Team Board (Board 38)
- Fetch ALL issues in the sprint (typically 70-80 issues)
- Get issue details: status, assignee, type, priority, parent, subtasks
- Get previous sprint data for "Sprint X Goals" section

### 2. Calculate Sprint Metrics
- **Status breakdown:** Count issues by status (Done, In Progress, In Code Review, etc.)
- **Issue type distribution:** Epics, Tasks, Sub-tasks, Bugs
- **Team contributions:** Issues per assignee with completion rates
- **Completion rate:** Done ÷ Total issues
- **Quality metrics:** Bugs found vs bugs fixed

### 3. Identify Key Information
- **Accomplishments:** What was completed (epics closed, features delivered)
- **Blockers/Risks:** Unassigned work, pending bugs, blocked items
- **Sprint goals:** Extract from previous sprint review (or user input)
- **Team capacity:** Who worked on what, OOO dates
- **Decisions/Discussions:** Major process changes or strategy shifts

### 4. Generate Executive Sprint Report
**Format:** Matches Sprint 11 PDF style (2-page concise format)

**Page 1: Sprint Review**
- Sprint X Goals (from previous sprint)
- Accomplishments (bullet points, epic-focused)
- Decisions/Discussions (process updates, strategy)
- Blockers/Risks (current impediments)

**Page 2: Sprint Planning**
- Sprint X+1 Goals (current/next sprint)
- Team Capacity & Focus (table with hours and assignments)

**File:** `iBOPS FY25 Agile Team - Status Report Sprint {N} ({dates}).md`

### 5. Save Sprint Checkpoint (Full Sprint Mode)
Create timestamped checkpoint: `.claude-sessions/sprint-{N}-{YYYY-MM-DD}.json`

**Sprint Checkpoint Schema:**
```json
{
  "timestamp": "2025-12-29T14:00:00",
  "sprint_number": 12,
  "sprint_dates": {
    "start": "2025-12-15",
    "end": "2025-12-29"
  },
  "board_info": {
    "board_id": 38,
    "board_name": "BargeOps Agile Team Board",
    "project": "BOPS"
  },
  "metrics": {
    "total_issues": 77,
    "completed": 23,
    "in_progress": 4,
    "in_review": 8,
    "completion_pct": 29.9
  },
  "by_type": {
    "Epic": 2,
    "Task": 9,
    "Sub-task": 60,
    "Bug": 6
  },
  "by_status": {
    "Done": 23,
    "In Progress": 4,
    "In Code Review": 8,
    "Ready for Dev": 16,
    "New": 12,
    "IN CSG QA/UVT": 2,
    "Other": 12
  },
  "team_contributions": {
    "Doug Romano": {"assigned": 13, "completed": 11},
    "Paulette Whaley": {"assigned": 13, "completed": 2},
    "Viktor Dubrovin": {"assigned": 7, "completed": 3},
    "...": "..."
  },
  "key_epics": [
    {"key": "BOPS-3343", "name": "Crewing Module", "status": "In Progress"},
    {"key": "BOPS-3345", "name": "Parker Towing Customization", "status": "Done"}
  ],
  "blockers": [
    "Barge Admin v2 not started (BOPS-3517)",
    "34 unassigned items"
  ]
}
```

---

## Parameters (Optional)

Usage: `/admin-velocity [options]`

### Mode Selection
- `--full-sprint`: Generate full sprint report (all issues, not just Admin epic)
- `--both`: Generate both Admin epic analysis AND full sprint report

### General Options (Both Modes)
- `--sprint N`: Specify sprint number (default: auto-detect from Jira)
- `--compare-to DATE`: Compare to specific checkpoint date (e.g., `--compare-to 2025-12-15`)

### Admin Epic Mode Options
- `--skip-slides`: Skip Gamma slide generation (faster, table + analysis only)
- `--focus SCREEN`: Deep-dive on specific admin screen (e.g., `--focus Barge`)
- `--quick`: Generate simple table only (fastest, no velocity analysis)

### Full Sprint Mode Options
- `--skip-checkpoint`: Don't save sprint checkpoint (report only)
- `--format {concise|detailed}`: Report format (default: concise, matches Sprint 11 PDF)

**Examples:**

**Admin Epic Analysis (Default):**
- `/admin-velocity` - Full Admin epic analysis with Gamma slides
- `/admin-velocity --sprint 13` - Explicit sprint number
- `/admin-velocity --skip-slides` - Table + analysis, no Gamma deck
- `/admin-velocity --quick` - Simple table only
- `/admin-velocity --focus Barge` - Deep dive on Barge Admin

**Full Sprint Report:**
- `/admin-velocity --full-sprint` - Complete sprint report (Sprint 11 PDF format)
- `/admin-velocity --full-sprint --sprint 12` - Specific sprint number
- `/admin-velocity --full-sprint --format detailed` - Detailed report with metrics tables

**Both Reports:**
- `/admin-velocity --both` - Generate both Admin epic analysis + full sprint report

## Key Principles (Always Follow)

1. **Conservative Forecasting**:
   - Only project completion dates for screens with validation data
   - Barge Admin = validation gate
   - Don't project remaining 5 screens until Barge Admin validates velocity

2. **Velocity Validation**:
   - Use actual measured data (Boat Admin: 0.56 tasks/day)
   - Show improvement factors explicitly (+30% process, +40% team)
   - Provide three scenarios (conservative, realistic, optimistic)

3. **Scope Transparency**:
   - Always show scope changes (subtasks added/removed)
   - Explain why scope changed (demo discoveries, refinements)
   - Distinguish "scope creep" from "scope discovery"

4. **Sprint-Over-Sprint Comparison**:
   - Load previous checkpoint if exists
   - Show deltas for all metrics (±X subtasks, ±Y% velocity)
   - Flag concerning trends (velocity decrease, scope explosion)

5. **Validation Gates**:
   - Define success criteria (4 metrics for Barge Admin)
   - Show pass/fail outcomes
   - Explain impact on future forecasts

## Output Files Created

### Admin Epic Mode
1. **`Admin-Screens-Progress-Sprint-{N}.md`** - Simple table (Sprint 11 PDF format)
2. **`Admin-Velocity-Analysis-Sprint-{N}.md`** - Full narrative analysis
3. **`Admin-Velocity-Gamma-Sprint-{N}.md`** - Gamma presentation slides (unless --skip-slides)
4. **`.claude-sessions/admin-velocity-{YYYY-MM-DD}.json`** - Checkpoint for next comparison

### Full Sprint Mode
1. **`iBOPS FY25 Agile Team - Status Report Sprint {N} ({dates}).md`** - Executive sprint report (Sprint 11 PDF format)
2. **`.claude-sessions/sprint-{N}-{YYYY-MM-DD}.json`** - Sprint checkpoint for comparison

### Both Modes (--both)
All of the above files from both modes

## Integration with Existing Files

### Admin Epic Mode References
- **Jira Epic:** BOPS-3515 (Admin Web App v2)
- **Boat Admin:** BOPS-3533 (baseline velocity source)
- **Barge Admin:** BOPS-3517 (validation sprint)
- **Demo Issues:** Documented in Barge Admin demo MD files
- **Previous Analyses:** Sprint 11 baseline, earlier progress reports

### Full Sprint Mode References
- **Jira Board:** Board 38 (BargeOps Agile Team Board)
- **Project:** BOPS (BargeOps)
- **Active Sprint:** Auto-detected from board
- **All Epics:** BOPS-3343 (Crewing), BOPS-3515 (Admin), BOPS-3657 (BI Work), etc.
- **Previous Sprint Reports:** Located in `OneDrive - Cornerstone Solutions Group\Desktop\Internal BOPS Team\iBOPS Sprint Reports\`

## Workflow

### Admin Epic Mode Workflow
1. User invokes: `/admin-velocity` (or with Admin-specific parameters)
2. Skill fetches Admin epic BOPS-3515 and all child issues via Jira MCP
3. Skill loads previous admin-velocity checkpoint (if exists) from `.claude-sessions/`
4. Skill calculates velocity metrics (baseline, projected) and compares to previous sprint
5. Skill generates 3 reports (progress table, velocity analysis, Gamma slides)
6. Skill saves new admin-velocity checkpoint for next sprint comparison
7. User gets summary of files created and key velocity findings

### Full Sprint Mode Workflow
1. User invokes: `/admin-velocity --full-sprint` (or `--both`)
2. Skill fetches active sprint from Board 38 (all issues) via Jira MCP
3. Skill loads previous sprint checkpoint (if exists) from `.claude-sessions/`
4. Skill calculates sprint metrics (status breakdown, team contributions, completion rate)
5. Skill analyzes accomplishments, blockers, and generates executive summary
6. Skill generates sprint report matching Sprint 11 PDF format
7. Skill saves new sprint checkpoint for next sprint comparison
8. User gets summary of sprint health and report location

## Success Metrics

### Admin Epic Mode Success Criteria
After running `/admin-velocity`, you should have:
- ✅ Clear velocity baseline and projections for Admin epic
- ✅ Sprint-over-sprint comparison showing Admin screens progress
- ✅ Presentation-ready Gamma slides for stakeholders
- ✅ Conservative forecasting with validation gates
- ✅ Saved admin-velocity checkpoint for next sprint review

### Full Sprint Mode Success Criteria
After running `/admin-velocity --full-sprint`, you should have:
- ✅ Complete sprint status across all work streams (not just Admin)
- ✅ Team contribution breakdown with completion rates
- ✅ Executive summary in Sprint 11 PDF format
- ✅ Clear identification of blockers and risks
- ✅ Saved sprint checkpoint for next retrospective

## Notes

### Admin Epic Mode
- **First Run:** No previous checkpoint exists, skill will note this and create baseline
- **Subsequent Runs:** Automatic comparison to previous sprint
- **Scope Changes:** Skill detects and explains subtask additions/removals
- **Demo Issues:** Skill incorporates demo findings (e.g., Barge Admin's 17 issues)

### Full Sprint Mode
- **Report Format:** Designed to match Sprint 11 PDF style (concise, executive-focused)
- **Board Integration:** Auto-fetches from Board 38 (BargeOps Agile Team Board)
- **Team Capacity:** Estimates based on issue assignments (can be refined with user input)
- **Sprint Goals:** Extracted from previous sprint or can be provided via user input
- **Checkpoint Comparison:** Shows sprint-over-sprint deltas (velocity, scope, completion)

### Both Modes
- **Jira MCP Required:** Skill uses Jira MCP server for data fetching
- **Output Location:** Reports saved to current directory (or OneDrive path for full sprint reports)
- **Checkpoint Storage:** All checkpoints saved to `.claude-sessions/` directory
- **Date Format:** Uses ISO format (YYYY-MM-DD) for consistency

---

**Created:** December 28, 2025
**Last Updated:** December 29, 2025
**Skill Type:** Workflow / Reporting (Dual-Mode)
**Category:** Project Management, Velocity Tracking, Sprint Reporting
**Modes:** Admin Epic Analysis | Full Sprint Reporting
