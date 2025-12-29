#!/usr/bin/env python3
"""
Admin Web App Velocity Checkpoint Script
Saves current sprint state for sprint-over-sprint comparison
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def create_checkpoint(
    sprint_num=13,
    boat_subtasks=28,
    boat_completed=15,
    boat_in_progress=4,
    barge_subtasks=21,
    barge_completed=1,
    barge_demo_issues=17,
    epic_total_subtasks=64,
    epic_total_completed=16,
    boat_velocity=0.56,
    sprint_11_velocity=0.93,
    sprint_12_velocity=0.23,
):
    """
    Create a checkpoint with current admin web app metrics

    Args:
        sprint_num: Current sprint number
        boat_subtasks: Total Boat Admin subtasks
        boat_completed: Boat Admin completed subtasks
        boat_in_progress: Boat Admin in-progress subtasks
        barge_subtasks: Total Barge Admin subtasks (including demo issues)
        barge_completed: Barge Admin completed subtasks
        barge_demo_issues: Number of demo issues for Barge Admin
        epic_total_subtasks: Total epic subtasks
        epic_total_completed: Total epic completed subtasks
        boat_velocity: Boat Admin baseline velocity (tasks/day)
        sprint_11_velocity: Sprint 11 velocity (peak)
        sprint_12_velocity: Sprint 12 velocity
    """

    # Calculate derived metrics
    boat_remaining = boat_subtasks - boat_completed - boat_in_progress
    boat_completion_pct = round((boat_completed / boat_subtasks) * 100)

    barge_remaining = barge_subtasks - barge_completed
    barge_completion_pct = round((barge_completed / barge_subtasks) * 100) if barge_subtasks > 0 else 0

    epic_remaining = epic_total_subtasks - epic_total_completed
    epic_completion_pct = round((epic_total_completed / epic_total_subtasks) * 100)

    # Build checkpoint data
    checkpoint = {
        "timestamp": datetime.now().isoformat(),
        "sprint": sprint_num,
        "analysis_date": datetime.now().strftime("%Y-%m-%d"),

        "boat_admin": {
            "issue_key": "BOPS-3533",
            "subtasks": boat_subtasks,
            "completed": boat_completed,
            "in_progress": boat_in_progress,
            "remaining": boat_remaining,
            "completion_pct": boat_completion_pct,
            "days_active": None,  # Calculated by skill from created date
            "velocity": boat_velocity,
            "notes": "Learning phase complete, baseline established"
        },

        "barge_admin": {
            "issue_key": "BOPS-3517",
            "subtasks": barge_subtasks,
            "completed": barge_completed,
            "remaining": barge_remaining,
            "completion_pct": barge_completion_pct,
            "demo_issues": barge_demo_issues,
            "velocity": None,  # Not yet measured
            "notes": "Validation sprint - 17 demo issues from Dec 22"
        },

        "other_screens": {
            "customer": {"issue_key": "BOPS-3516", "subtasks": 3, "completed": 0},
            "facility": {"issue_key": "BOPS-3522", "subtasks": 3, "completed": 0},
            "vendor": {"issue_key": "BOPS-3532", "subtasks": 3, "completed": 0},
            "commodity": {"issue_key": "BOPS-3534", "subtasks": 3, "completed": 0},
            "river": {"issue_key": "BOPS-3535", "subtasks": 3, "completed": 0}
        },

        "epic_total": {
            "issue_key": "BOPS-3515",
            "subtasks": epic_total_subtasks,
            "completed": epic_total_completed,
            "remaining": epic_remaining,
            "completion_pct": epic_completion_pct
        },

        "velocity_trends": {
            "sprint_11": sprint_11_velocity,
            "sprint_12": sprint_12_velocity,
            "baseline": boat_velocity,
            "projected_barge": 0.90,  # Realistic scenario
            "notes": "Sprint 11 = peak (QA burst), Sprint 12 = scope expansion, Baseline = blended avg"
        },

        "scope_changes": {
            "boat_admin_added": 4,  # +4 subtasks since Sprint 11
            "barge_admin_added": 17,  # +17 demo issues
            "total_added": 21,
            "notes": "Boat: +4 screens (Fuel Price, Status, Settings, +1). Barge: +17 demo issues (Dec 22)"
        },

        "key_dates": {
            "boat_admin_created": "2025-11-07",
            "barge_admin_demo": "2025-12-22",
            "checkpoint_created": datetime.now().strftime("%Y-%m-%d"),
            "next_milestone": "2026-01-21",  # Barge Admin target (revised from Jan 18)
            "notes": "Barge Admin target revised to Jan 21-22 (more conservative)"
        }
    }

    # Save checkpoint
    checkpoint_dir = Path.home() / ".claude-sessions"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_file = checkpoint_dir / f"admin-velocity-{checkpoint['analysis_date']}.json"
    checkpoint_file.write_text(json.dumps(checkpoint, indent=2))

    # Windows-compatible output (no emojis)
    print(f"[OK] Checkpoint saved: {checkpoint_file}")
    print(f"[DATA] Sprint {sprint_num} | Epic: {epic_completion_pct}% | Boat: {boat_completion_pct}% | Barge: {barge_completion_pct}%")
    return checkpoint_file


def load_checkpoint(date=None):
    """
    Load a checkpoint file

    Args:
        date: Date string (YYYY-MM-DD) or None for latest

    Returns:
        Checkpoint data dict or None if not found
    """
    checkpoint_dir = Path.home() / ".claude-sessions"

    if date:
        checkpoint_file = checkpoint_dir / f"admin-velocity-{date}.json"
        if checkpoint_file.exists():
            return json.loads(checkpoint_file.read_text())
        else:
            print(f"[ERROR] Checkpoint not found: {checkpoint_file}")
            return None
    else:
        # Find latest checkpoint
        checkpoints = sorted(checkpoint_dir.glob("admin-velocity-*.json"), reverse=True)
        if checkpoints:
            latest = checkpoints[0]
            print(f"[LOAD] Loading latest checkpoint: {latest}")
            return json.loads(latest.read_text())
        else:
            print("[ERROR] No checkpoints found")
            return None


def compare_checkpoints(old_checkpoint, new_checkpoint):
    """Compare two checkpoints and show deltas"""

    if not old_checkpoint:
        print("[INFO] No previous checkpoint - this is the baseline")
        return

    print("\n" + "="*60)
    print("SPRINT-OVER-SPRINT COMPARISON")
    print("="*60)

    # Boat Admin comparison
    old_boat = old_checkpoint["boat_admin"]
    new_boat = new_checkpoint["boat_admin"]
    print(f"\n[BOAT] Boat Admin (BOPS-3533):")
    print(f"  Subtasks: {old_boat['subtasks']} → {new_boat['subtasks']} ({new_boat['subtasks'] - old_boat['subtasks']:+d})")
    print(f"  Completed: {old_boat['completed']} → {new_boat['completed']} ({new_boat['completed'] - old_boat['completed']:+d})")
    print(f"  Completion: {old_boat['completion_pct']}% → {new_boat['completion_pct']}% ({new_boat['completion_pct'] - old_boat['completion_pct']:+d}%)")

    # Barge Admin comparison
    old_barge = old_checkpoint["barge_admin"]
    new_barge = new_checkpoint["barge_admin"]
    print(f"\n[BARGE] Barge Admin (BOPS-3517):")
    print(f"  Subtasks: {old_barge['subtasks']} → {new_barge['subtasks']} ({new_barge['subtasks'] - old_barge['subtasks']:+d})")
    print(f"  Completed: {old_barge['completed']} → {new_barge['completed']} ({new_barge['completed'] - old_barge['completed']:+d})")
    print(f"  Completion: {old_barge['completion_pct']}% → {new_barge['completion_pct']}% ({new_barge['completion_pct'] - old_barge['completion_pct']:+d}%)")

    # Epic totals
    old_epic = old_checkpoint["epic_total"]
    new_epic = new_checkpoint["epic_total"]
    print(f"\n[EPIC] Epic Total (BOPS-3515):")
    print(f"  Subtasks: {old_epic['subtasks']} → {new_epic['subtasks']} ({new_epic['subtasks'] - old_epic['subtasks']:+d})")
    print(f"  Completed: {old_epic['completed']} → {new_epic['completed']} ({new_epic['completed'] - old_epic['completed']:+d})")
    print(f"  Completion: {old_epic['completion_pct']}% → {new_epic['completion_pct']}% ({new_epic['completion_pct'] - old_epic['completion_pct']:+d}%)")

    print("\n" + "="*60)


if __name__ == "__main__":
    # Default: create checkpoint with current data (Dec 28, 2025 state)
    if len(sys.argv) > 1 and sys.argv[1] == "--load":
        # Load and display checkpoint
        date = sys.argv[2] if len(sys.argv) > 2 else None
        checkpoint = load_checkpoint(date)
        if checkpoint:
            print(json.dumps(checkpoint, indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "--compare":
        # Compare two checkpoints
        old_date = sys.argv[2] if len(sys.argv) > 2 else None
        old_checkpoint = load_checkpoint(old_date)
        new_checkpoint = load_checkpoint()  # Latest
        compare_checkpoints(old_checkpoint, new_checkpoint)
    else:
        # Create new checkpoint with current data
        create_checkpoint(
            sprint_num=13,
            boat_subtasks=28,
            boat_completed=15,
            boat_in_progress=4,
            barge_subtasks=21,
            barge_completed=1,
            barge_demo_issues=17,
            epic_total_subtasks=64,
            epic_total_completed=16,
            boat_velocity=0.56,
            sprint_11_velocity=0.93,
            sprint_12_velocity=0.23
        )
