# **SpeakWise**

## **Project Overview**

SpeakWise is a conference feedback platform designed to facilitate meaningful feedback for speakers, provide analytics for organizers, and enhance the conference experience for attendees. This platform allows organizers to create and manage events across different regions, while attendees can navigate through regions, countries, and sessions to give detailed feedback on speakers. 

### **Purpose**

- **For Attendees**: To easily navigate events by region and provide session-specific feedback that helps improve future conferences.
- **For Organizers**: To manage events and sessions, analyze attendee feedback, and gather insights on speaker performance.
- **For Speakers**: To gain actionable insights from attendee feedback, helping them refine and improve future presentations.

---

## **User Flows**

### **1. Attendee Flow**

**Purpose**: This flow allows attendees to register, select their event region, navigate to specific sessions, submit feedback, and manage their profile.

**Detailed Workflow**:

1. **Registration & Login**
   - Attendees register with their email, username, and password.
   - After registration, attendees receive a **unique attendance code** to verify actual attendance (only sent to attendees who check in at the event).

2. **Event & Location Selection**
   - Attendees begin by selecting the region of the conference. The seven regions are:
     - North America
     - South America
     - Europe
     - Africa
     - Middle East
     - Asia
     - South Pacific

   - **Example Path**:
     - **Step 1**: Select **Africa** as the region.
     - **Step 2**: Choose the country where the conference took place, e.g., **Ghana**.
     - **Step 3**: View and select the specific conference, e.g., **PyHo 2024**.
     - **Step 4**: Select the day of the conference, e.g., **Day 2**.
     - **Step 5**: Choose the session, e.g., **Reinforcement Learning - by Jason Quist**.

3. **Session Feedback Submission**
   - Once inside a session, attendees can provide feedback using:
     - **Overall Rating**: Give a star rating out of 5 to rate the session overall.
     - **Qualitative Ratings** (on a scale of 1 to 10) for specific aspects:
       - **Engagement**
       - **Clarity**
       - **Depth of Content**
       - **Speaker’s Knowledge**
       - **Practical Relevance**
     - **Text Comments**: Attendees can leave additional feedback in a comment box (non-editable after 24 hours).
     - **Anonymous Option**: Option to submit feedback anonymously.

4. **Verification of Attendance**
   - **Unique Attendance Code**: After checking into the conference, attendees receive a unique code via email, allowing only verified attendees to submit feedback. 

5. **Feedback History**
   - Attendees can view past feedback they’ve submitted in their profile. This feedback is read-only after the 24-hour editable period.

6. **Profile Management**
   - Update profile details (name, organization), password, and notification preferences.

---

### **2. Organizer Flow**

**Purpose**: This flow is for conference organizers to create and manage events and sessions, oversee attendee engagement, and analyze feedback.

**Detailed Workflow**:

1. **Event & Session Management**
   - Organizers create events by defining:
     - **Region**: One of the seven regions (e.g., Africa).
     - **Country**: The country within the region (e.g., Ghana).
     - **Event Details**: Event name, description, and specific dates (e.g., PyHo 2024).
     - **Session Details**: Define session name, speaker(s), time, and location for each session within the event.

2. **Attendee Management**
   - Manage attendee registrations and send **unique attendance codes** to those who check in at the conference.
   - Monitor which attendees have verified their attendance, enabling only those who attended to provide feedback.

3. **Analytics Dashboard**
   - Access real-time feedback and engagement metrics, with features like:
     - **Heatmaps**: Visual representation of session popularity and attendee engagement levels.
     - **Speaker Comparison Tool**: Compare speakers based on aggregated ratings (Engagement, Clarity, etc.).

4. **Reporting & Exports**
   - Generate and export reports (PDF, CSV) with feedback summaries, session ratings, and other insights for post-event analysis.

---

### **3. Speaker Flow**

**Purpose**: This flow provides speakers with access to detailed feedback on their sessions and a platform to manage their profile.

**Detailed Workflow**:

1. **Profile Setup**
   - Upon receiving a link from the organizer, speakers create a profile with details like:
     - **Bio**: Background information and expertise.
     - **Social Links**: Optional links to LinkedIn, Twitter, etc.

2. **Session Feedback Analytics**
   - Access detailed feedback for each session they conducted, including:
     - **Quantitative Feedback**: Aggregated ratings for Engagement, Clarity, Content Depth, Speaker Knowledge, and Practical Relevance.
     - **Qualitative Comments**: See attendee comments on the session.
     - **Reviewer Visibility**: Only see reviewer names if the feedback is non-anonymous.

3. **Export Feedback**
   - Option to download reports on session feedback, allowing speakers to keep a record and reflect on their performance.

---

## **Backend Structure**

The backend is organized into modular Django apps, each aligned with a specific flow or core functionality. Below is the project structure, with comments to clarify each app's purpose.

```
backend/
├── speakwise/                # Main Django project directory containing core settings and configurations
│   ├── __init__.py
│   ├── asgi.py               # ASGI configuration for handling asynchronous requests
│   ├── settings.py           # Django settings file for project-wide configurations (e.g., database, middleware)
│   ├── urls.py               # Root URL configuration linking to individual app routes
│   └── wsgi.py               # WSGI configuration for deploying the Django application
├── events/                   # Handles all event and session-related functionality
│   ├── models.py             # Models for events, sessions, regions, and countries
│   ├── serializers.py        # Serializers for converting event data to JSON format
│   ├── views.py              # Views for creating, retrieving, and managing events and sessions
│   ├── urls.py               # Endpoints for event-related operations
├── feedback/                 # Manages feedback and ratings for sessions
│   ├── models.py             # Models for feedback, ratings, and comments
│   ├── serializers.py        # Serializers for feedback data and anonymous options
│   ├── views.py              # Views for submitting, viewing, and managing feedback
│   ├── urls.py               # Endpoints for feedback-related actions
├── organizers/               # For organizer-specific functionalities and analytics
│   ├── models.py             # Models for event organizers and verification codes
│   ├── serializers.py        # Serializers for organizer data
│   ├── views.py              # Views for event/session management and analytics
│   ├── urls.py               # Endpoints for organizer actions
├── speakers/                 # For speaker-specific functionalities
│   ├── models.py             # Models for speaker profiles and feedback aggregation
│   ├── serializers.py        # Serializers for speaker data and profile management
│   ├── views.py              # Views for speaker feedback and profile analytics
│   ├── urls.py               # Speaker-related endpoints
├── attendees/                # Core user functionality, renamed from `users` for clarity
│   ├── models.py             # Models for attendees, their profiles, and role information
│   ├── serializers.py        # Serializers for attendee registration, login, and profile management
│   ├── views.py              # Views for handling attendee registration, login, and feedback history
│   ├── urls.py               # Attendee-related endpoints
├── common/                   # Shared utilities and settings, if needed for shared functionality
│   ├── models.py             # Any shared models across apps, such as role definitions
│   ├── utils.py              # Utility functions and helper methods for cross-app usage
└── manage.py                 # Django management file to handle commands like migrations and running the server
```

---

## **Footer Notes**

- **Technologies**: The backend is built with Django, utilizing Django Rest Framework (DRF) for API endpoints. This modular setup allows each flow to function independently while sharing common resources through the `common` directory.
- **Modularization**: By breaking down the project into distinct apps, each representing a specific user flow (attendees, organizers, speakers) or core functionality (events, feedback), we ensure clear separation of concerns and scalability.
- **Future Considerations**: Additional apps or modules can be added easily if new user flows or complex features are introduced, such as advanced analytics or additional data processing tools.
