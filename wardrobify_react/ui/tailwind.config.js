/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      backgroundImage: {
        'tester': "url('/public/mountains.jpeg')"
      },
      colors: {
        'blue-transparent': 'rgba(59, 52, 226, 0.4)'
      },
    },
  },
  plugins: [],
}
