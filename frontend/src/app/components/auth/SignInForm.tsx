'use client';

import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';

export default function SignInForm() {
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission
    console.log(formData);
  };

  return (
    <div className="h-screen flex items-center justify-center p-4 bg-gray-50">
      <div className="w-full max-w-5xl h-[90vh] flex rounded-3xl overflow-hidden bg-white shadow-2xl">
        {/* Left Side - Promo Content */}
        <div className="w-1/2 bg-black text-white p-10 flex flex-col justify-center relative overflow-hidden">
          {/* Background Image */}
          <div className="absolute inset-0 bg-[url('/images/conference-bg.jpg')] bg-cover bg-center opacity-40" />
          
          <div className="relative z-10">
            <div className="mb-8">
              <h1 className="text-xl font-bold">
                Speak<span className="text-primary">Wise</span>
              </h1>
            </div>
            <div>
              <h2 className="text-4xl font-bold leading-tight mb-6">
                Review talks from<br />
                <span className="text-primary">conferences</span> you<br />
                attended
              </h2>
              <p className="text-gray-400 text-base">
                Whichever tech conference you attended<br />
                recently, you can find your favourite speaking<br />
                sessions and leave reviews and feedback.
              </p>
            </div>
          </div>
        </div>

        {/* Right Side - Sign In Form */}
        <div className="w-1/2 p-10 flex flex-col justify-center">
          <div className="w-full max-w-md mx-auto">
            <h2 className="text-2xl font-bold mb-2">Welcome back!</h2>
            <p className="text-gray-600 mb-8 text-sm">
              Don't have an account?{' '}
              <Link href="/auth/signup" className="text-primary hover:underline">
                Sign Up
              </Link>
            </p>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                  Email Address
                </label>
                <input
                  type="email"
                  id="email"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full px-3 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition-all text-sm"
                  required
                />
              </div>

              <div>
                <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">
                  Password
                </label>
                <div className="relative">
                  <input
                    type={showPassword ? "text" : "password"}
                    id="password"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    className="w-full px-3 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition-all text-sm"
                    required
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-1/2 -translate-y-1/2"
                  >
                    <svg 
                      className="w-4 h-4 text-gray-400" 
                      fill="none" 
                      viewBox="0 0 24 24" 
                      stroke="currentColor"
                    >
                      {showPassword ? (
                        <path 
                          strokeLinecap="round" 
                          strokeLinejoin="round" 
                          strokeWidth={2} 
                          d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"
                        />
                      ) : (
                        <path 
                          strokeLinecap="round" 
                          strokeLinejoin="round" 
                          strokeWidth={2} 
                          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                        />
                      )}
                    </svg>
                  </button>
                </div>
              </div>

              <div className="text-right">
                <Link href="/auth/recover" className="text-sm text-primary hover:underline">
                  Forgot Password?
                </Link>
              </div>

              <button
                type="submit"
                className="w-full bg-primary text-white py-2.5 rounded-lg text-sm font-semibold hover:bg-primary-harsh transition-colors mt-6"
              >
                Sign In
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
} 