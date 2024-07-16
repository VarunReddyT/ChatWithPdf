import React from 'react'

export default function Home() {
  return (
    <div>
      <header class="bg-white">
        <div class="max-w-screen-xl mx-auto p-4">
          <h1 class="text-4xl font-semibold  dark:text-black">Welcome to Smart PDF</h1>
          <p class="text-lg dark:text-black">The best tool to convert your documents to PDF</p>
        </div>
      </header>
      <main class="max-w-screen-xl mx-auto p-4">
        <ul class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          <button class="p-4 border
          border-gray-200 dark:border-gray-600 rounded-lg">
            <h3 class="text-xl font-semibold text-gray-800 dark:text-black">Interact with PDF</h3>
            <p class="mt-2 text-gray-600 dark:text-black">Get instant insights from your document.</p>
          </button>
          <button class="p-4 border
          border-gray-200 dark:border-gray-600 rounded-lg">
            <h3 class="text-xl font-semibold text-gray-800 dark:text-black">Convert to PDF</h3>
            <p class="mt-2 text-gray-600 dark:text-black">Convert your documents to PDF with a simple click.</p>
          </button>
          <button class="p-4 border
          border-gray-200 dark:border-gray-600 rounded-lg">
            <h3 class="text-xl font-semibold text-gray-800 dark:text-black">Share PDF</h3>
            <p class="mt-2 text-gray-600 dark:text-black">Share your PDF file with anyone.</p>
          </button>
        </ul>
      </main>
    </div>
  )
}
