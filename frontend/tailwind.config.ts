import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#F15A22', // Orange (Original)
          harsh: '#FF4500',   // Harsh Orange
        },
        secondary: {
          DEFAULT: '#FFD700', // Bright Yellow
          light: '#FFFF00',   // Light Yellow
          pale: '#FFF8A6',    // Pale Yellow
          warm: '#FFA500',    // Orange-Yellow
        },
        accent: {
          red: '#FF0000',
        },
        neutral: {
          black: '#000000',
          grey: {
            DEFAULT: '#A0A0A0',
            dark: '#4A4A4A',
          },
          white: '#FFFFFF',
        }
      },
    },
  },
  plugins: [],
}

export default config;
