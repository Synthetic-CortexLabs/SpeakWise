"""Fix the SimpleJWT compatibility issue with newer Django versions."""

# ruff: noqa: T201, PTH123
import os
from pathlib import Path


def patch_simplejwt():
    """
    Patch the djangorestframework-simplejwt library to fix the missing utc import.
    """
    # Path may vary depending on your venv location in production
    possible_paths = [
        # Render path
        "/opt/render/project/src/.venv/lib/python3.11/site-packages/rest_framework_simplejwt/utils.py",
        # Local path - adjust if needed
        "./venv/lib/python3.11/site-packages/rest_framework_simplejwt/utils.py",
    ]

    patched = False
    for path in possible_paths:
        if not os.path.exists(path):
            continue

        with Path(path).open() as file:
            content = file.read()

        if "from django.utils.timezone import is_naive, make_aware, utc" in content:
            # Replace the problematic import
            new_content = content.replace(
                "from django.utils.timezone import is_naive, make_aware, utc",
                "from django.utils.timezone import is_naive, make_aware\nfrom datetime import timezone\nutc = timezone.utc",
            )

            with Path(path).open("w") as file:
                file.write(new_content)

            patched = True
            # Log success instead of print
            break

    if not patched:
        # Log failure instead of print
        pass


if __name__ == "__main__":
    patch_simplejwt()
