---
name: ibops-sprint
description: Generate iBOPS sprint reports with Jira + Fathom meeting insights - full sprint status OR admin velocity analysis
---

# iBOPS Sprint Reporting Skill

## Purpose
**Comprehensive sprint reporting with Fathom meeting integration:**
1. **Full Sprint Report** (default): Complete sprint status with Jira data + Fathom meeting insights
2. **Admin Velocity Analysis** (--include-admin-velocity): Optional add-on for Admin Web App V2 Epic velocity tracking

## When to Use

### Full Sprint Report (Default)
- **Sprint retrospectives** (complete sprint summary with meeting context)
- **Stakeholder updates** (synthesized view of Jira work + discussions)
- **Team capacity planning** (who worked on what, plus decisions from meetings)
- **Executive summaries** (Jira metrics + strategic decisions from sprint meetings)

### Admin Velocity Analysis (Optional)
- **Sprint reviews** (end of sprint) - Admin Web App epic focus
- **Mid-sprint checkpoints** (velocity checks) - Boat/Barge Admin progress
- **Executive reporting** (prepare presentation materials) - Gamma slides
- **Forecasting updates** (after validation milestones) - Velocity projections

## What This Skill Does

## MODE 1: Full Sprint Report (DEFAULT)

### 1. Fetch Sprint Data from Board
- Get active sprint from BargeOps Agile Team Board (Board 38)
- Fetch ALL issues in the sprint (typically 70-80 issues)
- Get issue details: status, assignee, type, priority, parent, subtasks
- Get previous sprint data for "Sprint X Goals" section

### 2. Fetch Meeting Data from Fathom (NEW)
- Use Fathom MCP `search_meetings` tool
- Filter: title contains "iBOPS" OR "BOPS"
- Date range: sprint start date to sprint end date
- Retrieve: summaries, action items, highlights, transcripts
- Process: Extract accomplishments, decisions, blockers from meeting discussions

### 3. Calculate Sprint Metrics
- **Status breakdown:** Count issues by status (Done, In Progress, In Code Review, etc.)
- **Issue type distribution:** Epics, Tasks, Sub-tasks, Bugs
- **Team contributions:** Issues per assignee with completion rates
- **Completion rate:** Done ÷ Total issues
- **Quality metrics:** Bugs found vs bugs fixed

### 4. Synthesize Insights (ENHANCED)
- **Accomplishments:** Merge Jira completed issues + meeting celebrations/demos discussed
- **Decisions/Discussions:** Add strategic decisions and process changes from meetings
- **Blockers/Risks:** Merge Jira blockers + concerns raised in meetings
- **Deduplicate:** Remove redundant information (if Jira shows BOPS-3345 done, skip meeting mention)
- **Attribution:** Add light prefixes like "From sprint planning:" or "From retrospective:"
- **Keep Concise:** 2-5 meeting insights per section, 1 sentence max each

### 5. Generate Executive Sprint Report
**Format:** Matches Sprint 11 PDF style (2-page concise format) **with meeting insights blended in**

**Page 1: Sprint Review**
- Sprint X Goals (from previous sprint)
- Accomplishments (bullet points, epic-focused) **+ meeting celebrations**
- Decisions/Discussions (process updates, strategy) **+ meeting strategic decisions**
- Blockers/Risks (current impediments) **+ meeting concerns**

**Page 2: Sprint Planning**
- Sprint X+1 Goals (current/next sprint)
- Team Capacity & Focus (table with hours and assignments)

**Enhanced Section Example:**
```markdown
## Key Accomplishments ✅

### 1. **Parker Towing Co. Customization Epic - COMPLETED** (BOPS-3345)
- Entire TVR Form customization epic closed
- Status: Done (December 17, 2025)
- From retrospective: Team celebrated seamless deployment with zero rollback

### 2. **Boat Admin v2 - Major Progress** (BOPS-3533)
- **Completed:** 13 demo/QA fixes addressing demo feedback
- From sprint planning: Demo received positive feedback from stakeholders
```

**File:** `iBOPS FY25 Agile Team - Status Report Sprint {N} ({dates}).md`

### 6. Generate Sprint Review Gamma Presentation (NEW)
**Format:** 4-slide deck inspired by existing Sprint Review PowerPoints **with creative liberty**

**Design Approach:**
- Focus on content structure and information flow (well-defined)
- Don't attempt to replicate exact brand graphics, logos, or blob graphics
- Keep slides clean and professional with Gamma's native styling
- Prioritize readability and content clarity over brand matching

**Slide Structure:**

**Slide 1: Title**
```markdown
# Sprint {N}: Product Owner Review

**iBOPS**

Sprint Dates: {start_date} - {end_date}

**Gamma Instructions:**
- Clean title slide, professional styling
- No complex graphics or logos
- Centered text with hierarchy
```

**Slide 2: Sprint {N} Overview**
```markdown
## Sprint {N} Goals
**Deliverables:**
- [Key deliverable 1 from sprint goals]
- [Key deliverable 2]

**Process:**
- [Process improvement 1]

## Work Stream Status
**[Category 1]** (e.g., Parker Towing, BI Work, Crewing)
- [Epic/feature name] - Complete | In Progress | X items remaining
- Meeting insights integrated where relevant

**[Category 2]**
- ...

**Gamma Instructions:**
- Use bullet lists with status indicators
- Optional: status badges (✅ Complete, 🔄 In Progress, ⏳ Remaining)
- Organize by work stream categories
```

**Slide 3: Sprint {N+1} Plan**
```markdown
## Goals
**Deliverables:**
- [Next sprint deliverable 1]
- [Next sprint deliverable 2]

**Work Streams:**
**[Category 1]**
- [Goal 1] - Target: [date if applicable]
- [Goal 2]

**[Category 2]**
- [Goal 1]

**Gamma Instructions:**
- Forward-looking content
- Clean bullet organization by work stream
- Include target dates for key milestones
```

**Slide 4: Demos**
```markdown
## Sprint {N} Demos

- [Demo 1 name from Fathom meeting insights]
- [Demo 2 name]
- [Demo 3 name]

**Gamma Instructions:**
- Simple list format
- Can include brief 1-sentence descriptions if helpful
- Pull demo names from Fathom meeting insights or Jira completed items
```

**File:** `Sprint-Review-Gamma-Sprint-{N}.md`

**When to Generate:**
- Default: Always generate with full sprint report
- Skip: Use `--skip-sprint-slides` parameter (faster, report only)

### 7. Save Sprint Checkpoint (Full Sprint Mode)
Create timestamped checkpoint: `.claude-sessions/ibops-sprint-full-{N}-{YYYY-MM-DD}.json`

**Enhanced Sprint Checkpoint Schema (with Fathom metadata):**
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
    "completion_pct": 29.9
  },
  "fathom_integration": {
    "enabled": true,
    "meetings_fetched": 5,
    "meetings_processed": 5,
    "filter_used": "title contains 'iBOPS' OR 'BOPS'",
    "insights_extracted": {
      "accomplishments": 3,
      "decisions": 4,
      "blockers": 2
    },
    "meeting_list": [
      {
        "title": "iBOPS Sprint 12 Planning",
        "date": "2025-12-15T10:00:00Z",
        "recording_id": "abc123"
      }
    ]
  }
}
```

---

## MODE 2: Admin Velocity Analysis (--include-admin-velocity or --admin-only)

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
- Check for previous checkpoint: `.claude-sessions/ibops-sprint-admin-*.json` or `.claude-sessions/admin-velocity-*.json` (backward compatible)
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
Create timestamped checkpoint: `.claude-sessions/ibops-sprint-admin-{YYYY-MM-DD}.json`

**Checkpoint Schema:**
```json
{
  "timestamp": "2025-12-28T10:30:00",
  "sprint": 13,
  "analysis_date": "2025-12-28",
  "boat_admin": {
    "subtasks": 28,
    "completed": 15,
    "velocity": 0.56
  },
  "barge_admin": {
    "subtasks": 21,
    "completed": 1
  },
  "epic_total": {
    "subtasks": 64,
    "completion_pct": 25
  }
}
```

---

## Parameters (Optional)

Usage: `/ibops-sprint [options]`

### Mode Selection
- **(default)**: Full sprint report with Fathom integration
- `--include-admin-velocity`: Add Admin epic analysis to full sprint report (both reports generated)
- `--admin-only`: Generate only Admin epic analysis (legacy mode, no Fathom)
- `--skip-meetings`: Skip Fathom integration (Jira-only report, faster)

### General Options (Both Modes)
- `--sprint N`: Specify sprint number (default: auto-detect from Jira)
- `--compare-to DATE`: Compare to specific checkpoint date (e.g., `--compare-to 2025-12-15`)
- `--meeting-filter KEYWORD`: Override meeting filter (default: "iBOPS OR BOPS")

### Admin Velocity Mode Options (when --include-admin-velocity or --admin-only)
- `--skip-slides`: Skip Gamma slide generation (faster, table + analysis only)
- `--focus SCREEN`: Deep-dive on specific admin screen (e.g., `--focus Barge`)
- `--quick`: Generate simple table only (fastest, no velocity analysis)

### Full Sprint Mode Options
- `--skip-sprint-slides`: Skip Sprint Review Gamma generation (faster, report only)
- `--skip-checkpoint`: Don't save sprint checkpoint (report only)
- `--format {concise|detailed}`: Report format (default: concise, matches Sprint 11 PDF)

**Examples:**

**Full Sprint Report (Default):**
- `/ibops-sprint` - Full sprint report with Jira + Fathom insights + Sprint Review Gamma (DEFAULT)
- `/ibops-sprint --sprint 13` - Explicit sprint number
- `/ibops-sprint --skip-meetings` - Jira-only report (faster, no Fathom)
- `/ibops-sprint --skip-sprint-slides` - Skip Sprint Review Gamma (faster, report only)
- `/ibops-sprint --meeting-filter "BargeOps"` - Override meeting filter

**Admin Velocity Analysis:**
- `/ibops-sprint --admin-only` - Admin epic analysis only (no full sprint)
- `/ibops-sprint --admin-only --sprint 13` - Specific sprint number
- `/ibops-sprint --admin-only --skip-slides` - Table + analysis, no Gamma deck
- `/ibops-sprint --admin-only --focus Barge` - Deep dive on Barge Admin

**Combined Reports:**
- `/ibops-sprint --include-admin-velocity` - Full sprint + admin analysis
- `/ibops-sprint --include-admin-velocity --sprint 13` - Explicit sprint

**Migration from old skill:**
- `/admin-velocity` → `/ibops-sprint --admin-only`
- `/admin-velocity --full-sprint` → `/ibops-sprint`
- `/admin-velocity --both` → `/ibops-sprint --include-admin-velocity`

---

## Output Path Configuration

### Standard Output Location
All skill outputs saved to OneDrive:
```
C:\Users\layden\OneDrive - Cornerstone Solutions Group\Desktop\Internal BOPS Team\iBOPS Sprint Reports\Automated Sprint Reports\Sprint {N} ({dates})\
```

**Folder Structure Created Automatically:**
- `Sprint {N} ({dates})\` - Created per skill run with sprint number and date range
- Inside each sprint folder:
  - Full sprint status report
  - Sprint Review Gamma presentation (4 slides)
  - Admin velocity analysis reports (if `--include-admin-velocity` used)

**Example:** Running `/ibops-sprint --sprint 12` creates:
```
Automated Sprint Reports\
└── Sprint 12 (Dec 15 - Dec 29)\
    ├── iBOPS FY25 Agile Team - Status Report Sprint 12 (Dec 15 - Dec 29).md
    └── Sprint-Review-Gamma-Sprint-12.md
```

### Checkpoint Storage (Unchanged)
Checkpoints remain in `.claude-sessions/` (local, not OneDrive) for fast access:
- `.claude-sessions/ibops-sprint-full-{N}-{YYYY-MM-DD}.json` - Full sprint checkpoints
- `.claude-sessions/ibops-sprint-admin-{YYYY-MM-DD}.json` - Admin velocity checkpoints

**Rationale:** OneDrive sync delays (1-5 seconds) would slow checkpoint comparisons. Local storage ensures instant access.

---

## Error Handling

### Fathom Integration Failures

**Scenarios and Fallbacks:**
- **Fathom MCP not configured** → Skip meeting integration, generate Jira-only report, display warning
- **Fathom API key invalid** → Skip meeting integration, generate Jira-only report, display warning
- **No meetings found** → Continue with Jira-only report (no meeting insights added)
- **Fathom API timeout (>30s)** → Skip meeting processing, continue with Jira data, display warning
- **Meeting search error** → Log error, continue with Jira-only report

**User Notification Format:**
```
⚠️ Fathom meeting integration skipped (reason: MCP server not available)
Generating Jira-only sprint report...
Tip: Use --skip-meetings flag to suppress this warning
```

**Graceful Degradation:**
```
Full Sprint Report (with Fathom)
    ↓ (Fathom unavailable)
Full Sprint Report (Jira-only)
    ↓ (Jira unavailable)
SKILL FAILS (cannot proceed)
```

### Checkpoint Migration (v2.0 → v3.0)

**Backward Compatibility:**
- Old checkpoints automatically detected and loaded:
  - `.claude-sessions/admin-velocity-*.json` → migrated to new format
  - `.claude-sessions/sprint-*.json` → migrated with `fathom_integration.enabled: false`
- New checkpoints saved with new naming:
  - `.claude-sessions/ibops-sprint-full-*.json`
  - `.claude-sessions/ibops-sprint-admin-*.json`

**Migration Logic (Auto-Applied During Checkpoint Load):**

1. **Detect Old Checkpoint Format:**
   ```python
   # Check if checkpoint is missing 'fathom_integration' section
   if 'fathom_integration' not in checkpoint_data:
       # This is a v2.0 checkpoint, needs migration
       migrate_checkpoint_to_v3(checkpoint_data)
   ```

2. **Add Missing Fathom Integration Section:**
   ```python
   # Default values for migrated checkpoints
   checkpoint_data['fathom_integration'] = {
       "enabled": false,
       "meetings_fetched": 0,
       "meetings_processed": 0,
       "filter_used": "N/A (pre-v3.0 checkpoint)",
       "insights_extracted": {
           "accomplishments": 0,
           "decisions": 0,
           "blockers": 0
       },
       "meeting_list": [],
       "migration_note": "Checkpoint migrated from v2.0 to v3.0 format"
   }
   ```

3. **Preserve All Existing Data:**
   - Do NOT modify existing fields (sprint_number, metrics, team_contributions, etc.)
   - Only ADD the missing `fathom_integration` section
   - Original checkpoint file remains unchanged on disk
   - Migration happens in-memory during load

4. **Migration Verification:**
   - After migration, checkpoint_data should validate against v3.0 schema
   - Log migration: "ℹ️ Loaded v2.0 checkpoint, migrated to v3.0 format (Fathom disabled)"
   - User sees seamless experience (no errors, no manual intervention)

**Example Migration:**

**Before (v2.0 checkpoint):**
```json
{
  "timestamp": "2025-12-15T14:00:00",
  "sprint_number": 11,
  "metrics": {
    "total_issues": 65,
    "completed": 18,
    "completion_pct": 27.7
  },
  "by_status": { ... },
  "team_contributions": { ... }
}
```

**After Migration (v3.0 format, in-memory):**
```json
{
  "timestamp": "2025-12-15T14:00:00",
  "sprint_number": 11,
  "metrics": {
    "total_issues": 65,
    "completed": 18,
    "completion_pct": 27.7
  },
  "by_status": { ... },
  "team_contributions": { ... },
  "fathom_integration": {
    "enabled": false,
    "meetings_fetched": 0,
    "meetings_processed": 0,
    "filter_used": "N/A (pre-v3.0 checkpoint)",
    "insights_extracted": {
      "accomplishments": 0,
      "decisions": 0,
      "blockers": 0
    },
    "meeting_list": [],
    "migration_note": "Checkpoint migrated from v2.0 to v3.0 format"
  }
}
```

**When to Apply Migration:**
- **During checkpoint load:** Before using checkpoint data for comparison
- **NOT during checkpoint save:** Always save with v3.0 schema (full `fathom_integration` section)
- **Every time:** Check for missing section on each load (idempotent operation)

---

## Key Principles (Always Follow)

1. **Conservative Forecasting** (Admin Mode):
   - Only project completion dates for screens with validation data
   - Barge Admin = validation gate
   - Don't project remaining 5 screens until Barge Admin validates velocity

2. **Meeting Synthesis** (Full Sprint Mode):
   - Keep insights concise (2-5 bullets per section, 1 sentence max)
   - Add light attribution ("From sprint planning:", "From retrospective:")
   - Deduplicate with Jira data (don't repeat information)
   - Filter for relevance (skip off-topic discussions)

3. **Scope Transparency**:
   - Always show scope changes (subtasks added/removed)
   - Explain why scope changed (demo discoveries, refinements)
   - Distinguish "scope creep" from "scope discovery"

4. **Sprint-Over-Sprint Comparison**:
   - Load previous checkpoint if exists
   - Show deltas for all metrics (±X subtasks, ±Y% velocity)
   - Flag concerning trends (velocity decrease, scope explosion)

5. **Error Resilience**:
   - Fathom failures don't block report generation
   - Always produce Jira-based report as fallback
   - Warn user but continue execution

---

## Output Files Created

**All reports saved to:**
`C:\Users\layden\OneDrive - Cornerstone Solutions Group\Desktop\Internal BOPS Team\iBOPS Sprint Reports\Automated Sprint Reports\Sprint {N} ({dates})\`

**Checkpoints saved to (local, not OneDrive):**
`.claude-sessions/`

---

### Full Sprint Mode (Default)
**Outputs created in** `Automated Sprint Reports\Sprint {N} ({dates})\`:
1. **`iBOPS FY25 Agile Team - Status Report Sprint {N} ({dates}).md`** - Executive sprint report with meeting insights
2. **`Sprint-Review-Gamma-Sprint-{N}.md`** - 4-slide Gamma presentation (unless `--skip-sprint-slides`)

**Checkpoint (local):**
3. **`.claude-sessions/ibops-sprint-full-{N}-{YYYY-MM-DD}.json`** - Sprint checkpoint with Fathom metadata

### Admin Velocity Mode (--admin-only or --include-admin-velocity)
**Outputs created in** `Automated Sprint Reports\Sprint {N} ({dates})\`:
1. **`Admin-Screens-Progress-Sprint-{N}.md`** - Simple table (Sprint 11 PDF format)
2. **`Admin-Velocity-Analysis-Sprint-{N}.md`** - Full narrative analysis
3. **`Admin-Velocity-Gamma-Sprint-{N}.md`** - 10-slide Gamma presentation (unless `--skip-slides`)

**Checkpoint (local):**
4. **`.claude-sessions/ibops-sprint-admin-{YYYY-MM-DD}.json`** - Admin checkpoint

### Combined Mode (--include-admin-velocity)
All of the above files from both modes (5 files total: 2 from Full Sprint + 3 from Admin Velocity + 2 checkpoints)

---

## Integration with Existing Files

### Full Sprint Mode References
- **Jira Board:** Board 38 (BargeOps Agile Team Board)
- **Project:** BOPS (BargeOps)
- **Active Sprint:** Auto-detected from board
- **All Epics:** BOPS-3343 (Crewing), BOPS-3515 (Admin), BOPS-3657 (BI Work), etc.
- **Previous Sprint Reports:** Located in `OneDrive - Cornerstone Solutions Group\Desktop\Internal BOPS Team\iBOPS Sprint Reports\`
- **Fathom Meetings:** Auto-fetched by title filter ("iBOPS" OR "BOPS") and date range

### Admin Velocity Mode References
- **Jira Epic:** BOPS-3515 (Admin Web App v2)
- **Boat Admin:** BOPS-3533 (baseline velocity source)
- **Barge Admin:** BOPS-3517 (validation sprint)
- **Demo Issues:** Documented in Barge Admin demo MD files
- **Previous Analyses:** Sprint 11 baseline, earlier progress reports

---

## Workflow

### Full Sprint Mode Workflow (Default)
1. User invokes: `/ibops-sprint` (or `/ibops-sprint --sprint 13`)
2. Skill fetches active sprint from Board 38 (all issues) via Jira MCP
3. Skill fetches iBOPS meetings from Fathom MCP (title filter, date range)
4. Skill loads previous sprint checkpoint (if exists) from `.claude-sessions/`
5. Skill calculates sprint metrics (status breakdown, team contributions, completion rate)
6. Skill extracts meeting insights (accomplishments, decisions, blockers)
7. Skill synthesizes insights into report sections (deduplicate, add attribution)
8. Skill creates sprint-specific output folder in OneDrive (if needed): `Automated Sprint Reports\Sprint {N} ({dates})\`
9. Skill generates sprint report matching Sprint 11 PDF format (with meeting insights)
10. Skill generates Sprint Review Gamma presentation (4 slides) unless `--skip-sprint-slides` is used
11. Skill saves outputs to OneDrive folder (sprint report + Sprint Review Gamma)
12. Skill saves new sprint checkpoint (with Fathom metadata) to `.claude-sessions/` for next sprint comparison
13. User gets summary of sprint health, report location (OneDrive path), and meeting insights count

### Admin Velocity Mode Workflow (--admin-only)
1. User invokes: `/ibops-sprint --admin-only` (or with Admin-specific parameters)
2. Skill fetches Admin epic BOPS-3515 and all child issues via Jira MCP
3. Skill loads previous admin checkpoint (if exists) from `.claude-sessions/`
4. Skill calculates velocity metrics (baseline, projected) and compares to previous sprint
5. Skill creates sprint-specific output folder in OneDrive (if needed): `Automated Sprint Reports\Sprint {N} ({dates})\`
6. Skill generates 3 reports (progress table, velocity analysis, Admin Velocity Gamma slides)
7. Skill saves reports to OneDrive folder
8. Skill saves new admin checkpoint to `.claude-sessions/` for next sprint comparison
9. User gets summary of files created (OneDrive path) and key velocity findings

---

## Success Metrics

### Full Sprint Mode Success Criteria
After running `/ibops-sprint`, you should have:
- ✅ Complete sprint status across all work streams (Jira metrics)
- ✅ Meeting insights blended into Accomplishments, Decisions, and Blockers sections
- ✅ Team contribution breakdown with completion rates
- ✅ Executive summary in Sprint 11 PDF format
- ✅ Sprint Review Gamma presentation (4 slides) for stakeholder presentations
- ✅ All outputs saved to OneDrive folder: `Automated Sprint Reports\Sprint {N} ({dates})\`
- ✅ Saved sprint checkpoint with Fathom metadata (in `.claude-sessions/`) for next retrospective

### Admin Velocity Mode Success Criteria
After running `/ibops-sprint --admin-only`, you should have:
- ✅ Clear velocity baseline and projections for Admin epic
- ✅ Sprint-over-sprint comparison showing Admin screens progress
- ✅ Presentation-ready Admin Velocity Gamma slides (10 slides) for stakeholders
- ✅ Conservative forecasting with validation gates
- ✅ All outputs saved to OneDrive folder: `Automated Sprint Reports\Sprint {N} ({dates})\`
- ✅ Saved admin checkpoint (in `.claude-sessions/`) for next sprint review

---

## Notes

### Full Sprint Mode
- **Fathom Integration:** Automatically fetches meetings if MCP configured; gracefully skips if unavailable
- **Meeting Filter:** Default "iBOPS OR BOPS" in title; override with `--meeting-filter`
- **Synthesis Quality:** Meeting insights are concise (1 sentence max, 2-5 per section)
- **Attribution Style:** Light prefixes ("From sprint planning:") for context
- **Deduplication:** Removes redundant info (if Jira shows done, skip meeting mention)
- **Error Handling:** Fathom failures don't block report; falls back to Jira-only

### Admin Velocity Mode
- **First Run:** No previous checkpoint exists, skill will note this and create baseline
- **Subsequent Runs:** Automatic comparison to previous sprint
- **Scope Changes:** Skill detects and explains subtask additions/removals
- **Demo Issues:** Skill incorporates demo findings (e.g., Barge Admin's 17 issues)

### Both Modes
- **Jira MCP Required:** Skill uses Jira MCP server for data fetching (mandatory)
- **Fathom MCP Optional:** Meeting integration requires Fathom MCP (optional, graceful fallback)
- **Backward Compatible:** Old checkpoints automatically migrated when loaded
- **Output Location:** Reports saved to current directory (or OneDrive path for full sprint reports)
- **Checkpoint Storage:** All checkpoints saved to `.claude-sessions/` directory
- **Date Format:** Uses ISO format (YYYY-MM-DD) for consistency

---

**Created:** December 28, 2025
**Last Updated:** December 30, 2025
**Skill Type:** Workflow / Reporting (Dual-Mode with Fathom Integration)
**Category:** Project Management, Velocity Tracking, Sprint Reporting, Meeting Synthesis
**Modes:** Full Sprint Report (with Fathom) | Admin Epic Velocity Analysis
