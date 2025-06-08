# Testing Role-Based Access Control

This directory contains tests for verifying the proper implementation of role-based access control (RBAC) in the SpeakWise platform.

## Running the Tests

To run these tests, use the following command from the project root:

```bash
python manage.py test speakwise.authentication.tests.test_permissions
```

## What's Being Tested

The test suite includes:

1. **Session Management Permissions**
   - Viewing sessions (should be public)
   - Creating sessions (organizers and admins only)
   - Updating sessions (speakers for their own sessions, organizers and admins for all sessions)
   - Deleting sessions (speakers for their own sessions, organizers and admins for all sessions)

2. **Feedback Permissions**
   - Viewing feedback (speakers, organizers and admins only)
   - Submitting feedback (attendees only)
   - Updating feedback (speakers, organizers and admins only)
   - Deleting feedback (speakers, organizers and admins only)

3. **Authentication Flows**
   - Attendee login (verifies role check)
   - Speaker login (verifies role check)
   - Organizer login (verifies role check)
   - Wrong role tests (verifies users can't log in with the wrong endpoint)

## Adding More Tests

To add more tests for RBAC, extend the `PermissionsTestCase` or `AuthenticationTestCase` classes in `test_permissions.py`.

## Troubleshooting

If you encounter issues with the tests:

1. Ensure all role types are properly defined in the database
2. Check that permission classes are properly applied in your views
3. Verify that your API routes are correctly configured
4. Make sure the login views properly check for user roles
