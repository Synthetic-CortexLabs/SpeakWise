# **SpeakWise Frontend/UI Detailed Plan**

Based on the project requirements and the backend structure provided, this document outlines a comprehensive plan for the frontend/UI development of **SpeakWise**. This plan is intended to guide the frontend developers in building a user-friendly and efficient interface using the **Remix** framework with **React**, **TypeScript**, and **JavaScript**, leveraging server-side rendering for optimal performance.

---

## **Table of Contents**

1. [Introduction](#introduction)
2. [Core Features and User Flows](#core-features-and-user-flows)
   - [Attendee Flow](#1-attendee-flow)
   - [Organizer Flow](#2-organizer-flow)
   - [Speaker Flow](#3-speaker-flow)
3. [Frontend Architecture](#frontend-architecture)
   - [Project Structure](#project-structure)
   - [Routing Strategy](#routing-strategy)
   - [State Management](#state-management)
   - [Authentication and Authorization](#authentication-and-authorization)
4. [Detailed Component Breakdown](#detailed-component-breakdown)
   - [Common Components](#common-components)
   - [Attendee Components](#attendee-components)
   - [Organizer Components](#organizer-components)
   - [Speaker Components](#speaker-components)
5. [Data Fetching and API Integration](#data-fetching-and-api-integration)
   - [Loaders and Actions](#loaders-and-actions)
   - [Error Handling](#error-handling)
6. [Styling and UI/UX Considerations](#styling-and-uiux-considerations)
7. [Accessibility and Internationalization](#accessibility-and-internationalization)
8. [Testing Strategy](#testing-strategy)
9. [Footer Notes](#footer-notes)

---

## **Introduction**

The frontend of **SpeakWise** aims to provide an intuitive and seamless experience for all users—attendees, organizers, and speakers. By utilizing **Remix**, we can leverage server-side rendering to improve performance and SEO, while building interactive and dynamic interfaces with **React** and **TypeScript**.

---

## **Core Features and User Flows**

### **1. Attendee Flow**

**Purpose**: Enable attendees to register, navigate events by region, provide session-specific feedback, and manage their profiles.

#### **Core Features and Sub-Features**

1. **Registration & Login**
   - User registration with email, username, and password.
   - Login functionality with authentication tokens.
   - Password reset and email verification (if implemented).

3. **Event & Location Navigation**
   - Region selection (7 regions).
   - Country selection within a region.
   - Conference/event selection within a country.
   - Day selection for the event.
   - Session listing and selection.

4. **Session Feedback Submission**
   - Overall star rating (out of 5).
   - Ratings for specific aspects (1-10 scale).
   - Comment box with optional anonymity toggle.
   - Feedback editing within 24 hours.

5. **Feedback History**
   - List of past feedback submissions.
   - Read-only view after 24 hours.

6. **Profile Management**
   - Update personal details.
   - Change password.
   - Manage notification preferences.

---

### **2. Organizer Flow**

**Purpose**: Allow organizers to create and manage events and sessions, oversee attendee engagement, and analyze feedback.

#### **Core Features and Sub-Features**

1. **Dashboard Overview**
   - Summary of upcoming events.
   - Quick stats on attendee engagement.

2. **Event Management**
   - Create, edit, and delete events.
   - View list of events.

3. **Session Management**
   - Create, edit, and delete sessions within events.
   - Assign speakers to sessions.

4. **Attendee Management**
   - View registered attendees.
   - Monitor attendance verification.

5. **Analytics Dashboard**
   - Real-time feedback metrics.
   - Heatmaps of session popularity.
   - Speaker comparison charts.

6. **Reporting & Exports**
   - Generate and download reports (PDF, CSV).

---

### **3. Speaker Flow**

**Purpose**: Provide speakers with access to detailed feedback on their sessions and a platform to manage their profiles.

#### **Core Features and Sub-Features**

1. **Profile Setup and Management**
   - Update bio and add social media links.
   - View personal information.

2. **Session Feedback Analytics**
   - View quantitative ratings and qualitative comments.
   - Option to see reviewer names if feedback is non-anonymous.

3. **Export Feedback**
   - Download feedback reports.

---

## **Frontend Architecture**

### **Project Structure**

Utilizing Remix's conventions, the project will be organized as follows:

```
speakwise-frontend/
├── app/
│   ├── components/          # Reusable UI components
│   ├── routes/              # Remix routes (pages)
│   ├── styles/              # Global and component-specific styles
│   ├── utils/               # Utility functions and helpers
│   ├── entry.client.tsx     # Client-side entry point
│   ├── entry.server.tsx     # Server-side entry point
│   ├── root.tsx             # Root component with global context providers
│   └── session.server.ts    # Session management on the server
├── public/                  # Static assets (images, icons)
├── package.json             # Project dependencies and scripts
├── remix.config.js          # Remix configuration
├── tsconfig.json            # TypeScript configuration
└── README.md
```

### **Routing Strategy**

- **File-based Routing**: Remix uses file-based routing where each file in the `routes/` directory corresponds to a route.
- **Nested Routes**: Utilize nested routes for shared layouts and UI components.
- **Protected Routes**: Implement route guards for authentication and role-based access control.

### **State Management**

- **Remix Loaders and Actions**: Leverage Remix's data loading mechanisms to fetch data on the server and hydrate the client.
- **Context API**: Use React's Context API for global state (e.g., user authentication status).
- **Local State**: Manage component-specific state with React's `useState` and `useReducer`.

### **Authentication and Authorization**

- **Session Management**: Use Remix's session handling to manage user authentication with secure cookies.
- **Role-Based Access Control**: Implement authorization checks based on user roles (attendee, organizer, speaker).
- **Protected Components**: Create higher-order components or wrappers to protect routes and components.

---

## **Detailed Component Breakdown**

### **Common Components**

These components are shared across different user roles.

1. **Layout Components**
   - `Header`: Displays the navigation bar with dynamic links based on user role and authentication status.
   - `Footer`: Contains site-wide footer information and links.
   - `Sidebar`: Used in dashboards for organizers and speakers.

2. **Form Components**
   - `InputField`: Reusable input fields with validation.
   - `Select`: Custom select dropdowns.
   - `Button`: Standardized buttons with variants (primary, secondary, etc.).
   - `RatingStars`: Component for star ratings.
   - `Slider`: For ratings on a scale of 1 to 10.

3. **Modal and Dialog Components**
   - `Modal`: For displaying dialogs, confirmations, and forms.
   - `Toast`: Notification messages for success, error, or info.

4. **Navigation Components**
   - `Breadcrumbs`: Display navigation path, especially in event navigation.
   - `Pagination`: For paginated lists.

5. **Data Display Components**
   - `Table`: Standardized table for displaying data.
   - `Card`: For displaying grouped information.
   - `Chart`: Integrate with chart libraries for analytics.

---

### **Attendee Components**

#### **Pages and Routes**

1. **Authentication**
   - `/login`: Login page.
   - `/register`: Registration page.
   - `/forgot-password`: Password reset initiation.
   - `/reset-password`: Password reset completion.

2. **Event Navigation**
   - `/regions`: Region selection page.
   - `/regions/:regionId/countries`: Country selection.
   - `/countries/:countryId/events`: Event selection.
   - `/events/:eventId/days`: Day selection within the event.
   - `/events/:eventId/sessions`: Session listing.
   - `/sessions/:sessionId`: Session details and feedback submission.

3. **Feedback**
   - `/feedbacks`: List of attendee's feedbacks.
   - `/feedbacks/:feedbackId/edit`: Edit feedback (if within 24 hours).

4. **Profile**
   - `/profile`: View and edit profile.
   - `/profile/settings`: Update notification preferences.

#### **Key Components**

1. **RegionSelection**
   - Displays list of regions.
   - On selection, navigates to country selection.

2. **CountrySelection**
   - Fetches and displays countries based on selected region.

3. **EventList**
   - Lists events in the selected country.
   - Includes search and filtering options.

4. **SessionList**
   - Displays sessions for the selected day of the event.
   - Allows attendees to select a session to provide feedback.

5. **FeedbackForm**
   - Inputs for overall rating and specific aspect ratings.
   - Comment box with anonymity toggle.
   - Validation to ensure attendance code is provided.

6. **FeedbackHistory**
   - Lists submitted feedbacks.
   - Indicates if feedback is editable.

7. **ProfilePage**
   - Shows attendee's information.
   - Options to edit details and change password.

---

### **Organizer Components**

#### **Pages and Routes**

1. **Dashboard**
   - `/organizer/dashboard`: Overview of events and stats.

2. **Event Management**
   - `/organizer/events`: List of events.
   - `/organizer/events/new`: Create event.
   - `/organizer/events/:eventId/edit`: Edit event.
   - `/organizer/events/:eventId`: Event details and sessions.

3. **Session Management**
   - `/organizer/events/:eventId/sessions/new`: Create session.
   - `/organizer/sessions/:sessionId/edit`: Edit session.

4. **Attendee Management**
   - `/organizer/events/:eventId/attendees`: List attendees.
   - `/organizer/attendees/:attendeeId`: Attendee details.

5. **Analytics**
   - `/organizer/events/:eventId/analytics`: Event analytics dashboard.

6. **Reports**
   - `/organizer/events/:eventId/reports`: Generate and download reports.

#### **Key Components**

1. **OrganizerDashboard**
   - Summary cards showing key metrics.
   - Quick links to manage events and sessions.

2. **EventForm**
   - Form to create or edit events.
   - Inputs for event details and selection of region and country.

3. **SessionForm**
   - Form to create or edit sessions.
   - Inputs for session details and assignment of speakers.

5. **AnalyticsCharts**
   - Visual representations of feedback data.
   - Interactive charts for heatmaps and comparisons.

6. **ReportGenerator**
   - Options to select report type and format.
   - Button to generate and download reports.

---

### **Speaker Components**

#### **Pages and Routes**

1. **Dashboard**
   - `/speaker/dashboard`: Overview of sessions and feedback.

2. **Profile Management**
   - `/speaker/profile`: View and edit profile.

3. **Session Feedback**
   - `/speaker/sessions`: List of sessions.
   - `/speaker/sessions/:sessionId`: Session feedback details.
   - `/speaker/sessions/:sessionId/feedback`: Detailed feedback analytics.

4. **Reports**
   - `/speaker/sessions/:sessionId/reports`: Download feedback reports.

#### **Key Components**

1. **SpeakerDashboard**
   - Overview of upcoming sessions.
   - Summary of recent feedback.

2. **SessionList**
   - Lists sessions the speaker is associated with.
   - Links to feedback analytics.

3. **FeedbackAnalytics**
   - Detailed view of quantitative and qualitative feedback.
   - Option to filter anonymous and non-anonymous feedback.

4. **ProfileForm**
   - Form to update bio and social media links.

5. **ReportDownloader**
   - Interface to select report format and initiate download.

---

## **Data Fetching and API Integration**

### **Loaders and Actions**

- **Loaders**: Functions that run on the server to fetch data before rendering a route.
  - Used for pre-fetching data for pages like event lists, session details, and feedback history.
  - Ensures data is available when the page is rendered.

- **Actions**: Functions that handle form submissions and mutations.
  - Used for handling login, registration, feedback submission, profile updates.
  - Allows server-side validation and redirects upon success.

### **Error Handling**

- Use Remix's built-in error boundaries to catch and display errors.
- Provide user-friendly error messages and options to retry or navigate back.
- Implement form validation errors on the client and server side.

---

## **Styling and UI/UX Considerations**

- **CSS-in-JS**: Use libraries like **styled-components** or **Emotion** for component-level styling, or Remix's built-in support for CSS modules.
- **Responsive Design**: Ensure the application is mobile-friendly and adapts to various screen sizes.
- **Design System**: Establish a consistent design language with predefined styles for colors, typography, spacing, and components.
- **Accessibility**: Follow WCAG guidelines to make the application accessible to users with disabilities.
- **User Feedback**: Provide immediate visual feedback for user actions (e.g., button clicks, form submissions).
- **Loading States**: Implement loading indicators while data is being fetched.
- **Empty States**: Design informative empty states for pages without data.

---

## **Accessibility and Internationalization**

### **Accessibility**

- **ARIA Attributes**: Use ARIA attributes to improve screen reader support.
- **Keyboard Navigation**: Ensure all interactive elements are accessible via keyboard.
- **Contrast Ratios**: Use sufficient color contrast for text and UI elements.

### **Internationalization**

- **Language Support**: Plan for multi-language support if needed in the future.
- **Localization**: Use libraries like **react-intl** for managing localized strings.
- **Date and Number Formats**: Display dates and numbers according to user locale.

---

## **Testing Strategy**

### **Unit Testing**

- Write unit tests for components using **Jest** and **React Testing Library**.
- Focus on component logic and rendering.

### **Integration Testing**

- Test interactions between components and routes.
- Use Remix's testing utilities for loaders and actions.

### **End-to-End Testing**

- Use **Cypress** or **Playwright** for E2E tests.
- Simulate user flows (e.g., registration, feedback submission).

### **Performance Testing**

- Use tools like **Lighthouse** to analyze performance and SEO.
- Optimize for fast load times and minimal render blocking.

---

## **Footer Notes**

- **Collaboration**: Maintain clear communication with backend developers to align API contracts.
- **Documentation**: Keep documentation up-to-date for components and utilities.
- **Version Control**: Use Git with feature branching and pull requests for code reviews.
- **Continuous Integration**: Set up CI/CD pipelines for automated testing and deployments.
- **Code Quality**: Enforce coding standards with ESLint and Prettier.
- **Security**: Sanitize user inputs and protect against common web vulnerabilities (e.g., XSS, CSRF).
