'use client';

import Link from 'next/link';

export default function UserTypeSelection() {
  return (
    <div className="h-screen flex items-center justify-center p-4 bg-gray-50">
      <div className="w-full max-w-5xl h-[90vh] flex rounded-3xl overflow-hidden bg-white shadow-2xl">
        {/* Left Side - Promo Content */}
        <div className="w-1/2 bg-black text-white p-10 flex flex-col justify-center relative overflow-hidden">
          {/* Background Image */}
          <div className="absolute inset-0 bg-[url('/images/conference-bg.jpg')] bg-cover bg-center opacity-50" />
          
          <div className="relative z-10">
            <div className="mb-8">
              <h1 className="text-xl font-bold">
                Speak<span className="text-primary">Wise</span>
              </h1>
            </div>
            <div>
              <h2 className="text-4xl font-bold leading-tight mb-6">
                You need to track<br />
                your Speaking<br />
                engagements?
              </h2>
              <p className="text-gray-400 text-base">
                Whichever tech conference you attended<br />
                recently, you can find your favourite speaking<br />
                sessions and leave reviews and feedback.
              </p>
            </div>
          </div>
        </div>

        {/* Right Side - Auth Content */}
        <div className="w-1/2 p-10 flex flex-col justify-center">
          <div className="w-full max-w-md mx-auto">
            {/* Logo and Title */}
            <div className="text-center mb-8">
              <h1 className="text-2xl font-bold mb-2">
                Speak<span className="text-primary">Wise</span>
              </h1>
              <p className="text-gray-600 text-sm">Select User Type</p>
            </div>

            {/* User Type Buttons */}
            <div className="space-y-3">
              <Link
                href="/auth/attendee"
                className="block w-full bg-primary text-white text-center py-2.5 rounded-lg text-sm font-semibold hover:bg-primary-harsh transition-colors"
              >
                Sign In as Attendee
              </Link>
              
              <Link
                href="/auth/speaker"
                className="block w-full bg-primary text-white text-center py-2.5 rounded-lg text-sm font-semibold hover:bg-primary-harsh transition-colors"
              >
                Sign In as Speaker
              </Link>
              
              <Link
                href="/auth/organizer"
                className="block w-full bg-primary text-white text-center py-2.5 rounded-lg text-sm font-semibold hover:bg-primary-harsh transition-colors"
              >
                Sign In as Organizer
              </Link>
            </div>

            {/* Sign Up Link */}
            <div className="mt-6 text-center">
              <p className="text-gray-600 text-sm">
                Don't have an account?{' '}
                <Link href="/auth/signup" className="text-primary hover:underline">
                  Sign Up
                </Link>
              </p>
            </div>

            {/* Social Links */}
            <div className="mt-8">
              <p className="text-gray-600 mb-3 text-center text-sm">Connect with us</p>
              <div className="flex justify-center space-x-4">
                <Link
                  href="https://linkedin.com/company/speakwise"
                  target="_blank"
                  className="text-black hover:text-primary transition-colors"
                >
                  <svg className="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                  </svg>
                </Link>
                <Link
                  href="https://twitter.com/speakwise"
                  target="_blank"
                  className="text-black hover:text-primary transition-colors"
                >
                  <svg className="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                  </svg>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
} 