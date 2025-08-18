"""organizers utils."""

import csv
import io

from django.utils import timezone

from speakwise.attendees.models import Attendee


def process_csv_file(self, AttendanceEmails):
    """Process the uploaded CSV file and create attendees."""

    if self.processed:
        return self.success_count, []

    errors = []
    success_count = 0

    try:
        # Read the CSV file
        self.csv_file.seek(0)
        content = self.csv_file.read().decode("utf-8")
        csv_data = csv.DictReader(io.StringIO(content))

        for row_num, row in enumerate(csv_data, start=2):
            try:
                # Expected CSV columns
                first_name = row.get("first_name", "").strip()
                last_name = row.get("last_name", "").strip()
                email = row.get("email", "").strip()
                organization = row.get("organization", "").strip()

                if not email:
                    errors.append(f"Row {row_num}: Email is required")
                    continue

                if not first_name:
                    errors.append(f"Row {row_num}: First name is required")
                    continue

                # Check if attendee already exists
                if Attendee.objects.filter(email=email).exists():
                    msg = f"Row {row_num}: Attendee with email {email} exists"
                    errors.append(msg)
                    continue

                # Create attendee
                Attendee.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    organization=organization,
                    is_verified=True,
                )

                # Also create AttendanceEmails entry for verification
                AttendanceEmails.objects.get_or_create(
                    event=self.event,
                    email=email,
                    defaults={"is_given_feedback": False},
                )

                success_count += 1

            except ValueError as e:
                errors.append(f"Row {row_num}: {e!s}")

    except Exception as e:
        errors.append(f"Error reading CSV file: {e!s}")

    # Update the upload record
    self.success_count = success_count
    self.error_count = len(errors)
    self.error_log = "\n".join(errors)
    self.processed = True
    self.processed_at = timezone.now()
    self.save()

    return success_count, errors
