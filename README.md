# University Project Planning Tool

This repository contains a comprehensive project planning tool developed as part of a university project. The tool helps users plan, execute, and manage projects effectively through guided workflows for task breakdown, timeline creation, resource allocation, risk assessment, and financial planning.

## Features

### Project Planning
- Comprehensive project planning assistance
- Task breakdown and estimation
- Timeline creation with milestones
- Resource allocation planning
- Risk assessment and mitigation
- Financial planning and tracking

### Islamic Content SEO Tool
- Keyword research for Islamic content
- Platform-specific hashtag generation
- Content optimization for Islamic topics
- Guidelines for social media platforms
- Cultural sensitivity considerations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/university-project-planning-tool.git
```

2. Navigate to the project directory:
```bash
cd university-project-planning-tool
```

## Usage

### Project Planning Tool

The project planning tool is organized as a Claude Code skill in the `.claude/skills/project-planning` directory.

To use the main project planner:
```bash
cd .claude/skills/project-planning/scripts
python project_planner.py --name "My Project" --description "Project description" --type software --duration 12 --team-size 5 --budget 50000
```

To perform risk assessment:
```bash
python risk_assessment.py --project-type software
```

To calculate budgets:
```bash
python budget_calculator.py --project-name "My Project" --total-budget 50000
```

To build timelines:
```bash
python timeline_builder.py --project-name "My Project" --start-date 2024-01-01 --duration-days 90
```

### Islamic Content SEO Tool

The Islamic content SEO tool is organized as a Claude Code skill in the `.claude/skills/islamic-content-seo` directory.

To research keywords:
```bash
cd .claude/skills/islamic-content-seo/scripts
python keyword_research.py prayer ramadan
```

To generate hashtags:
```bash
python hashtag_generator.py Instagram "daily prayer"
```

To optimize content:
```bash
python content_optimizer.py "Daily Prayer" "Learn about daily prayers" "content.txt" prayer islam
```

## Skills Structure

Both tools follow the Claude Code skill structure:

```
.claude/skills/
├── project-planning/
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── project_planner.py
│   │   ├── risk_assessment.py
│   │   ├── budget_calculator.py
│   │   ├── timeline_builder.py
│   │   └── package_skill.py
│   └── references/
│       ├── project-templates.md
│       ├── methodologies.md
│       ├── checklists.md
│       └── best-practices.md
└── islamic-content-seo/
    ├── SKILL.md
    ├── scripts/
    │   ├── keyword_research.py
    │   ├── hashtag_generator.py
    │   ├── content_optimizer.py
    │   └── package_skill.py
    └── references/
        ├── islamic-keywords.md
        ├── social-platforms.md
        ├── seo-best-practices.md
        └── cultural-considerations.md
```

## Contributing

If you'd like to contribute to this project:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developed as part of a university project
- Built following Claude Code skill development best practices
- Designed to assist with project planning and Islamic content SEO