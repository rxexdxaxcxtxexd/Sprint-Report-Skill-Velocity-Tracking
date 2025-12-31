# iBOPS FY25 Agile Team - Status Report
## Sprint 12 (December 15 - December 29, 2025)

---

## Sprint 11 Goals (Previous Sprint)

### Deliverables
- Complete BI work deployment to production
- Continue Boat Admin V2 development
- Address CTC BI support issues
- Progress Crewing Module features

### Process
- Establish agile team cadence
- Demo-driven development approach

---

## Key Accomplishments ✅

### 1. **Parker Towing Co. Customization Epic - COMPLETED** (BOPS-3345)
- **Status:** Done (December 17, 2025)
- Entire TVR Form customization epic closed
- Seamless deployment with zero rollback
- From Sprint Review: "Team celebrated successful completion"

### 2. **Boat Admin V2 - Major Progress** (BOPS-3533)
- **Completed:** 17 demo/QA fixes addressing SME feedback
- **Current Status:** 48% complete (13 of 27 active tasks)
- **Scope Discovery:** 4 additional screens identified (Fuel Price, Status, Global Settings, Position History)
- From Sprint Review: "Boat admin screen completed and held demo with Barge admin SME"

**Completed Tasks (13):**
- Navigation list filtering (BOPS-3613)
- Asset Management grouping (BOPS-3612)
- Active/Inactive button behavior (BOPS-3611)
- Position History placement (BOPS-3610)
- Enable Onboard license control (BOPS-3608)
- Business Unit field logic (BOPS-3607)
- Track Position in AIS fix (BOPS-3606)
- Time format - military time (BOPS-3604)
- Required fields validation (BOPS-3603)
- River mile logic (BOPS-3602)
- Add-screen river mile translation (BOPS-3601)
- HP/Business Unit columns (BOPS-3599)
- Fleet Only vs Business Unit Boats Only label (BOPS-3598)

### 3. **Barge Admin V2 - Validation Sprint Initiated** (BOPS-3517)
- **Demo Held:** December 22 with SME
- **Issues Identified:** 17 items for AI-driven testing approach
- **Completed:** Barge Loading Timeout fix (BOPS-3628)
- **Strategy:** AI agent tackles bulk of issues, human review for remaining
- From Barge Admin Demo: "17 issues identified for AI agent to tackle with human review"

### 4. **Crewing Module Features** (BOPS-3343)
- **Completed:** Delete boat manning requirement (BOPS-3648)
- **Completed:** Zero manning requirement visibility fix (BOPS-3647)
- Epic continues with ongoing enhancements

### 5. **CTC BI Support & Bug Fixes**
- Item Types bug fix (BOPS-3640) - Complete
- Transform update for item type bug (BOPS-3638) - Complete
- Division override fix for Outside Vendor (BOPS-3558) - Complete
- Barge Trip Power BI Report (BOPS-3476) - IN CSG QA/UVT

---

## Decisions & Discussions 💡

### Process Improvements (Sprint 12)
1. **Story Point Estimates** - Now required on all tickets (Dec 18)
   - From Stand-Up: "Team agreed to start including story point estimates on all tickets moving forward"
2. **Playwright Test Artifacts** - Captured in JIRA for traceability (Dec 18)
   - From Stand-Up: "Capturing Playwright test artifacts (reports, recordings) in JIRA tickets to improve visibility"
3. **AI-Driven QA Approach** - Approved for Barge Admin 17 issues (Dec 22)
   - From Sprint Review: "AI-driven testing approach for barge admin identified issues"

### UI/UX Standards (From Barge Admin Demo - Dec 22)
4. **Consistent Delete/Deactivate Pattern** - Single button with confirmation prompt
   - From Demo: "Establishing consistent UI patterns, such as having a single delete/deactivate button"
5. **Button Labels** - Use "Search and Clear" pattern (from Liquids app)
   - From Demo: "Agreed to use the Search and Clear button labels seen in the Liquids app"
6. **Action Button Placement** - Top-right corner of screens
   - From Demo: "Position the action buttons in the top-right corner of screens"
7. **Barge Search Optimization** - Swap load status with cover type field
   - From Demo: "Cover type is a more static property whereas load status can change frequently"

### Strategic Decisions
8. **Velocity Reporting** - Using Boat Admin as baseline for projections
   - From Sprint Review: "Plans to provide more detailed velocity reporting, using boat admin screen as baseline"
9. **Fluid Task Management** - Less JIRA overhead, more collaborative approach
   - From Barge Admin Demo: "Take a more fluid approach to assigning and tracking tasks rather than relying heavily on JIRA"
10. **Screen Prioritization** - Vendor and River Area screens prioritized for Barge Admin v1
   - From Barge Admin Demo: "Prioritizing the vendor and river area screens for the initial release"

---

## Blockers & Risks ⚠️

### Active Blockers
1. **Business Unit Lookup Missing** (BOPS-3600) - Ready for Dev
   - Blocks final boat admin validation
   - Requires fleetID mapping implementation

### Risks
2. **Scope Expansion Risk**
   - 4 additional Boat Admin screens discovered in Sprint 12
   - From Sprint Review: "4 additional screens were identified and added to the scope"
   - Impact: Extended timeline for Boat Admin completion

3. **FAC Tables ETL Backlog**
   - 27 subtasks total: 9 in code review, 18 ready for dev
   - Resource contention with GIA priorities
   - Paulette juggling multiple work streams

4. **Dimension Table Transition Risk**
   - Potential role change for key resource
   - Need to wrap up dimension tables before transition

---

## Sprint 13 Goals (Next Sprint)

### Deliverables
- **Boat Admin V2** - Complete remaining 9 subtasks (target: 75%+ completion)
- **Barge Admin V2** - Complete 3 remaining subtasks (Final UI, API, QA Artifacts)
- **Licensing Integration** - Complete license-dependent filters and enforcement
- **FAC Tables ETL** - Progress on 9 in-review tasks

### Process
- Velocity baseline reporting active (Boat Admin as reference)
- Daily Barge Admin velocity tracking vs baseline (0.56 tasks/day)
- Validation gate decision by Jan 12 (greenlight remaining 5 admin screens or adjust)

**Note:** Sprint 13 is a modified sprint (9 effective days) due to holiday period

---

## Team Capacity & Focus

| Team Member | Sprint 12 Completion | In Progress (Sprint 13) | Completion Rate |
|------------|---------------------|------------------------|----------------|
| **Doug Romano** | 11 tasks | 0 | 84.6% (11/13) |
| **Viktor Dubrovin** | 3 tasks | 4 | 37.5% (3/8) |
| **Derick Mayberry** | Active development | 2 | N/A (new to team) |
| **Paulette Whaley** | 1 task | 2 | 7.1% (1/14) - GIA contention |
| **Jan Lange** | 2 tasks | 1 | 100% (2/2) |
| **Janice Mattox** | Support tasks | 1 | Active |
| **Kal Miller** | BI work | 1 | In QA |
| **Mark Maxwell** | 1 task | 0 | 50% (1/2) |
| **Unassigned** | 4 tasks | 2 | 13.3% (4/30) |

**Top Contributor:** Doug Romano (11 tasks completed - 50% of all completions)

---

## Sprint Metrics

### Overall Status (77 issues)
- **Done:** 22 (28.6%)
- **In Progress:** 6 (7.8%)
- **In Code Review:** 9 (11.7%)
- **IN CSG QA/UVT:** 5 (6.5%)
- **In UAT:** 1 (1.3%)
- **Ready for Dev:** 18 (23.4%)
- **New:** 9 (11.7%)
- **Obsolete:** 7 (9.1%)

### By Issue Type
- **Epics:** 2 (1 done, 1 in progress)
- **Tasks:** 9 (1 done, 5 in progress/review, 3 ready/new)
- **Sub-tasks:** 60 (18 done, 39 in progress/ready, 3 new)
- **Bugs:** 6 (2 done, 2 in progress/review, 2 new)

### Velocity
- **Sprint Duration:** 14 days (Dec 15-29)
- **Tasks Completed:** 22
- **Velocity:** 1.57 tasks/day
- **Note:** Overall sprint velocity including all issue types

**Admin Web App V2 Epic Velocity:**
- **Boat Admin Tasks Completed:** 13 (Sprint 12 only)
- **Sprint 12 Velocity:** 0.93 tasks/day
- **Baseline Velocity:** 0.56 tasks/day (historical average from Nov 7 - Dec 29)
- **Performance:** 166% of baseline (sustained peak from Sprint 11)

---

## Meeting Insights Summary

**Meetings Processed:** 7 iBOPS meetings (Dec 17-30)
- Sprint 12 Review (Dec 29)
- Daily Stand-Ups (Dec 17, 18, 22, 29, 30)
- Barge Admin QA Demo (Dec 22)

**Key Themes:**
- ✅ Velocity reporting and metrics tracking emphasized
- ✅ Consistent UI patterns established (delete/deactivate, Search/Clear)
- ✅ AI-driven QA approach approved for Barge Admin
- ✅ Story point estimates and Playwright artifacts now standard
- ✅ Team celebrated Parker Towing Co. Epic completion

---

**Report Generated:** December 30, 2025
**Data Sources:** Jira Board 38 (Sprint 2340 - 77 issues) + Fathom Meetings (7 meetings)
**Next Sprint Review:** January 12, 2026 (Sprint 13)

---

*🤖 Generated with iBOPS Sprint Reporting Skill v3.0 (Full Sprint Mode with Fathom Integration)*
