#!/usr/bin/env python3
"""
Simple packaging script for Islamic Content SEO skill
This creates a .skill file that can be distributed and imported into Claude Code.
"""

import os
import zipfile
from pathlib import Path

def package_skill(skill_dir: str, output_path: str = None):
    """
    Package the Islamic Content SEO skill into a distributable format.
    """
    skill_path = Path(skill_dir)
    skill_name = skill_path.name

    if not output_path:
        output_path = f"{skill_name}.skill"

    # Collect all files in the skill directory
    files_to_package = []
    for root, dirs, files in os.walk(skill_path):
        for file in files:
            file_path = Path(root) / file
            files_to_package.append(file_path)

    # Create the zip file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in files_to_package:
            # Calculate the archive name (relative to skill directory)
            archive_name = file_path.relative_to(skill_path.parent)
            zipf.write(file_path, archive_name)

    print(f"Skill packaged successfully: {output_path}")
    print(f"Included {len(files_to_package)} files in the package")

    # List the files that were included
    print("\nFiles included in the package:")
    for file_path in sorted(files_to_package):
        archive_name = file_path.relative_to(skill_path.parent)
        print(f"  - {archive_name}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <skill_directory> [output_path]")
        print("Example: python package_skill.py islamic-content-seo")
        sys.exit(1)

    skill_dir = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    package_skill(skill_dir, output_path)