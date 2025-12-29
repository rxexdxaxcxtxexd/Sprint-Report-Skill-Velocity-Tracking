# iBOPS FY25 Agile Team
## Sprint 12 (Dec 15th – Dec 29th)

## Sprint 11 Goals
• Complete Boat Admin, SME demo for Barge Admin (12/17) – **Admin Web App v2 (BOPS-3515)**
• Complete CodeSmith replacement - **CodeSmith Replacement (BOPS-3553)**
• Implement bug fixes for CTC - **CTC BI Gap - BI Work (BOPS-3321)**

## Accomplishments
• **Parker Towing Customization Epic completed** - Parker Towing 2025 Q2 Customizations **(BOPS-3345)**
• **13 Boat Admin v2 fixes deployed** - Demo/QA issues resolved including river mile logic, time formatting, license controls, and navigation improvements – **Admin Web App v2 (BOPS-3515)**
• **Crewing module enhancements** - Manning requirement deletion capability added, zero-manning display bug fixed, 1 item in CSG QA – **Crewing Module (BOPS-3343)**
• **Data quality improvements** - Division override bug fixed, transform updates for item types, database scripts for Liquids app – **BI Work (BOPS-3321, BOPS-3657)**
• **7 obsolete tasks closed** - Technical debt cleanup across Fac Tables work

## Decisions/Discussions
• **Admin Web App v2 progress** **(BOPS-3515):**
  - Boat Admin: 13/24 sub-tasks complete, additional screens in progress
  - Barge Admin: Work not started despite sprint commitment – **requires immediate prioritization**
• **Data Warehouse ETL strategy** **(BOPS-3562):**
  - 7 Fac Tables in code review (Paulette)
  - 14 Fac Tables ready for dev – **need to prioritize top 5 critical tables for Sprint 13**
  - Recommend splitting large backlog across multiple sprints
• **Code review capacity:**
  - 8 items currently in review
  - Need to ensure adequate review bandwidth

## Blockers/Risks
• **Barge Admin v2 not started** - All sub-tasks (UI, API, QA) remain "New" with no assignees – **Admin Web App v2 (BOPS-3517)**
• **Unassigned work** - 34 items have no assignee (16 Ready for Dev, 12 New, 3 Groomed)
• **Fac Tables backlog** - 14 sub-tasks ready for development with limited capacity – **Fac Tables ETL (BOPS-3562)**
• **Outstanding bugs** - 3 bugs need resolution:
  - Revenue Variance in facAccrual (In Code Review) – **(BOPS-3627)**
  - Barge-Only Trips Transform Issue (New) – **(BOPS-3639)**
  - Additional Boat Admin v2 issues groomed but not started

---

## Sprint 13 Goals
• **Complete Boat Admin v2** - Finish remaining screens (Fuel Price, Status, Global Settings), deploy licensing screen, address groomed items – **Admin Web App v2 (BOPS-3533)**
• **Launch Barge Admin v2** - Complete UI, API, and QA artifacts – **Admin Web App v2 (BOPS-3517)**
• **Fac Tables ETL Priority Push** - Complete top 5 critical tables from backlog – **Fac Tables ETL (BOPS-3562)**
• **Close outstanding bugs** - Resolve revenue variance, barge-only trips, and admin app issues – **BI Work (BOPS-3627, BOPS-3639)**
• **Barge Trip Power BI Report** - Complete QA and deploy – **(BOPS-3476)**

## Team Capacity & Focus

| Team Member | Capacity | Focus |
|-------------|----------|-------|
| **Doug** | 80hr iBOPS (Jan 2nd - 5th OOO) | Admin Web App (Boat & Barge Admin v2) |
| **Viktor** | 80hr iBOPS | Admin Web App (Boat & Barge Admin v2) |
| **Derick** | 80hr iBOPS | Admin Web App (Boat Admin v2 screens) |
| **Jan** | 80hr iBOPS | Crewing Module + Onboard Support |
| **Paulette** | 40hr iBOPS 40hr GIA | Fac Tables ETL + BI Issues |
| **Mark** | 20hr CTC 20hr Support 40hr iBOPS | Release + QA + Bug Fixes |
| **Kal** | 6hr iBOPS 74hr GIA | Barge Trip BI Report (As Needed) |
| **Janice** | As Needed | Reports Support (Cargo Storage Invoice) |
| **Luke** | 80hr iBOPS | AI-SDM Admin Web App Support |
| **Matt** | 80hr iBOPS, Support As Needed | CodeSmith Replacement + Support |
