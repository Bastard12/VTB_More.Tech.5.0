/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./index.html"],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'blue': {
        100: '#EDF5FF',
        200: '#D6E4FE',
        300: '#A7C7FF',
        400: '#6FA3FF',
        500: '#3A85FF',
        600: '#0062FF',
        700: '#0142D3',
        800: '#022D9A',
        900: '#001D6D',
        950: '#001144',
      }
    },
    extend: {},
  },
  plugins: [],
}

