#!/usr/bin/env python3
"""
Timeline Builder for Project Planning
This script helps create and manage project timelines with milestones and dependencies.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

class TaskStatus(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    CANCELLED = "cancelled"

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Task:
    id: str
    name: str
    description: str
    duration_days: int
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    dependencies: List[str] = None
    assigned_to: Optional[str] = None
    status: TaskStatus = TaskStatus.NOT_STARTED
    priority: Priority = Priority.MEDIUM
    estimated_effort_hours: float = 0.0

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

@dataclass
class Milestone:
    id: str
    name: str
    description: str
    target_date: str
    deliverable: str
    completed_date: Optional[str] = None
    achieved: bool = False

@dataclass
class Timeline:
    project_name: str
    start_date: str
    planned_duration_days: int
    tasks: List[Task]
    milestones: List[Milestone]

def create_timeline(
    project_name: str,
    start_date: str,
    planned_duration_days: int
) -> Timeline:
    """Create a new project timeline."""
    return Timeline(
        project_name=project_name,
        start_date=start_date,
        planned_duration_days=planned_duration_days,
        tasks=[],
        milestones=[]
    )

def add_task(
    timeline: Timeline,
    name: str,
    description: str,
    duration_days: int,
    dependencies: List[str] = None,
    assigned_to: str = "",
    priority: Priority = Priority.MEDIUM,
    estimated_effort_hours: float = 0.0
) -> Task:
    """Add a task to the timeline."""
    if dependencies is None:
        dependencies = []

    task_id = f"task_{len(timeline.tasks) + 1:03d}"

    task = Task(
        id=task_id,
        name=name,
        description=description,
        duration_days=duration_days,
        dependencies=dependencies,
        assigned_to=assigned_to,
        priority=priority,
        estimated_effort_hours=estimated_effort_hours
    )

    timeline.tasks.append(task)
    return task

def add_milestone(
    timeline: Timeline,
    name: str,
    description: str,
    target_date: str,
    deliverable: str
) -> Milestone:
    """Add a milestone to the timeline."""
    milestone_id = f"milestone_{len(timeline.milestones) + 1:03d}"

    milestone = Milestone(
        id=milestone_id,
        name=name,
        description=description,
        target_date=target_date,
        deliverable=deliverable
    )

    timeline.milestones.append(milestone)
    return milestone

def calculate_task_dates(timeline: Timeline) -> Timeline:
    """Calculate start and end dates for all tasks based on dependencies."""
    # Convert string dates to datetime objects for calculations
    start_dt = datetime.strptime(timeline.start_date, "%Y-%m-%d")

    # Sort tasks by dependencies to process them in correct order
    sorted_tasks = _sort_tasks_by_dependencies(timeline.tasks)

    for task in sorted_tasks:
        # Calculate start date based on dependencies
        if task.dependencies:
            dependency_end_dates = []
            for dep_id in task.dependencies:
                dep_task = next((t for t in timeline.tasks if t.id == dep_id), None)
                if dep_task and dep_task.end_date:
                    dep_end_dt = datetime.strptime(dep_task.end_date, "%Y-%m-%d")
                    dependency_end_dates.append(dep_end_dt)

            if dependency_end_dates:
                # Start after latest dependency ends
                task_start_dt = max(dependency_end_dates)
            else:
                task_start_dt = start_dt
        else:
            # No dependencies, start at project start date
            task_start_dt = start_dt

        # Calculate end date
        task_end_dt = task_start_dt + timedelta(days=task.duration_days)

        # Update task dates
        task.start_date = task_start_dt.strftime("%Y-%m-%d")
        task.end_date = task_end_dt.strftime("%Y-%m-%d")

    return timeline

def _sort_tasks_by_dependencies(tasks: List[Task]) -> List[Task]:
    """Sort tasks by dependencies to ensure dependent tasks come after their dependencies."""
    # Create a copy to avoid modifying the original list
    sorted_tasks = tasks.copy()
    remaining_tasks = tasks.copy()
    result = []

    # Process tasks until all are sorted
    while remaining_tasks:
        # Find tasks with no unsatisfied dependencies
        ready_tasks = []
        for task in remaining_tasks:
            deps_satisfied = all(
                dep_id in [t.id for t in result] for dep_id in task.dependencies
            )
            if deps_satisfied:
                ready_tasks.append(task)

        if not ready_tasks:
            # Circular dependency detected
            raise ValueError("Circular dependency detected in task dependencies")

        # Add ready tasks to result and remove from remaining
        for task in ready_tasks:
            result.append(task)
            remaining_tasks.remove(task)

    return result

def calculate_critical_path(timeline: Timeline) -> List[str]:
    """Calculate the critical path of the project."""
    # This is a simplified critical path calculation
    # In a real implementation, we'd use forward and backward passes

    # For now, return the longest sequence of dependent tasks
    if not timeline.tasks:
        return []

    # Find tasks with no dependencies
    start_tasks = [t for t in timeline.tasks if not t.dependencies]

    if not start_tasks:
        return []

    # Calculate the longest path (simplified)
    critical_path = []
    current_task = start_tasks[0]  # Start with first task without dependencies

    while current_task:
        critical_path.append(current_task.id)
        # Find next task with longest duration that depends on current task
        next_tasks = [
            t for t in timeline.tasks
            if current_task.id in t.dependencies
        ]
        if next_tasks:
            current_task = max(next_tasks, key=lambda t: t.duration_days)
        else:
            current_task = None

    return critical_path

def calculate_timeline_metrics(timeline: Timeline) -> Dict:
    """Calculate various timeline metrics."""
    calculate_task_dates(timeline)  # Ensure dates are calculated

    # Count statuses
    status_counts = {status.value: 0 for status in TaskStatus}
    for task in timeline.tasks:
        status_counts[task.status.value] += 1

    # Calculate completion percentage
    completed_tasks = sum(1 for t in timeline.tasks if t.status == TaskStatus.COMPLETED)
    completion_percentage = (completed_tasks / len(timeline.tasks)) * 100 if timeline.tasks else 0

    # Calculate timeline health
    today = datetime.now()
    overdue_tasks = 0
    for task in timeline.tasks:
        if task.end_date and task.status != TaskStatus.COMPLETED:
            end_dt = datetime.strptime(task.end_date, "%Y-%m-%d")
            if end_dt < today:
                overdue_tasks += 1

    # Calculate project duration
    if timeline.tasks:
        start_dates = [t.start_date for t in timeline.tasks if t.start_date]
        end_dates = [t.end_date for t in timeline.tasks if t.end_date]

        if start_dates and end_dates:
            project_start = min(start_dates)
            project_end = max(end_dates)

            start_dt = datetime.strptime(project_start, "%Y-%m-%d")
            end_dt = datetime.strptime(project_end, "%Y-%m-%d")
            actual_duration = (end_dt - start_dt).days
        else:
            actual_duration = 0
    else:
        actual_duration = 0

    return {
        'total_tasks': len(timeline.tasks),
        'completed_tasks': completed_tasks,
        'completion_percentage': round(completion_percentage, 2),
        'overdue_tasks': overdue_tasks,
        'on_track_tasks': len(timeline.tasks) - completed_tasks - overdue_tasks,
        'task_status_breakdown': status_counts,
        'actual_duration_days': actual_duration,
        'planned_duration_days': timeline.planned_duration_days,
        'schedule_variance_days': actual_duration - timeline.planned_duration_days,
        'critical_path': calculate_critical_path(timeline)
    }

def identify_timeline_alerts(timeline: Timeline, days_ahead: int = 7) -> List[Dict]:
    """Identify timeline-related alerts."""
    alerts = []
    today = datetime.now()

    # Check for upcoming milestones
    for milestone in timeline.milestones:
        if not milestone.achieved:
            try:
                milestone_date = datetime.strptime(milestone.target_date, "%Y-%m-%d")
                days_until_milestone = (milestone_date - today).days

                if 0 <= days_until_milestone <= days_ahead:
                    alerts.append({
                        'type': 'upcoming_milestone',
                        'severity': 'info',
                        'message': f'Milestone "{milestone.name}" due in {days_until_milestone} days',
                        'date': milestone.target_date
                    })
            except ValueError:
                continue

    # Check for overdue tasks
    for task in timeline.tasks:
        if task.end_date and task.status != TaskStatus.COMPLETED:
            try:
                end_date = datetime.strptime(task.end_date, "%Y-%m-%d")
                days_overdue = (today - end_date).days

                if days_overdue > 0:
                    alerts.append({
                        'type': 'overdue_task',
                        'severity': 'critical',
                        'message': f'Task "{task.name}" is {days_overdue} days overdue',
                        'date': task.end_date
                    })
            except ValueError:
                continue

    # Check for critical path tasks
    critical_path = calculate_critical_path(timeline)
    for task_id in critical_path:
        task = next((t for t in timeline.tasks if t.id == task_id), None)
        if task and task.status != TaskStatus.COMPLETED:
            try:
                end_date = datetime.strptime(task.end_date, "%Y-%m-%d")
                days_remaining = (end_date - today).days

                if days_remaining <= 3:
                    alerts.append({
                        'type': 'critical_task_due',
                        'severity': 'warning',
                        'message': f'Critical task "{task.name}" due in {days_remaining} days',
                        'date': task.end_date
                    })
            except ValueError:
                continue

    return alerts

def generate_timeline_report(timeline: Timeline) -> str:
    """Generate a formatted timeline report."""
    metrics = calculate_timeline_metrics(timeline)
    alerts = identify_timeline_alerts(timeline)

    report = []
    report.append("TIMELINE REPORT")
    report.append("=" * 50)
    report.append(f"Project: {timeline.project_name}")
    report.append(f"Start Date: {timeline.start_date}")
    report.append(f"Planned Duration: {timeline.planned_duration_days} days")
    report.append("")

    report.append("PROJECT METRICS:")
    report.append("-" * 15)
    report.append(f"Total Tasks: {metrics['total_tasks']}")
    report.append(f"Completed: {metrics['completed_tasks']}")
    report.append(f"Completion: {metrics['completion_percentage']}%")
    report.append(f"On Track: {metrics['on_track_tasks']}")
    report.append(f"Overdue: {metrics['overdue_tasks']}")
    report.append(f"Actual Duration: {metrics['actual_duration_days']} days")
    report.append(f"Schedule Variance: {metrics['schedule_variance_days']} days")
    report.append("")

    if metrics['critical_path']:
        report.append("CRITICAL PATH:")
        report.append("-" * 12)
        for task_id in metrics['critical_path']:
            task = next((t for t in timeline.tasks if t.id == task_id), None)
            if task:
                report.append(f"  → {task.name}")
        report.append("")

    if alerts:
        report.append("TIMELINE ALERTS:")
        report.append("-" * 12)
        for alert in alerts:
            severity_symbol = {
                'info': "ℹ️",
                'warning': "⚠️",
                'critical': "🚨"
            }.get(alert['severity'], "❓")
            report.append(f"{severity_symbol} {alert['message']} (Date: {alert['date']})")
        report.append("")

    report.append("TASKS:")
    report.append("-" * 5)
    for task in timeline.tasks:
        status_symbol = {
            'not_started': "⏳",
            'in_progress': "🔄",
            'completed': "✅",
            'on_hold': "⏸️",
            'cancelled': "❌"
        }.get(task.status.value, "❓")

        priority_symbol = {
            'low': "🟢",
            'medium': "🟡",
            'high': "🟠",
            'critical': "🔴"
        }.get(task.priority.value, "⚪")

        dates_str = f"{task.start_date} to {task.end_date}" if task.start_date and task.end_date else "TBD"
        report.append(f"{status_symbol}{priority_symbol} {task.name} ({dates_str})")
        report.append(f"      Duration: {task.duration_days} days, Effort: {task.estimated_effort_hours} hrs")
        if task.assigned_to:
            report.append(f"      Assigned: {task.assigned_to}")
        if task.dependencies:
            report.append(f"      Depends: {', '.join(task.dependencies)}")
        report.append("")

    report.append("MILESTONES:")
    report.append("-" * 9)
    for milestone in timeline.milestones:
        achievement_symbol = "✅" if milestone.achieved else "⏳"
        report.append(f"{achievement_symbol} {milestone.name} (Due: {milestone.target_date})")
        report.append(f"      Deliverable: {milestone.deliverable}")
        if milestone.description:
            report.append(f"      Description: {milestone.description}")
        if milestone.completed_date:
            report.append(f"      Completed: {milestone.completed_date}")
        report.append("")

    return "\n".join(report)

def save_timeline(timeline: Timeline, filename: str):
    """Save timeline to JSON file."""
    timeline_dict = asdict(timeline)

    # Convert enums to strings
    timeline_dict['tasks'] = [
        {k: (v.value if isinstance(v, (TaskStatus, Priority)) else v)
         for k, v in asdict(task).items()}
        for task in timeline.tasks
    ]

    timeline_dict['milestones'] = [
        {k: v for k, v in asdict(milestone).items()}
        for milestone in timeline.milestones
    ]

    with open(filename, 'w') as f:
        json.dump(timeline_dict, f, indent=2)

def load_timeline_from_json(filename: str) -> Timeline:
    """Load timeline from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)

    # Convert dictionaries back to dataclass objects
    tasks = []
    for task_data in data['tasks']:
        task = Task(
            id=task_data['id'],
            name=task_data['name'],
            description=task_data['description'],
            duration_days=task_data['duration_days'],
            start_date=task_data['start_date'],
            end_date=task_data['end_date'],
            dependencies=task_data['dependencies'],
            assigned_to=task_data['assigned_to'],
            status=TaskStatus(task_data['status']),
            priority=Priority(task_data['priority']),
            estimated_effort_hours=task_data['estimated_effort_hours']
        )
        tasks.append(task)

    milestones = []
    for milestone_data in data['milestones']:
        milestone = Milestone(
            id=milestone_data['id'],
            name=milestone_data['name'],
            description=milestone_data['description'],
            target_date=milestone_data['target_date'],
            deliverable=milestone_data['deliverable'],
            completed_date=milestone_data['completed_date'],
            achieved=milestone_data['achieved']
        )
        milestones.append(milestone)

    return Timeline(
        project_name=data['project_name'],
        start_date=data['start_date'],
        planned_duration_days=data['planned_duration_days'],
        tasks=tasks,
        milestones=milestones
    )

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Timeline Builder for Project Planning")
    parser.add_argument("--project-name", required=True, help="Name of the project")
    parser.add_argument("--start-date", required=True, help="Project start date (YYYY-MM-DD)")
    parser.add_argument("--duration-days", type=int, required=True, help="Planned duration in days")
    parser.add_argument("--add-task", action="append", help="Add task in format: name:description:days:assigned_to:priority")
    parser.add_argument("--add-milestone", action="append", help="Add milestone in format: name:description:date:deliverable")
    parser.add_argument("--output", default="timeline.json", help="Output file for timeline")

    args = parser.parse_args()

    # Create timeline
    timeline = create_timeline(
        project_name=args.project_name,
        start_date=args.start_date,
        planned_duration_days=args.duration_days
    )

    # Add tasks if provided
    if args.add_task:
        for task_str in args.add_task:
            parts = task_str.split(":")
            if len(parts) >= 3:
                try:
                    duration = int(parts[2])
                    assigned_to = parts[3] if len(parts) > 3 else ""
                    priority_str = parts[4] if len(parts) > 4 else "medium"

                    priority = Priority(priority_str.lower())

                    add_task(
                        timeline=timeline,
                        name=parts[0],
                        description=parts[1],
                        duration_days=duration,
                        assigned_to=assigned_to,
                        priority=priority
                    )
                except (ValueError, KeyError):
                    print(f"Warning: Invalid task format: {task_str}")

    # Add milestones if provided
    if args.add_milestone:
        for milestone_str in args.add_milestone:
            parts = milestone_str.split(":")
            if len(parts) >= 4:
                try:
                    add_milestone(
                        timeline=timeline,
                        name=parts[0],
                        description=parts[1],
                        target_date=parts[2],
                        deliverable=parts[3]
                    )
                except (ValueError, IndexError):
                    print(f"Warning: Invalid milestone format: {milestone_str}")

    # Calculate dates
    calculate_task_dates(timeline)

    # Generate and print report
    print(generate_timeline_report(timeline))

    # Save timeline
    save_timeline(timeline, args.output)
    print(f"\nTimeline saved to {args.output}")