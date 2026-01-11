#!/usr/bin/env python3
"""
Risk Assessment Tool for Project Planning
This script helps identify, evaluate, and prioritize project risks.
"""

import json
import math
from typing import List, Dict, Tuple
from enum import Enum

class RiskCategory(Enum):
    TECHNICAL = "technical"
    FINANCIAL = "financial"
    SCHEDULE = "schedule"
    RESOURCE = "resource"
    SCOPE = "scope"
    EXTERNAL = "external"
    QUALITY = "quality"

class Probability(Enum):
    VERY_LOW = 0.1
    LOW = 0.25
    MODERATE = 0.5
    HIGH = 0.75
    VERY_HIGH = 0.9

class Impact(Enum):
    VERY_LOW = 0.1
    LOW = 0.25
    MODERATE = 0.5
    HIGH = 0.75
    VERY_HIGH = 0.9

class RiskMatrix(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

def get_common_project_risks(project_type: str) -> List[Dict]:
    """
    Get common risks associated with different project types.
    """
    common_risks = {
        "software": [
            {"name": "Technical Complexity", "category": RiskCategory.TECHNICAL, "description": "Underestimated technical challenges"},
            {"name": "Scope Creep", "category": RiskCategory.SCOPE, "description": "Requirements changing during development"},
            {"name": "Resource Availability", "category": RiskCategory.RESOURCE, "description": "Key developers becoming unavailable"},
            {"name": "Integration Issues", "category": RiskCategory.TECHNICAL, "description": "Problems integrating with existing systems"},
            {"name": "Performance Issues", "category": RiskCategory.QUALITY, "description": "Software not meeting performance requirements"}
        ],
        "marketing": [
            {"name": "Market Response", "category": RiskCategory.EXTERNAL, "description": "Campaign not resonating with target audience"},
            {"name": "Competitive Response", "category": RiskCategory.EXTERNAL, "description": "Competitors launching competing campaigns"},
            {"name": "Brand Damage", "category": RiskCategory.QUALITY, "description": "Campaign causing negative brand perception"},
            {"name": "Regulatory Compliance", "category": RiskCategory.EXTERNAL, "description": "Campaign violating advertising regulations"},
            {"name": "Budget Overrun", "category": RiskCategory.FINANCIAL, "description": "Marketing costs exceeding budget"}
        ],
        "research": [
            {"name": "Hypothesis Failure", "category": RiskCategory.TECHNICAL, "description": "Research hypothesis proving incorrect"},
            {"name": "Data Quality", "category": RiskCategory.TECHNICAL, "description": "Insufficient or poor quality data"},
            {"name": "Equipment Failure", "category": RiskCategory.TECHNICAL, "description": "Critical research equipment malfunctioning"},
            {"name": "Publication Delays", "category": RiskCategory.SCHEDULE, "description": "Delays in publishing research findings"},
            {"name": "Funding Cuts", "category": RiskCategory.FINANCIAL, "description": "Loss of research funding"}
        ],
        "operations": [
            {"name": "Process Disruption", "category": RiskCategory.TECHNICAL, "description": "Changes disrupting existing operations"},
            {"name": "Staff Resistance", "category": RiskCategory.RESOURCE, "description": "Employees resisting operational changes"},
            {"name": "System Integration", "category": RiskCategory.TECHNICAL, "description": "New processes not integrating with existing systems"},
            {"name": "Training Issues", "category": RiskCategory.RESOURCE, "description": "Staff unable to adapt to new processes"},
            {"name": "Compliance Issues", "category": RiskCategory.EXTERNAL, "description": "New processes violating regulations"}
        ],
        "construction": [
            {"name": "Weather Delays", "category": RiskCategory.EXTERNAL, "description": "Adverse weather conditions affecting construction"},
            {"name": "Material Shortages", "category": RiskCategory.RESOURCE, "description": "Delays in material deliveries"},
            {"name": "Safety Incidents", "category": RiskCategory.QUALITY, "description": "Accidents causing work stoppage"},
            {"name": "Regulatory Changes", "category": RiskCategory.EXTERNAL, "description": "Changes in building codes"},
            {"name": "Cost Overruns", "category": RiskCategory.FINANCIAL, "description": "Construction costs exceeding estimates"}
        ],
        "event": [
            {"name": "Attendance", "category": RiskCategory.EXTERNAL, "description": "Lower than expected attendance"},
            {"name": "Vendor Issues", "category": RiskCategory.RESOURCE, "description": "Key vendors failing to deliver"},
            {"name": "Weather", "category": RiskCategory.EXTERNAL, "description": "Adverse weather affecting outdoor events"},
            {"name": "Security Issues", "category": RiskCategory.QUALITY, "description": "Safety or security incidents"},
            {"name": "Budget Exceedance", "category": RiskCategory.FINANCIAL, "description": "Event costs exceeding budget"}
        ],
        "product": [
            {"name": "Market Demand", "category": RiskCategory.EXTERNAL, "description": "Product not meeting market demand"},
            {"name": "Manufacturing Issues", "category": RiskCategory.TECHNICAL, "description": "Production problems affecting quality"},
            {"name": "Competition", "category": RiskCategory.EXTERNAL, "description": "Competitors launching similar products"},
            {"name": "Quality Defects", "category": RiskCategory.QUALITY, "description": "Product defects requiring recalls"},
            {"name": "Supply Chain", "category": RiskCategory.RESOURCE, "description": "Supply chain disruptions"}
        ]
    }

    return common_risks.get(project_type.lower(), [])

def calculate_risk_score(probability: float, impact: float) -> Tuple[float, RiskMatrix]:
    """
    Calculate risk score and categorize risk level.
    """
    risk_score = probability * impact

    if risk_score <= 0.25:
        level = RiskMatrix.LOW
    elif risk_score <= 0.5:
        level = RiskMatrix.MEDIUM
    elif risk_score <= 0.75:
        level = RiskMatrix.HIGH
    else:
        level = RiskMatrix.CRITICAL

    return risk_score, level

def suggest_mitigation_strategies(category: RiskCategory) -> List[str]:
    """
    Suggest mitigation strategies based on risk category.
    """
    strategies = {
        RiskCategory.TECHNICAL: [
            "Conduct thorough technical feasibility analysis",
            "Prototype and test critical components early",
            "Establish technical review gates",
            "Maintain technical documentation",
            "Have backup technical solutions ready"
        ],
        RiskCategory.FINANCIAL: [
            "Establish contingency reserves",
            "Implement regular budget reviews",
            "Negotiate flexible contracts",
            "Secure multiple funding sources",
            "Monitor cash flow regularly"
        ],
        RiskCategory.SCHEDULE: [
            "Build buffer time into critical path",
            "Identify fast-track opportunities",
            "Use parallel processing where possible",
            "Regular schedule monitoring",
            "Maintain schedule change control"
        ],
        RiskCategory.RESOURCE: [
            "Cross-train team members",
            "Maintain resource flexibility",
            "Establish vendor relationships",
            "Create resource allocation plans",
            "Monitor resource utilization"
        ],
        RiskCategory.SCOPE: [
            "Define clear acceptance criteria",
            "Implement change control process",
            "Regular stakeholder communication",
            "Document scope requirements",
            "Manage stakeholder expectations"
        ],
        RiskCategory.EXTERNAL: [
            "Monitor external environment",
            "Build in regulatory compliance reviews",
            "Maintain stakeholder relationships",
            "Develop contingency plans",
            "Regular market analysis"
        ],
        RiskCategory.QUALITY: [
            "Implement quality gates",
            "Regular testing and reviews",
            "Quality assurance processes",
            "Continuous improvement",
            "Customer feedback mechanisms"
        ]
    }

    return strategies.get(category, ["Develop appropriate mitigation strategy"])

def assess_project_risks(risks_data: List[Dict]) -> Dict:
    """
    Perform comprehensive risk assessment on a list of risks.
    """
    assessed_risks = []
    total_risk_score = 0
    critical_risks = 0
    high_risks = 0
    medium_risks = 0
    low_risks = 0

    for risk in risks_data:
        probability_value = risk.get('probability', 0.5)
        impact_value = risk.get('impact', 0.5)

        risk_score, risk_level = calculate_risk_score(probability_value, impact_value)

        category = RiskCategory(risk.get('category', 'TECHNICAL'))
        mitigation_strategies = suggest_mitigation_strategies(category)

        assessed_risk = {
            'id': risk.get('id', f"risk_{len(assessed_risks)+1}"),
            'name': risk.get('name', 'Unnamed Risk'),
            'description': risk.get('description', ''),
            'category': category.value,
            'probability': probability_value,
            'impact': impact_value,
            'risk_score': risk_score,
            'level': risk_level.value,
            'mitigation_strategies': mitigation_strategies,
            'owner': risk.get('owner', 'TBD'),
            'status': risk.get('status', 'identified')
        }

        assessed_risks.append(assessed_risk)
        total_risk_score += risk_score

        if risk_level == RiskMatrix.CRITICAL:
            critical_risks += 1
        elif risk_level == RiskMatrix.HIGH:
            high_risks += 1
        elif risk_level == RiskMatrix.MEDIUM:
            medium_risks += 1
        else:
            low_risks += 1

    # Calculate overall project risk indicators
    avg_risk_score = total_risk_score / len(assessed_risks) if assessed_risks else 0

    if avg_risk_score > 0.6:
        overall_project_risk = "high"
    elif avg_risk_score > 0.3:
        overall_project_risk = "medium"
    else:
        overall_project_risk = "low"

    # Identify top risks
    sorted_risks = sorted(assessed_risks, key=lambda x: x['risk_score'], reverse=True)
    top_risks = sorted_risks[:5]  # Top 5 risks

    return {
        'overall_project_risk': overall_project_risk,
        'total_risks_identified': len(assessed_risks),
        'risk_distribution': {
            'critical': critical_risks,
            'high': high_risks,
            'medium': medium_risks,
            'low': low_risks
        },
        'average_risk_score': round(avg_risk_score, 2),
        'top_risks': top_risks,
        'all_assessed_risks': assessed_risks,
        'recommendations': generate_risk_recommendations(critical_risks, high_risks, avg_risk_score)
    }

def generate_risk_recommendations(critical_risks: int, high_risks: int, avg_score: float) -> List[str]:
    """
    Generate recommendations based on risk assessment results.
    """
    recommendations = []

    if critical_risks > 0:
        recommendations.append(f"IMMEDIATE ATTENTION: Address {critical_risks} critical risks as top priority")

    if high_risks > 0:
        recommendations.append(f"Focus on mitigating {high_risks} high-priority risks")

    if avg_score > 0.5:
        recommendations.append("Consider increasing contingency reserves and buffer time")

    if critical_risks + high_risks > 5:
        recommendations.append("Project risk level is concerning - consider risk reduction strategies before proceeding")

    if not recommendations:
        recommendations.append("Risk levels appear manageable, continue with standard risk management practices")

    return recommendations

def generate_risk_report(assessment_result: Dict) -> str:
    """
    Generate a formatted risk assessment report.
    """
    report = []
    report.append("RISK ASSESSMENT REPORT")
    report.append("=" * 50)
    report.append(f"Overall Project Risk Level: {assessment_result['overall_project_risk'].upper()}")
    report.append(f"Total Risks Identified: {assessment_result['total_risks_identified']}")
    report.append("")

    report.append("RISK DISTRIBUTION:")
    dist = assessment_result['risk_distribution']
    report.append(f"  Critical: {dist['critical']}")
    report.append(f"  High: {dist['high']}")
    report.append(f"  Medium: {dist['medium']}")
    report.append(f"  Low: {dist['low']}")
    report.append(f"  Average Risk Score: {assessment_result['average_risk_score']}")
    report.append("")

    if assessment_result['top_risks']:
        report.append("TOP 5 RISKS:")
        report.append("-" * 20)
        for i, risk in enumerate(assessment_result['top_risks'], 1):
            report.append(f"{i}. {risk['name']} ({risk['level'].upper()}, Score: {risk['risk_score']:.2f})")
            report.append(f"   Category: {risk['category']}")
            report.append(f"   Description: {risk['description']}")
            report.append("")

    report.append("RECOMMENDATIONS:")
    report.append("-" * 15)
    for rec in assessment_result['recommendations']:
        report.append(f"• {rec}")

    return "\n".join(report)

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Risk Assessment Tool for Project Planning")
    parser.add_argument("--project-type", required=True, help="Type of project (software, marketing, research, etc.)")
    parser.add_argument("--custom-risk", action="append", help="Add custom risk in format: name:description:category:probability:impact")
    parser.add_argument("--output", default="risk_assessment.json", help="Output file for risk assessment")

    args = parser.parse_args()

    # Get common risks for the project type
    common_risks = get_common_project_risks(args.project_type)

    # Parse custom risks if provided
    custom_risks = []
    if args.custom_risk:
        for risk_str in args.custom_risk:
            parts = risk_str.split(":")
            if len(parts) >= 5:
                try:
                    custom_risk = {
                        "name": parts[0],
                        "description": parts[1],
                        "category": parts[2].upper(),
                        "probability": float(parts[3]),
                        "impact": float(parts[4])
                    }
                    custom_risks.append(custom_risk)
                except ValueError:
                    print(f"Warning: Invalid custom risk format: {risk_str}")

    # Combine common and custom risks
    all_risks = common_risks + custom_risks

    # Perform risk assessment
    assessment_result = assess_project_risks(all_risks)

    # Print risk report
    print(generate_risk_report(assessment_result))

    # Save assessment to file
    with open(args.output, 'w') as f:
        json.dump(assessment_result, f, indent=2)

    print(f"\nRisk assessment saved to {args.output}")