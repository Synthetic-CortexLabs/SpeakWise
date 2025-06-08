#!/usr/bin/env python
"""
Script to fix permission class usage in Django REST Framework views.
Replaces usage of the unsupported | operator between permission classes.
"""

import os
import re


def fix_permission_classes(file_path):
    """Fix permission classes in the given file."""
    with open(file_path, "r") as file:
        content = file.read()

    # Define pattern to match permission class OR operations
    # This looks for return statements with permission classes using the | operator
    pattern = r"return \[(.*?)\|(.*?)\]"

    # Replace with separate permission classes
    # This transforms: return [ClassA() | ClassB()]
    # into: return [ClassA(), ClassB()]
    fixed_content = re.sub(
        pattern, lambda m: f"return [{m.group(1)}, {m.group(2)}]", content
    )

    # Write the fixed content back to the file
    with open(file_path, "w") as file:
        file.write(fixed_content)

    print(f"Fixed permission classes in {file_path}")


if __name__ == "__main__":
    # Path to attendees views.py file
    file_path = os.path.join("speakwise", "speakwise", "attendees", "views.py")

    # Check if the file exists
    if os.path.exists(file_path):
        fix_permission_classes(file_path)
    else:
        print(f"File not found: {file_path}")
        # Try with the absolute path
        base_path = os.path.join(
            "/Users", "macbook", "Desktop", "Devs", "SpeakWise", "speakwise"
        )
        file_path = os.path.join(
            base_path, "speakwise", "speakwise", "attendees", "views.py"
        )
        if os.path.exists(file_path):
            fix_permission_classes(file_path)
        else:
            print(f"File not found: {file_path}")
