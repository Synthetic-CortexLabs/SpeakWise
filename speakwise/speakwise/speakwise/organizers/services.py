"""organizers services file."""

import os
import tempfile
from email_validator import validate_email, EmailNotValidError
import pandas

from speakwise.organizers.models import AttendanceEmails


class FileHandler:
    """handle the extraction of emails from uploaded attendance list."""

    def _save_extracted_email(self, email_list, event=None):
        """save extracted emails, save unto a database."""
        for email in email_list:
            try:
                validate_email(email)
                try:
                    AttendanceEmails.objects.get(email=email, event=event)
                except AttendanceEmails.DoesNotExist:
                    AttendanceEmails.objects.create(email=email, event=event)
            except EmailNotValidError:
                raise ValueError("Email is not valid.")

    def clean_file(self, file_obj):
        """clean uploaded file."""
        if not file_obj:
            raise FileNotFoundError("No file provided.")

        # Save the uploaded file using a temporary file
        suffix = os.path.splitext(file_obj.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            for chunk in file_obj.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name

        return temp_file_path

    def extract_emails(self, uploaded_file, event=None):
        """extract emails from csv or excel file."""
        if not os.path.exists(uploaded_file) or not os.path.isfile(uploaded_file):
            raise ValueError("File does not exist.")

        if not uploaded_file.endswith(".csv") and not uploaded_file.endswith(".xlsx"):
            raise ValueError("File is not a csv or excel file.")

        """use pandas to extract emails."""
        if uploaded_file.endswith(".csv"):
            data_frame = pandas.read_csv(uploaded_file)
            for column in data_frame.columns:
                if column == "email":
                    _email_list = data_frame[column].tolist()
                    return self._save_extracted_email(_email_list, event=event)

        if uploaded_file.endswith(".xlsx"):
            data_frame = pandas.read_excel(uploaded_file)
            for column in data_frame.columns:
                if column == "email":
                    _email_list = data_frame[column].tolist()
                    return self._save_extracted_email(_email_list)
