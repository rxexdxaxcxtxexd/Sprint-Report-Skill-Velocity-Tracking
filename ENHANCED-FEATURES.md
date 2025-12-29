# Admin Velocity Skill - ENHANCED (Dec 29, 2025)

## What Changed?

The `/admin-velocity` skill now has **TWO MODES**:

### Mode 1: Admin Epic Analysis (Original Behavior)
✅ **Focus:** Admin Web App V2 Epic (BOPS-3515)
✅ **Purpose:** Velocity tracking for Boat/Barge Admin screens
✅ **Outputs:** Progress table, velocity analysis, Gamma slides

### Mode 2: Full Sprint Reporting (NEW!)
🆕 **Focus:** Entire sprint (all 70-80 issues across all epics)
🆕 **Purpose:** Executive sprint report matching Sprint 11 PDF format
🆕 **Outputs:** Sprint status report with team capacity and blockers

---

## Quick Start

### Use Admin Epic Mode (Default)
```bash
/admin-velocity
```
**Result:** Admin Web App epic velocity analysis + Gamma slides

### Use Full Sprint Mode
```bash
/admin-velocity --full-sprint
```
**Result:** Complete sprint report (Sprint 11 PDF style) covering all work

### Generate Both Reports
```bash
/admin-velocity --both
```
**Result:** Admin epic analysis + full sprint report

---

## Full Sprint Report Features

When you run `/admin-velocity --full-sprint`, you get:

### Page 1: Sprint Review
- ✅ **Sprint X Goals** (from previous sprint)
- ✅ **Accomplishments** (what was completed - epics, features, bugs)
- ✅ **Decisions/Discussions** (process changes, strategy shifts)
- ✅ **Blockers/Risks** (current impediments, unassigned work)

### Page 2: Sprint Planning
- ✅ **Sprint X+1 Goals** (current/next sprint goals)
- ✅ **Team Capacity & Focus** (table showing hours and assignments)

### Metrics Calculated
- Status breakdown (Done, In Progress, In Code Review, etc.)
- Issue type distribution (Epics, Tasks, Sub-tasks, Bugs)
- Team contributions (who worked on what, completion rates)
- Completion rate (Done ÷ Total)
- Quality metrics (bugs found vs fixed)

---

## All Available Parameters

### Mode Selection
| Parameter | Description |
|-----------|-------------|
| `--full-sprint` | Generate full sprint report (all issues) |
| `--both` | Generate both Admin epic + full sprint reports |

### General Options (Both Modes)
| Parameter | Description |
|-----------|-------------|
| `--sprint N` | Specify sprint number (auto-detect if omitted) |
| `--compare-to DATE` | Compare to specific checkpoint date |

### Admin Epic Mode Options
| Parameter | Description |
|-----------|-------------|
| `--skip-slides` | Skip Gamma slides (faster) |
| `--focus SCREEN` | Deep-dive on specific screen (e.g., `--focus Barge`) |
| `--quick` | Simple table only (fastest) |

### Full Sprint Mode Options
| Parameter | Description |
|-----------|-------------|
| `--skip-checkpoint` | Don't save sprint checkpoint |
| `--format {concise\|detailed}` | Report format (default: concise) |

---

## Examples

### Scenario 1: End of Sprint 12 - Need Sprint Report
```bash
/admin-velocity --full-sprint --sprint 12
```
**Output:**
- `iBOPS FY25 Agile Team - Status Report Sprint 12 (Dec 15th - Dec 29th).md`
- `.claude-sessions/sprint-12-2025-12-29.json` (checkpoint)

**Contains:**
- Sprint 11 goals (previous sprint)
- Sprint 12 accomplishments
- Decisions/discussions
- Blockers/risks
- Sprint 12/13 goals
- Team capacity table

---

### Scenario 2: Admin Epic Velocity Check
```bash
/admin-velocity
```
**Output:**
- `Admin-Screens-Progress-Sprint-12.md`
- `Admin-Velocity-Analysis-Sprint-12.md`
- `Admin-Velocity-Gamma-Sprint-12.md`
- `.claude-sessions/admin-velocity-2025-12-29.json`

**Contains:**
- Boat/Barge Admin progress
- Velocity metrics (0.56 baseline, 0.90 projected)
- Sprint-over-sprint comparison
- Gamma presentation slides

---

### Scenario 3: Comprehensive Review - Both Reports
```bash
/admin-velocity --both --sprint 12
```
**Output:** ALL files from both modes
- Admin epic analysis (3 files)
- Full sprint report (1 file)
- Both checkpoints (2 files)

**Use Case:** Quarterly review or major milestone where you need both detailed velocity analysis AND high-level sprint summary

---

## Checkpoints & Comparison

### Admin Epic Checkpoints
**Location:** `.claude-sessions/admin-velocity-YYYY-MM-DD.json`
**Contains:** Boat/Barge Admin metrics, velocity trends, scope changes

**Example:**
```json
{
  "sprint": 12,
  "boat_admin": {"subtasks": 28, "completed": 15, "velocity": 0.56},
  "barge_admin": {"subtasks": 21, "completed": 1},
  "epic_total": {"subtasks": 64, "completed": 16, "completion_pct": 25}
}
```

### Full Sprint Checkpoints
**Location:** `.claude-sessions/sprint-N-YYYY-MM-DD.json`
**Contains:** Sprint metrics, status breakdown, team contributions, blockers

**Example:**
```json
{
  "sprint_number": 12,
  "metrics": {"total_issues": 77, "completed": 23, "completion_pct": 29.9},
  "by_status": {"Done": 23, "In Progress": 4, "In Code Review": 8},
  "team_contributions": {"Doug Romano": {"assigned": 13, "completed": 11}}
}
```

---

## Report Output Locations

### Admin Epic Reports
**Default:** Current directory
- `Admin-Screens-Progress-Sprint-{N}.md`
- `Admin-Velocity-Analysis-Sprint-{N}.md`
- `Admin-Velocity-Gamma-Sprint-{N}.md`

### Full Sprint Reports
**Recommended:** OneDrive sprint reports folder
- `C:\Users\layden\OneDrive - Cornerstone Solutions Group\Desktop\Internal BOPS Team\iBOPS Sprint Reports\iBOPS FY25 Agile Team - Status Report Sprint {N} ({dates}).md`

---

## Sprint-over-Sprint Comparison

Both modes support automatic comparison to previous sprint:

### Admin Epic Comparison
```
SPRINT-OVER-SPRINT COMPARISON
======================================
[BOAT] Boat Admin (BOPS-3533):
  Subtasks: 24 → 28 (+4)
  Completed: 13 → 15 (+2)
  Completion: 54% → 54% (+0%)

[BARGE] Barge Admin (BOPS-3517):
  Subtasks: 4 → 21 (+17)
  Completed: 0 → 1 (+1)
  Completion: 0% → 5% (+5%)
```

### Full Sprint Comparison
```
SPRINT 11 → SPRINT 12 DELTA
======================================
Total Issues: 65 → 77 (+12)
Completed: 18 → 23 (+5)
Completion Rate: 27.7% → 29.9% (+2.2%)
Team Velocity: 0.82 → 0.71 tasks/day (-13%)
```

---

## When to Use Which Mode?

### Use Admin Epic Mode (`/admin-velocity`) When:
- ✅ Focused on Admin Web App V2 progress only
- ✅ Need detailed velocity projections for Boat/Barge Admin
- ✅ Creating executive Gamma slides for stakeholders
- ✅ Forecasting completion dates with conservative scenarios
- ✅ Deep-diving on specific admin screen progress

### Use Full Sprint Mode (`/admin-velocity --full-sprint`) When:
- ✅ End of sprint retrospective (all work streams)
- ✅ Need team-wide contribution breakdown
- ✅ Reporting to stakeholders on overall sprint health
- ✅ Identifying blockers across entire project
- ✅ Preparing for sprint planning (capacity review)
- ✅ Creating reports matching Sprint 11 PDF format

### Use Both (`/admin-velocity --both`) When:
- ✅ Quarterly reviews or major milestones
- ✅ Comprehensive sprint documentation needed
- ✅ Multiple audiences (technical team + executives)
- ✅ Archival purposes (complete sprint record)

---

## Testing the Enhancement

### Test 1: Full Sprint Report for Sprint 12
```bash
/admin-velocity --full-sprint --sprint 12
```
**Expected Output:**
- File created at OneDrive location
- Sprint 12 report with:
  - Sprint 11 goals
  - Sprint 12 accomplishments (Parker Towing complete, Boat Admin 13 fixes, etc.)
  - Blockers (Barge Admin not started, 34 unassigned items)
  - Team capacity table

### Test 2: Both Modes
```bash
/admin-velocity --both
```
**Expected Output:**
- 5 total files created (3 admin + 1 sprint + 1 checkpoint... wait, 2 checkpoints)
- Admin epic analysis with velocity metrics
- Full sprint report with team contributions

---

## Migration Notes

### Backward Compatibility
✅ **Existing behavior preserved:** Running `/admin-velocity` without parameters works exactly as before
✅ **Existing checkpoints:** Old admin-velocity checkpoints still work
✅ **No breaking changes:** All previous parameters still supported

### New Capabilities
🆕 **Dual-mode operation:** One skill, two reporting modes
🆕 **Full sprint coverage:** Not just Admin epic, all sprint work
🆕 **Executive format:** Matches Sprint 11 PDF style
🆕 **Sprint checkpoints:** Separate checkpoint schema for full sprint mode

---

## Troubleshooting

### Issue: "No sprint found"
**Cause:** Board 38 has no active sprint
**Solution:** Specify sprint number explicitly: `/admin-velocity --full-sprint --sprint 12`

### Issue: "Missing team capacity data"
**Cause:** Full sprint mode estimates capacity from assignments
**Solution:** Provide user input for OOO dates and hours allocation

### Issue: "Checkpoint comparison shows unexpected changes"
**Cause:** Admin epic vs full sprint checkpoints are separate
**Solution:** Ensure you're comparing like-to-like (admin vs admin, sprint vs sprint)

---

## Next Steps

1. **Test the enhanced skill:** Run `/admin-velocity --full-sprint` for Sprint 12
2. **Review the output:** Check if format matches Sprint 11 PDF expectations
3. **Iterate if needed:** Adjust report format, add missing sections
4. **Document learnings:** Update skill based on first real usage

---

**Enhancement Date:** December 29, 2025
**Skill Version:** 2.0 (Dual-Mode)
**Enhanced By:** Claude Code (Sonnet 4.5)
**Status:** ✅ Ready for Testing
