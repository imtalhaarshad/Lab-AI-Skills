#!/usr/bin/env python3
"""
Project Planner - Comprehensive Project Planning Tool
This script helps plan projects by guiding through key planning steps.
"""

import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class ProjectType(Enum):
    SOFTWARE = "software"
    MARKETING = "marketing"
    RESEARCH = "research"
    OPERATIONS = "operations"
    CONSTRUCTION = "construction"
    EVENT = "event"
    PRODUCT = "product"
    PROCESS = "process"

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
    effort_hours: float
    dependencies: List[str]
    assigned_to: str
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    priority: Priority = Priority.MEDIUM

@dataclass
class Milestone:
    id: str
    name: str
    description: str
    target_date: datetime.date
    deliverable: str
    completed: bool = False

@dataclass
class Resource:
    id: str
    name: str
    role: str
    availability_percentage: float  # 0-100
    hourly_rate: float
    skills: List[str]

@dataclass
class Risk:
    id: str
    name: str
    description: str
    probability: float  # 0-1 (0-100%)
    impact: float  # 0-1 (0-100%)
    mitigation_strategy: str
    owner: str

@dataclass
class Project:
    name: str
    description: str
    project_type: ProjectType
    start_date: datetime.date
    estimated_duration_weeks: int
    team_size: int
    budget: float
    priority: Priority
    objectives: List[str]
    stakeholders: List[str]
    tasks: List[Task] = None
    milestones: List[Milestone] = None
    resources: List[Resource] = None
    risks: List[Risk] = None

    def __post_init__(self):
        if self.tasks is None:
            self.tasks = []
        if self.milestones is None:
            self.milestones = []
        if self.resources is None:
            self.resources = []
        if self.risks is None:
            self.risks = []

def create_project_plan(
    name: str,
    description: str,
    project_type: ProjectType,
    duration_weeks: int,
    team_size: int,
    budget: float,
    priority: Priority = Priority.MEDIUM,
    objectives: List[str] = None,
    stakeholders: List[str] = None
) -> Project:
    """
    Create a basic project plan with initial parameters.
    """
    if objectives is None:
        objectives = []
    if stakeholders is None:
        stakeholders = []

    project = Project(
        name=name,
        description=description,
        project_type=project_type,
        start_date=datetime.date.today(),
        estimated_duration_weeks=duration_weeks,
        team_size=team_size,
        budget=budget,
        priority=priority,
        objectives=objectives,
        stakeholders=stakeholders
    )

    return project

def add_task_to_project(
    project: Project,
    name: str,
    description: str,
    duration_days: int,
    effort_hours: float,
    dependencies: List[str] = None,
    assigned_to: str = "",
    priority: Priority = Priority.MEDIUM
) -> Task:
    """
    Add a task to the project with proper ID generation.
    """
    if dependencies is None:
        dependencies = []

    # Generate unique task ID
    task_id = f"task_{len(project.tasks) + 1:03d}"

    task = Task(
        id=task_id,
        name=name,
        description=description,
        duration_days=duration_days,
        effort_hours=effort_hours,
        dependencies=dependencies,
        assigned_to=assigned_to,
        priority=priority
    )

    project.tasks.append(task)
    return task

def add_milestone_to_project(
    project: Project,
    name: str,
    description: str,
    target_date: datetime.date,
    deliverable: str
) -> Milestone:
    """
    Add a milestone to the project.
    """
    milestone_id = f"milestone_{len(project.milestones) + 1:03d}"

    milestone = Milestone(
        id=milestone_id,
        name=name,
        description=description,
        target_date=target_date,
        deliverable=deliverable
    )

    project.milestones.append(milestone)
    return milestone

def add_resource_to_project(
    project: Project,
    name: str,
    role: str,
    availability_percentage: float,
    hourly_rate: float,
    skills: List[str] = None
) -> Resource:
    """
    Add a resource to the project.
    """
    if skills is None:
        skills = []

    resource_id = f"resource_{len(project.resources) + 1:03d}"

    resource = Resource(
        id=resource_id,
        name=name,
        role=role,
        availability_percentage=availability_percentage,
        hourly_rate=hourly_rate,
        skills=skills
    )

    project.resources.append(resource)
    return resource

def add_risk_to_project(
    project: Project,
    name: str,
    description: str,
    probability: float,
    impact: float,
    mitigation_strategy: str,
    owner: str
) -> Risk:
    """
    Add a risk to the project.
    """
    risk_id = f"risk_{len(project.risks) + 1:03d}"

    risk = Risk(
        id=risk_id,
        name=name,
        description=description,
        probability=probability,
        impact=impact,
        mitigation_strategy=mitigation_strategy,
        owner=owner
    )

    project.risks.append(risk)
    return risk

def estimate_project_timeline(project: Project) -> Dict:
    """
    Estimate project timeline based on tasks and dependencies.
    """
    total_effort_hours = sum(task.effort_hours for task in project.tasks)
    total_duration_days = sum(task.duration_days for task in project.tasks)

    # Calculate resource-adjusted timeline
    avg_availability = sum(r.availability_percentage for r in project.resources) / len(project.resources) if project.resources else 50
    resource_adjustment_factor = avg_availability / 100.0

    adjusted_duration = total_duration_days / resource_adjustment_factor if resource_adjustment_factor > 0 else total_duration_days

    # Calculate critical path (simplified)
    critical_tasks = [task for task in project.tasks if not task.dependencies]
    if critical_tasks:
        critical_path_duration = max((task.duration_days for task in critical_tasks), default=0)
    else:
        critical_path_duration = adjusted_duration

    return {
        "total_effort_hours": total_effort_hours,
        "estimated_duration_days": round(adjusted_duration),
        "critical_path_days": critical_path_duration,
        "start_date": project.start_date.isoformat(),
        "estimated_end_date": (project.start_date + datetime.timedelta(days=round(adjusted_duration))).isoformat(),
        "resource_utilization_factor": resource_adjustment_factor
    }

def calculate_budget_allocation(project: Project) -> Dict:
    """
    Calculate budget allocation across different aspects of the project.
    """
    # Calculate labor costs
    labor_cost = sum(
        (task.effort_hours * next((r.hourly_rate for r in project.resources if r.name == task.assigned_to), 0))
        for task in project.tasks
        if task.assigned_to
    )

    # Calculate other costs based on project type
    overhead_percentage = {
        ProjectType.SOFTWARE: 0.15,
        ProjectType.MARKETING: 0.10,
        ProjectType.RESEARCH: 0.20,
        ProjectType.OPERATIONS: 0.08,
        ProjectType.CONSTRUCTION: 0.25,
        ProjectType.EVENT: 0.12,
        ProjectType.PRODUCT: 0.18,
        ProjectType.PROCESS: 0.05
    }.get(project.project_type, 0.15)

    overhead_cost = project.budget * overhead_percentage
    remaining_budget = project.budget - labor_cost - overhead_cost

    return {
        "total_budget": project.budget,
        "labor_cost": labor_cost,
        "overhead_cost": overhead_cost,
        "remaining_budget": remaining_budget,
        "budget_utilization_percentage": ((project.budget - remaining_budget) / project.budget) * 100 if project.budget > 0 else 0,
        "recommended_contingency": remaining_budget * 0.10  # 10% contingency
    }

def assess_project_risks(project: Project) -> Dict:
    """
    Assess overall project risk based on individual risks.
    """
    if not project.risks:
        return {
            "overall_risk_level": "low",
            "total_risks_identified": 0,
            "high_priority_risks": 0,
            "risk_score": 0.0,
            "recommendations": ["No risks have been identified yet. Consider conducting a risk assessment."]
        }

    total_risk_score = sum(risk.probability * risk.impact for risk in project.risks)
    avg_risk_score = total_risk_score / len(project.risks)

    high_priority_risks = sum(1 for risk in project.risks if (risk.probability * risk.impact) > 0.5)

    if avg_risk_score > 0.6:
        overall_risk_level = "high"
    elif avg_risk_score > 0.3:
        overall_risk_level = "medium"
    else:
        overall_risk_level = "low"

    recommendations = []
    if high_priority_risks > 0:
        recommendations.append(f"Address {high_priority_risks} high-priority risks immediately.")
    if avg_risk_score > 0.5:
        recommendations.append("Consider adding more contingency time and budget.")
    if len(project.risks) < 5:
        recommendations.append("Consider identifying more potential risks.")

    return {
        "overall_risk_level": overall_risk_level,
        "total_risks_identified": len(project.risks),
        "high_priority_risks": high_priority_risks,
        "risk_score": round(avg_risk_score, 2),
        "recommendations": recommendations
    }

def generate_project_summary(project: Project) -> Dict:
    """
    Generate a comprehensive summary of the project plan.
    """
    timeline_info = estimate_project_timeline(project)
    budget_info = calculate_budget_allocation(project)
    risk_info = assess_project_risks(project)

    return {
        "project_info": {
            "name": project.name,
            "description": project.description,
            "type": project.project_type.value,
            "priority": project.priority.value,
            "start_date": project.start_date.isoformat(),
            "estimated_duration_weeks": project.estimated_duration_weeks,
            "team_size": project.team_size
        },
        "timeline": timeline_info,
        "budget": budget_info,
        "risks": risk_info,
        "summary_stats": {
            "total_tasks": len(project.tasks),
            "total_milestones": len(project.milestones),
            "total_resources": len(project.resources),
            "total_stakeholders": len(project.stakeholders)
        }
    }

def save_project_to_json(project: Project, filename: str):
    """
    Save project to JSON file.
    """
    project_dict = asdict(project)
    # Convert dates to ISO format strings
    project_dict['start_date'] = project_dict['start_date'].isoformat()

    for task in project_dict['tasks']:
        if task['start_date']:
            task['start_date'] = task['start_date'].isoformat()
        if task['end_date']:
            task['end_date'] = task['end_date'].isoformat()

    for milestone in project_dict['milestones']:
        milestone['target_date'] = milestone['target_date'].isoformat()

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(project_dict, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Project Planner - Comprehensive Project Planning Tool")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--description", required=True, help="Project description")
    parser.add_argument("--type", required=True, choices=[pt.value for pt in ProjectType], help="Project type")
    parser.add_argument("--duration", type=int, required=True, help="Estimated duration in weeks")
    parser.add_argument("--team-size", type=int, required=True, help="Team size")
    parser.add_argument("--budget", type=float, required=True, help="Project budget")
    parser.add_argument("--priority", default="medium", choices=["low", "medium", "high", "critical"], help="Project priority")
    parser.add_argument("--output", default="project_plan.json", help="Output file for project plan")

    args = parser.parse_args()

    # Convert string arguments to appropriate types
    project_type = ProjectType(args.type)
    priority = Priority(args.priority)

    # Create project
    project = create_project_plan(
        name=args.name,
        description=args.description,
        project_type=project_type,
        duration_weeks=args.duration,
        team_size=args.team_size,
        budget=args.budget,
        priority=priority
    )

    # Generate and print project summary
    summary = generate_project_summary(project)

    print("PROJECT PLAN SUMMARY")
    print("=" * 50)
    print(f"Project: {summary['project_info']['name']}")
    print(f"Description: {summary['project_info']['description']}")
    print(f"Type: {summary['project_info']['type']}")
    print(f"Priority: {summary['project_info']['priority']}")
    print(f"Duration: {summary['project_info']['estimated_duration_weeks']} weeks")
    print(f"Team Size: {summary['project_info']['team_size']}")
    print()

    print("TIMELINE ESTIMATE")
    print("-" * 20)
    print(f"Total Effort Hours: {summary['timeline']['total_effort_hours']:.1f}")
    print(f"Estimated Duration: {summary['timeline']['estimated_duration_days']} days")
    print(f"Critical Path: {summary['timeline']['critical_path_days']} days")
    print(f"Start Date: {summary['timeline']['start_date']}")
    print(f"End Date: {summary['timeline']['estimated_end_date']}")
    print()

    print("BUDGET ANALYSIS")
    print("-" * 15)
    print(f"Total Budget: ${summary['budget']['total_budget']:,.2f}")
    print(f"Labor Cost: ${summary['budget']['labor_cost']:,.2f}")
    print(f"Overhead: ${summary['budget']['overhead_cost']:,.2f}")
    print(f"Remaining: ${summary['budget']['remaining_budget']:,.2f}")
    print(f"Utilization: {summary['budget']['budget_utilization_percentage']:.1f}%")
    print()

    print("RISK ASSESSMENT")
    print("-" * 15)
    print(f"Overall Risk Level: {summary['risks']['overall_risk_level']}")
    print(f"Risks Identified: {summary['risks']['total_risks_identified']}")
    print(f"High Priority Risks: {summary['risks']['high_priority_risks']}")
    print(f"Risk Score: {summary['risks']['risk_score']}")
    print()

    if summary['risks']['recommendations']:
        print("RECOMMENDATIONS")
        print("-" * 15)
        for rec in summary['risks']['recommendations']:
            print(f"- {rec}")
        print()

    print(f"Statistics: {summary['summary_stats']['total_tasks']} tasks, {summary['summary_stats']['total_milestones']} milestones, {summary['summary_stats']['total_resources']} resources")

    # Save project to file
    save_project_to_json(project, args.output)
    print(f"\nProject plan saved to {args.output}")