#!/bin/bash

# Script to test the Role-Based Access Control (RBAC) implementation

echo "=== Testing SpeakWise RBAC System ==="
echo "Running permission tests..."

# Navigate to the project directory
cd /Users/macbook/Desktop/Devs/SpeakWise/speakwise/speakwise

# Run the permission tests
python manage.py test speakwise.authentication.tests.test_permissions -v 2

# Check if tests passed
if [ $? -eq 0 ]; then
  echo "✅ RBAC tests passed successfully!"
else
  echo "❌ RBAC tests failed. Please review the errors above."
fi

echo ""
echo "For more information about RBAC implementation:"
echo "- See the RBAC_DOCUMENTATION.md file in the authentication app"
echo "- See the RBAC_SUMMARY.md file for a summary of implemented features"
echo "- Check the tests/README.md file for details on the test suite"
