'use client';

import { useState } from 'react';

export default function FaqSection() {
  const [searchQuery, setSearchQuery] = useState('');

  return (
    <section className="py-16 px-6">
      <div className="container mx-auto">
        {/* Header */}
        <div className="max-w-2xl mx-auto mb-12">
          <h2 className="text-3xl font-bold mb-3">
            <span className="text-primary">Got Any Questions?</span>
          </h2>
          <h3 className="text-2xl font-bold text-gray-400">
            We've Got Answers
          </h3>
        </div>

        {/* Search Bar */}
        <div className="max-w-2xl mx-auto">
          <div className="flex bg-gray-50 rounded-lg overflow-hidden">
            <div className="flex-1 flex items-center px-4 bg-gray-50">
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                className="h-4 w-4 text-gray-400" 
                fill="none" 
                viewBox="0 0 24 24" 
                stroke="currentColor"
              >
                <path 
                  strokeLinecap="round" 
                  strokeLinejoin="round" 
                  strokeWidth={2} 
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" 
                />
              </svg>
              <input
                type="text"
                placeholder="Search for answers..."
                className="flex-1 p-3 bg-transparent outline-none text-sm"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>
            <button className="px-6 py-3 bg-primary text-white text-sm font-semibold hover:bg-primary-harsh transition-colors">
              SEARCH
            </button>
          </div>
        </div>

        {/* Ready to Get Started Banner */}
        <div className="mt-24 bg-primary rounded-xl p-8 text-white flex justify-between items-center">
          <h3 className="text-2xl font-bold">Ready to get started?</h3>
          <button className="px-6 py-2 bg-white text-black rounded-full text-sm font-semibold hover:bg-gray-100 transition-colors">
            CONTACT US
          </button>
        </div>
      </div>
    </section>
  );
} 