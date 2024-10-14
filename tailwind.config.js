/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "media",
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        angsana: ["Angsana New"],
        athiti: ["Athiti"],
        kanit: ["Kanit"],
        sarabun: ["Sarabun"],
        mitr: ["Mitr"],
        prompt: ["Prompt"],
        kleeone: ["Klee One"],
        itim: ["Itim"]
      }
    },
  },
  plugins: [ require('@tailwindcss/aspect-ratio'),],
}

