import React from 'react'

export default function Navbar() {
    return (

        <nav class="bg-white dark:bg-sky-500 w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600">
            <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
                <a href="#" class="flex items-center space-x-3 rtl:space-x-reverse">
                    <img src="https://flowbite.com/docs/images/logo.svg" class="h-8" alt="Flowbite Logo" />
                    <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Smart PDF</span>
                </a>
                <div class="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Get started</button>
                </div>
                <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                    <ul class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-sky-500">
                        <li>
                            <a href="#" class="block py-2 px-3 text-white rounded md:bg-transparent md:text-gray-700 md:p-0 md:dark:text-gray-950" aria-current="page">Home</a>
                        </li>
                        <li>
                            <a href="#" class="block py-2 px-3 text-white rounded md:bg-transparent md:text-gray-700 md:p-0 md:dark:text-gray-950">About</a>
                        </li>
                        <li>
                            <a href="#" class="block py-2 px-3 text-white rounded md:bg-transparent md:text-gray-700 md:p-0 md:dark:text-gray-950">Services</a>
                        </li>
                        <li>
                            <a href="#" class="block py-2 px-3 text-white rounded md:bg-transparent md:text-gray-700 md:p-0 md:dark:text-gray-950">Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

    )
}
