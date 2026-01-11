#!/usr/bin/env python3
"""
Budget Calculator for Project Planning
This script helps calculate and track project budgets across different categories.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class BudgetCategory(Enum):
    LABOR = "labor"
    EQUIPMENT = "equipment"
    SOFTWARE = "software"
    SERVICES = "services"
    TRAVEL = "travel"
    TRAINING = "training"
    OVERHEAD = "overhead"
    MATERIALS = "materials"
    CONTINGENCY = "contingency"

class ExpenseStatus(Enum):
    PLANNED = "planned"
    APPROVED = "approved"
    INVOICED = "invoiced"
    PAID = "paid"
    CANCELLED = "cancelled"

@dataclass
class BudgetItem:
    id: str
    name: str
    category: BudgetCategory
    estimated_cost: float
    actual_cost: Optional[float] = None
    vendor: Optional[str] = None
    due_date: Optional[str] = None
    status: ExpenseStatus = ExpenseStatus.PLANNED
    description: Optional[str] = None

@dataclass
class BudgetPlan:
    project_name: str
    total_budget: float
    baseline_date: str
    items: List[BudgetItem]
    contingency_percentage: float = 10.0  # Default 10% contingency

    def calculate_totals(self) -> Dict:
        """Calculate budget totals and utilization."""
        planned_total = sum(item.estimated_cost for item in self.items)

        actual_total = sum(
            item.actual_cost for item in self.items
            if item.actual_cost is not None
        )

        remaining_budget = self.total_budget - actual_total
        utilized_percentage = (actual_total / self.total_budget) * 100 if self.total_budget > 0 else 0

        # Calculate by category
        category_breakdown = {}
        for item in self.items:
            cat = item.category.value
            if cat not in category_breakdown:
                category_breakdown[cat] = {'estimated': 0, 'actual': 0}
            category_breakdown[cat]['estimated'] += item.estimated_cost
            if item.actual_cost:
                category_breakdown[cat]['actual'] += item.actual_cost

        return {
            'planned_total': planned_total,
            'actual_total': actual_total,
            'remaining_budget': remaining_budget,
            'utilized_percentage': round(utilized_percentage, 2),
            'contingency_amount': self.total_budget * (self.contingency_percentage / 100),
            'category_breakdown': category_breakdown,
            'budget_variance': actual_total - planned_total
        }

def create_budget_plan(
    project_name: str,
    total_budget: float,
    contingency_percentage: float = 10.0
) -> BudgetPlan:
    """Create a new budget plan."""
    return BudgetPlan(
        project_name=project_name,
        total_budget=total_budget,
        baseline_date=str(__import__('datetime').datetime.now().date()),
        items=[],
        contingency_percentage=contingency_percentage
    )

def add_budget_item(
    budget_plan: BudgetPlan,
    name: str,
    category: BudgetCategory,
    estimated_cost: float,
    description: Optional[str] = None,
    vendor: Optional[str] = None,
    due_date: Optional[str] = None
) -> BudgetItem:
    """Add a budget item to the plan."""
    item_id = f"budget_{len(budget_plan.items) + 1:03d}"

    item = BudgetItem(
        id=item_id,
        name=name,
        category=category,
        estimated_cost=estimated_cost,
        description=description,
        vendor=vendor,
        due_date=due_date
    )

    budget_plan.items.append(item)
    return item

def update_budget_item_actual_cost(
    budget_plan: BudgetPlan,
    item_id: str,
    actual_cost: float
) -> bool:
    """Update the actual cost for a budget item."""
    for item in budget_plan.items:
        if item.id == item_id:
            item.actual_cost = actual_cost
            item.status = ExpenseStatus.PAID
            return True
    return False

def calculate_phase_budgets(items: List[BudgetItem]) -> Dict[str, float]:
    """Calculate budget allocations by project phase (based on naming convention)."""
    phase_breakdown = {}

    for item in items:
        # Extract phase from item name (assuming format like "Phase 1: Task Name")
        if ":" in item.name:
            phase = item.name.split(":")[0].strip()
        else:
            phase = "General"

        if phase not in phase_breakdown:
            phase_breakdown[phase] = 0
        phase_breakdown[phase] += item.estimated_cost

    return phase_breakdown

def generate_budget_forecast(
    budget_plan: BudgetPlan,
    monthly_expenses: List[Dict[str, float]]
) -> Dict:
    """Generate a budget forecast based on planned monthly expenses."""
    totals = budget_plan.calculate_totals()

    # Calculate cumulative forecast
    cumulative_spending = 0
    forecast_data = []

    for month_data in monthly_expenses:
        cumulative_spending += month_data.get('expected_spending', 0)
        remaining_after_month = budget_plan.total_budget - cumulative_spending

        forecast_data.append({
            'month': month_data['month'],
            'expected_spending': month_data['expected_spending'],
            'cumulative_spending': cumulative_spending,
            'remaining_budget': remaining_after_month,
            'spending_percentage': (cumulative_spending / budget_plan.total_budget) * 100 if budget_plan.total_budget > 0 else 0
        })

    return {
        'current_totals': totals,
        'forecast_data': forecast_data,
        'projected_completion_status': 'under_budget' if remaining_after_month >= 0 else 'over_budget'
    }

def identify_budget_alerts(budget_plan: BudgetPlan, threshold_percentage: float = 80.0) -> List[Dict]:
    """Identify budget items that exceed alert thresholds."""
    alerts = []
    totals = budget_plan.calculate_totals()

    # Check overall budget utilization
    if totals['utilized_percentage'] > threshold_percentage:
        alerts.append({
            'type': 'overall_budget',
            'severity': 'warning',
            'message': f'Budget utilization at {totals["utilized_percentage"]}% - exceeds {threshold_percentage}% threshold',
            'details': f'Spent ${totals["actual_total"]:,.2f} of ${budget_plan.total_budget:,.2f}'
        })

    # Check individual items
    for item in budget_plan.items:
        if item.actual_cost and item.estimated_cost > 0:
            variance = ((item.actual_cost - item.estimated_cost) / item.estimated_cost) * 100

            if variance > 20:  # 20% over budget
                alerts.append({
                    'type': 'item_overrun',
                    'severity': 'critical',
                    'message': f'Item "{item.name}" {variance:.1f}% over budget',
                    'details': f'Estimated: ${item.estimated_cost:.2f}, Actual: ${item.actual_cost:.2f}'
                })
            elif variance > 10:  # 10% over budget
                alerts.append({
                    'type': 'item_warning',
                    'severity': 'warning',
                    'message': f'Item "{item.name}" {variance:.1f}% over budget',
                    'details': f'Estimated: ${item.estimated_cost:.2f}, Actual: ${item.actual_cost:.2f}'
                })

    return alerts

def generate_budget_report(budget_plan: BudgetPlan) -> str:
    """Generate a formatted budget report."""
    totals = budget_plan.calculate_totals()
    alerts = identify_budget_alerts(budget_plan)

    report = []
    report.append("BUDGET REPORT")
    report.append("=" * 50)
    report.append(f"Project: {budget_plan.project_name}")
    report.append(f"Total Budget: ${budget_plan.total_budget:,.2f}")
    report.append(f"Contingency ({budget_plan.contingency_percentage}%): ${totals['contingency_amount']:,.2f}")
    report.append(f"As of: {budget_plan.baseline_date}")
    report.append("")

    report.append("BUDGET SUMMARY:")
    report.append("-" * 15)
    report.append(f"Planned Total: ${totals['planned_total']:,.2f}")
    report.append(f"Actual Spent: ${totals['actual_total']:,.2f}")
    report.append(f"Remaining: ${totals['remaining_budget']:,.2f}")
    report.append(f"Utilization: {totals['utilized_percentage']}%")
    report.append(f"Variance: ${totals['budget_variance']:,.2f}")
    report.append("")

    report.append("CATEGORY BREAKDOWN:")
    report.append("-" * 15)
    for category, amounts in totals['category_breakdown'].items():
        report.append(f"  {category.title()}: ${amounts['estimated']:,.2f} (Est.) / ${amounts['actual']:,.2f} (Act.)")
    report.append("")

    if alerts:
        report.append("BUDGET ALERTS:")
        report.append("-" * 12)
        for alert in alerts:
            severity_symbol = "⚠️" if alert['severity'] == 'warning' else "🚨" if alert['severity'] == 'critical' else "ℹ️"
            report.append(f"{severity_symbol} {alert['message']}")
            report.append(f"   {alert['details']}")
        report.append("")

    report.append("BUDGET ITEMS:")
    report.append("-" * 12)
    for item in budget_plan.items:
        status_symbol = {
            'planned': "⏳",
            'approved': "✅",
            'invoiced': "📋",
            'paid': "💰",
            'cancelled': "❌"
        }.get(item.status.value, "❓")

        actual_str = f"${item.actual_cost:,.2f}" if item.actual_cost else "TBD"
        report.append(f"{status_symbol} {item.name} (${item.estimated_cost:,.2f} est. / {actual_str} act.) - {item.category.value}")
        if item.vendor:
            report.append(f"      Vendor: {item.vendor}")
        if item.description:
            report.append(f"      Desc: {item.description}")
        report.append("")

    return "\n".join(report)

def save_budget_plan(budget_plan: BudgetPlan, filename: str):
    """Save budget plan to JSON file."""
    plan_dict = asdict(budget_plan)

    # Convert enums to strings
    plan_dict['items'] = [
        {k: (v.value if isinstance(v, (BudgetCategory, ExpenseStatus)) else v)
         for k, v in asdict(item).items()}
        for item in budget_plan.items
    ]

    with open(filename, 'w') as f:
        json.dump(plan_dict, f, indent=2)

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Budget Calculator for Project Planning")
    parser.add_argument("--project-name", required=True, help="Name of the project")
    parser.add_argument("--total-budget", type=float, required=True, help="Total project budget")
    parser.add_argument("--contingency", type=float, default=10.0, help="Contingency percentage (default: 10%)")
    parser.add_argument("--add-item", action="append", help="Add budget item in format: name:category:amount:description")
    parser.add_argument("--output", default="budget_plan.json", help="Output file for budget plan")

    args = parser.parse_args()

    # Create budget plan
    budget_plan = create_budget_plan(
        project_name=args.project_name,
        total_budget=args.total_budget,
        contingency_percentage=args.contingency
    )

    # Add budget items if provided
    if args.add_item:
        for item_str in args.add_item:
            parts = item_str.split(":")
            if len(parts) >= 3:
                try:
                    category = BudgetCategory(parts[1].upper())
                    amount = float(parts[2])
                    description = parts[3] if len(parts) > 3 else None

                    add_budget_item(
                        budget_plan=budget_plan,
                        name=parts[0],
                        category=category,
                        estimated_cost=amount,
                        description=description
                    )
                except (ValueError, KeyError):
                    print(f"Warning: Invalid budget item format: {item_str}")

    # Generate and print report
    print(generate_budget_report(budget_plan))

    # Save budget plan
    save_budget_plan(budget_plan, args.output)
    print(f"\nBudget plan saved to {args.output}")