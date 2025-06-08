# Role-Based Access Control (RBAC) for SpeakWise Platform

This document provides a comprehensive overview of the role-based access control system implemented in the SpeakWise platform.

## User Roles

The platform supports four distinct user roles, each with specific permissions:

1. **Attendee**: Regular users who attend events and provide feedback
2. **Speaker**: Users who speak at events and manage their sessions
3. **Organizer**: Users who manage events, speakers, and sessions
4. **Admin**: Users with full access to all platform features

## Permission Classes

The following permission classes are implemented in `authentication/permissions.py`:

- `IsAttendee`: Allows access only to users with the Attendee role
- `IsSpeaker`: Allows access only to users with the Speaker role
- `IsOrganizer`: Allows access only to users with the Organizer role
- `IsAdmin`: Allows access only to users with the Admin role
- `IsOrganizerOrAdmin`: Allows access to users with either the Organizer or Admin role
- `IsSpeakerOrOrganizerOrAdmin`: Allows access to users with either the Speaker, Organizer, or Admin role

## Access Control by Resource Type

### Events

- **Viewing events**: Everyone (public access)
- **Creating events**: Organizers and Admins
- **Updating events**: Organizers and Admins
- **Deleting events**: Organizers and Admins

### Sessions

- **Viewing sessions**: Everyone (public access)
- **Creating sessions**: Organizers and Admins
- **Updating sessions**: Session's assigned Speaker, Organizers, and Admins
- **Deleting sessions**: Session's assigned Speaker, Organizers, and Admins

### Speaker Profiles

- **Viewing speaker profiles**: Everyone (public access)
- **Creating speaker profiles**: Organizers and Admins
- **Updating speaker profiles**: Profile owner (Speaker), Organizers, and Admins
- **Deleting speaker profiles**: Organizers and Admins

### Attendee Profiles

- **Viewing attendee profiles**: Organizers and Admins
- **Creating attendee profiles**: Everyone (public registration)
- **Updating attendee profiles**: Profile owner (Attendee), Organizers, and Admins
- **Deleting attendee profiles**: Profile owner (Attendee), Organizers, and Admins

### Feedback

- **Viewing feedback**: Speakers, Organizers, and Admins
- **Creating feedback**: Attendees
- **Updating feedback**: Speakers, Organizers, and Admins
- **Deleting feedback**: Organizers and Admins

### Talks

- **Viewing talks**: Everyone (public access)
- **Creating talks**: Speakers, Organizers, and Admins
- **Updating talks**: Talk creator (Speaker), Organizers, and Admins
- **Deleting talks**: Organizers and Admins

### Skills and Tags

- **Viewing skills/tags**: Everyone (public access)
- **Creating skills/tags**: Speakers, Organizers, and Admins
- **Updating skills/tags**: Organizers and Admins
- **Deleting skills/tags**: Organizers and Admins

### Social Links

- **Viewing social links**: Everyone (public access via speaker profiles)
- **Creating social links**: Speaker (for their own profile)
- **Updating social links**: Speaker (for their own links)
- **Deleting social links**: Speaker (for their own links)

## Authentication Flow

1. Users register with a specific role (Attendee, Speaker, Organizer)
2. Users log in through the appropriate endpoint based on their role:
   - `/auth/attendee/` for Attendees
   - `/auth/speaker/` for Speakers
   - `/auth/organizer/` for Organizers
3. Upon successful authentication, the system verifies the user has the appropriate role
4. A JWT token is issued containing user information and role details
5. Subsequent API requests include this token to enforce appropriate permissions

## Object-Level Permissions

For certain resources, additional object-level permissions are enforced:

1. **Sessions**: Speakers can only edit their own sessions
2. **Speaker Profiles**: Speakers can only edit their own profiles
3. **Attendee Profiles**: Attendees can only edit their own profiles
4. **Social Links**: Speakers can only manage their own social links

## Testing RBAC

To test the RBAC implementation:

1. Create users with different roles
2. Authenticate each user and obtain their JWT token
3. Attempt to access various endpoints with different user tokens
4. Verify that permissions are correctly enforced according to the user's role

## Example API Calls

### Authenticate as a Speaker
```
POST /api/auth/speaker/
{
  "email": "speaker@example.com",
  "password": "password123"
}
```

### Create a Session (as an Organizer)
```
POST /api/sessions/
Authorization: Bearer <organizer_token>
{
  "title": "Introduction to RBAC",
  "description": "Learn about role-based access control",
  "start_time": "10:00:00",
  "end_time": "11:00:00",
  "event": 1,
  "speaker": 1
}
```

### Update a Session (as a Speaker)
```
PATCH /api/sessions/1/
Authorization: Bearer <speaker_token>
{
  "title": "Advanced RBAC Concepts"
}
```