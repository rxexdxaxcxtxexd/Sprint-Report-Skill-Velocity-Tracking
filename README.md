# Sprint Report Skill & Velocity Tracking

**Automated sprint reporting and velocity analysis for Agile teams using Claude Code + Jira MCP**

[![Claude Code](https://img.shields.io/badge/Claude-Code-purple)](https://claude.com/claude-code)
[![Jira](https://img.shields.io/badge/Jira-MCP-blue)](https://www.atlassian.com/software/jira)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Overview

This Claude Code skill provides **dual-mode sprint reporting**:

1. **Admin Epic Velocity Analysis** - Deep-dive velocity tracking for specific epics with forecasting
2. **Full Sprint Reporting** - Executive sprint summaries covering all work streams

Built for the BargeOps project, but **adaptable to any Jira Agile team**.

## Features

### 🚀 Dual-Mode Operation

**Mode 1: Epic Velocity Analysis**
- Track velocity for specific epic (e.g., Admin Web App V2)
- Calculate baseline velocity from historical data
- Project completion dates with conservative/realistic/optimistic scenarios
- Generate Gamma-ready presentation slides
- Sprint-over-sprint comparison with delta analysis

**Mode 2: Full Sprint Reporting**
- Comprehensive sprint status (all issues, not just one epic)
- Team contribution breakdown with completion rates
- Status distribution (Done, In Progress, In Review, etc.)
- Blocker and risk identification
- Executive format matching standard sprint review PDFs

### 📊 Automated Metrics

- **Velocity calculation** (tasks/day)
- **Completion rates** (%)
- **Team contributions** (per assignee)
- **Quality metrics** (bugs found vs fixed)
- **Sprint health indicators**

### 💾 Checkpoint System

- **Automatic checkpointing** after each run
- **Sprint-over-sprint comparison** showing deltas
- **Scope change tracking** (subtasks added/removed)
- **Trend analysis** (velocity acceleration/deceleration)

### 🎯 Smart Forecasting

- **Validation gates** before projecting future work
- **Improvement factors** (+30% process, +40% team expansion)
- **Three scenarios** (conservative, realistic, optimistic)
- **Transparent assumptions** (no black-box predictions)

## Quick Start

### Prerequisites

1. **Claude Code** installed and configured
2. **Jira MCP server** connected (for fetching Jira data)
3. **Active Jira board** with sprint tracking

### Installation

1. **Copy the skill definition:**
   ```bash
   cp skill-definition.md ~/.claude/skills/admin-velocity.md
   ```

2. **Copy the checkpoint script (optional):**
   ```bash
   cp admin-velocity-checkpoint.py ~/scripts/
   ```

3. **Reload Claude Code** or restart to load the skill

### Usage

#### Full Sprint Report (All Issues)
```bash
/admin-velocity --full-sprint
```

**Output:**
- `iBOPS FY25 Agile Team - Status Report Sprint N (dates).md`
- Sprint checkpoint: `.claude-sessions/sprint-N-YYYY-MM-DD.json`

#### Epic Velocity Analysis
```bash
/admin-velocity
```

**Output:**
- `Admin-Screens-Progress-Sprint-N.md` (simple table)
- `Admin-Velocity-Analysis-Sprint-N.md` (full narrative)
- `Admin-Velocity-Gamma-Sprint-N.md` (presentation slides)
- Epic checkpoint: `.claude-sessions/admin-velocity-YYYY-MM-DD.json`

#### Both Reports
```bash
/admin-velocity --both
```

**Output:** All files from both modes

## Examples

### Example: Sprint 12 Full Report

See [`examples/Sprint-12-Report-Example.md`](examples/Sprint-12-Report-Example.md) for a complete sprint report.

**Sprint 12 Highlights:**
- 77 total issues (2 Epics, 9 Tasks, 60 Sub-tasks, 6 Bugs)
- 23 completed (29.9%)
- Parker Towing Customization Epic ✅ DONE
- 13 Boat Admin v2 fixes deployed
- Identified: Barge Admin v2 not started (blocker)

### Example: Velocity Analysis Output

```
SPRINT-OVER-SPRINT COMPARISON
======================================
[BOAT] Boat Admin (BOPS-3533):
  Subtasks: 24 → 28 (+4)
  Completed: 13 → 15 (+2)
  Completion: 54% → 54% (+0%)
  Velocity: 0.56 tasks/day (baseline)

[BARGE] Barge Admin (BOPS-3517):
  Subtasks: 4 → 21 (+17)
  Completed: 0 → 1 (+1)
  Completion: 0% → 5% (+5%)
  Velocity: TBD (validation sprint)

[EPIC] Epic Total (BOPS-3515):
  Subtasks: 43 → 64 (+21)
  Completed: 13 → 16 (+3)
  Completion: 30% → 25% (-5%)
  Note: Scope expansion from demo discoveries
```

## Configuration

### Customize for Your Project

Edit `skill-definition.md` to adapt to your Jira setup:

1. **Board ID:** Change from Board 38 to your board ID
   ```markdown
   Get active sprint from BargeOps Agile Team Board (Board 38)
   ```

2. **Epic Key:** Change from BOPS-3515 to your epic
   ```markdown
   Get epic BOPS-3515 and all child issues
   ```

3. **Project Key:** Change from BOPS to your project
   ```markdown
   project: "BOPS"
   ```

4. **Report Path:** Update output location
   ```markdown
   OneDrive - Cornerstone Solutions Group\Desktop\Internal BOPS Team\iBOPS Sprint Reports\
   ```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--full-sprint` | Generate full sprint report | `/admin-velocity --full-sprint` |
| `--both` | Generate both modes | `/admin-velocity --both` |
| `--sprint N` | Specify sprint number | `/admin-velocity --sprint 12` |
| `--compare-to DATE` | Compare to specific checkpoint | `/admin-velocity --compare-to 2025-12-15` |
| `--skip-slides` | Skip Gamma slides (faster) | `/admin-velocity --skip-slides` |
| `--quick` | Simple table only | `/admin-velocity --quick` |
| `--focus SCREEN` | Deep-dive on specific item | `/admin-velocity --focus Barge` |

## Architecture

```
sprint-report-skill/
├── skill-definition.md           # Claude Code skill (main entrypoint)
├── admin-velocity-checkpoint.py  # Manual checkpoint script (optional)
├── README.md                      # This file
├── ENHANCED-FEATURES.md          # Detailed feature documentation
├── examples/
│   └── Sprint-12-Report-Example.md  # Example output
└── .claude-sessions/              # Checkpoints (auto-created)
    ├── admin-velocity-YYYY-MM-DD.json
    └── sprint-N-YYYY-MM-DD.json
```

### How It Works

1. **Skill invoked** via `/admin-velocity [options]`
2. **Claude Code** reads skill definition from `.claude/skills/admin-velocity.md`
3. **Jira MCP** fetches sprint/epic data via Atlassian API
4. **Metrics calculated** (velocity, completion rates, etc.)
5. **Previous checkpoint loaded** (if exists) for comparison
6. **Reports generated** (Markdown format)
7. **New checkpoint saved** for next sprint

## Use Cases

### 1. Sprint Retrospectives
Generate comprehensive sprint reports for team retrospectives:
```bash
/admin-velocity --full-sprint
```

### 2. Stakeholder Updates
Create executive summaries for stakeholder meetings:
```bash
/admin-velocity --full-sprint --format concise
```

### 3. Velocity Forecasting
Track epic velocity and forecast completion:
```bash
/admin-velocity --focus Barge
```

### 4. Mid-Sprint Check-ins
Quick progress check without full analysis:
```bash
/admin-velocity --quick
```

### 5. Quarterly Reviews
Comprehensive analysis with all reports:
```bash
/admin-velocity --both
```

## Troubleshooting

### Issue: "No sprint found"
**Cause:** Board has no active sprint
**Solution:** Use `--sprint N` to specify sprint number

### Issue: "Jira MCP not connected"
**Cause:** Jira MCP server not running
**Solution:** Check `.claude/settings.json` and restart MCP server

### Issue: "Checkpoint comparison shows unexpected changes"
**Cause:** Different checkpoint types being compared
**Solution:** Ensure comparing admin vs admin, or sprint vs sprint

## Contributing

This is an open-source skill! Contributions welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Support for multiple boards (multi-team reporting)
- [ ] Burndown chart generation (visual velocity tracking)
- [ ] Slack/Teams integration (automated posting)
- [ ] Custom metrics plugins (extend with your own calculations)
- [ ] Historical trend analysis (6-month velocity dashboard)
- [ ] AI-powered risk prediction (ML-based blocker detection)

## License

MIT License - See [LICENSE](LICENSE) for details

## Credits

**Built with:**
- [Claude Code](https://claude.com/claude-code) - AI-powered coding assistant
- [Jira MCP](https://github.com/modelcontextprotocol/servers) - Jira integration via MCP
- [BargeOps Project](https://csgsolutions.atlassian.net/jira/software/c/projects/BOPS) - Real-world testing

**Created by:** Claude Code (Sonnet 4.5) + Human collaboration
**Date:** December 2025
**Version:** 2.0 (Dual-Mode)

## Support

- **Issues:** [GitHub Issues](https://github.com/rxexdxaxcxtxexd/Sprint-Report-Skill-Velocity-Tracking/issues)
- **Discussions:** [GitHub Discussions](https://github.com/rxexdxaxcxtxexd/Sprint-Report-Skill-Velocity-Tracking/discussions)
- **Documentation:** See [ENHANCED-FEATURES.md](ENHANCED-FEATURES.md) for detailed feature docs

---

**⭐ Star this repo if you find it useful!**

**🔗 Share with your team** to improve your sprint reporting process!
