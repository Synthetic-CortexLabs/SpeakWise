# SpeakWise Frontend

A modern, responsive web application built with Next.js and Tailwind CSS for the SpeakWise conference feedback platform.

## Tech Stack

- **Framework**: Next.js 15.0.3 with App Router
- **Styling**: Tailwind CSS 3.4.1
- **Language**: TypeScript
- **State Management**: React Hooks
- **Authentication**: Custom implementation
- **Development Tools**: ESLint, PostCSS

## Project Structure

```
frontend/
├── public/
│   ├── images/
│   │   ├── conference-bg.jpg
│   │   ├── conference-feature.jpg
│   │   ├── conference-team.jpg
│   │   ├── conference-group.jpg
│   │   ├── world-map.png
│   │   ├── icons/
│   │   │   ├── globe.svg
│   │   │   ├── earth.svg
│   │   │   ├── calendar.svg
│   │   │   ├── event.svg
│   │   │   └── review.svg
│   │   ├── logos/
│   │   │   ├── gdg.png
│   │   │   ├── google-io.png
│   │   │   ├── devfest.png
│   │   │   └── flutter.png
│   │   └── social/
│   │       ├── linkedin.svg
│   │       └── twitter.svg
├── src/
│   ├── app/
│   │   ├── auth/
│   │   │   ├── page.tsx
│   │   │   ├── signin/
│   │   │   │   └── page.tsx
│   │   │   └── signup/
│   │   │       └── page.tsx
│   │   ├── components/
│   │   │   ├── auth/
│   │   │   │   ├── SignInForm.tsx
│   │   │   │   ├── SignUpForm.tsx
│   │   │   │   └── UserTypeSelection.tsx
│   │   │   ├── Navbar.tsx
│   │   │   ├── HeroSection.tsx
│   │   │   ├── AgencySection.tsx
│   │   │   ├── HowItWorksSection.tsx
│   │   │   ├── FaqSection.tsx
│   │   │   └── Footer.tsx
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   └── types/
└── tailwind.config.ts
```

## Features

### Landing Page
- Modern hero section with background image and world map overlay
- Conference logos showcase
- Agency section with rotating images
- How it works section with process cards
- FAQ section with search functionality
- Contact banner
- Footer with social links

### Authentication
- User type selection (Attendee, Speaker, Organizer)
- Sign up form with fields:
  - Name
  - Nationality
  - Email
  - Password
- Sign in form with:
  - Email
  - Password
  - Password visibility toggle
  - Forgot password link

### Design System
- Custom color palette:
  - Primary: #F15A22 (Orange)
  - Secondary colors for process cards
  - Neutral colors for text and backgrounds
- Consistent typography:
  - Font sizes from sm to 4xl
  - Font weights: medium, semibold, bold
- Component patterns:
  - Rounded corners (lg, xl, 2xl, 3xl)
  - Shadow variants (md, lg, xl)
  - Hover and focus states
  - Transitions and animations

## Getting Started

1. **Installation**
   ```bash
   npm install
   ```

2. **Development**
   ```bash
   npm run dev
   ```
   The application will start at http://localhost:3000

3. **Build**
   ```bash
   npm run build
   ```

4. **Production**
   ```bash
   npm start
   ```

## Environment Variables

Create a `.env.local` file in the root directory:
```env
NEXT_PUBLIC_API_URL=your_backend_url
```

## Contributing

1. Create a new branch
2. Make your changes
3. Submit a pull request

## Code Style

- Use TypeScript for all components
- Follow the existing component structure
- Use Tailwind CSS for styling
- Keep components small and focused
- Add proper TypeScript types
- Use meaningful component and variable names

## Performance Considerations

- Images are optimized using Next.js Image component
- Code splitting through Next.js dynamic imports
- Tailwind CSS purging unused styles in production
- Proper loading states and error boundaries
- SEO optimization through metadata

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is licensed under the terms of the MIT license.
