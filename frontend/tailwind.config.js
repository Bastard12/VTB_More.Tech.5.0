/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./index.html"],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'red':{
        100: '#FFEFEF',
        200: '#FFD4D4',
        300: '#FFA7A7',
        400: '#FF7C7C',
        500: '#F64E4E',
        600: '#D92020',
        700: '#A71212',
        800: '#780A0A',
        900: '#520606',
        950: '#320000',
      },
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
    extend: {
      fontFamily: {
        'VTBFontLight': ['VTBLight', 'sans-serif'],
        'VTBFontRegular': ['VTBRegular', 'sans-serif'],
        'VTBFontMedium': ['VTBMedium', 'sans-serif'],
        'VTBFontDemiBold': ['VTBDemiBold', 'sans-serif'],
        'VTBFontSemiBold': ['VTBSemiBold', 'sans-serif'],
        'VTBFontBold': ['VTBBold', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

