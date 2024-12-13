import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="absolute top-0 left-0 right-0 z-50 px-6 py-4 flex justify-between items-center">
      {/* Logo */}
      <Link href="/" className="text-xl font-bold text-white">
        Speak<span className="text-primary">Wise</span>
      </Link>

      {/* Navigation Links */}
      <div className="flex items-center space-x-6">
        <div className="hidden md:flex space-x-6 text-sm">
          <Link href="/" className="text-white hover:text-primary transition-colors">Home</Link>
          <Link href="/about" className="text-white hover:text-primary transition-colors">About</Link>
          <Link href="/speakers" className="text-white hover:text-primary transition-colors">Speakers</Link>
          <Link href="/events" className="text-white hover:text-primary transition-colors">Events</Link>
          <Link href="/review" className="text-white hover:text-primary transition-colors">Review</Link>
        </div>

        {/* Search Icon */}
        <button className="text-white p-1.5">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </button>

        {/* Explore Button */}
        <Link 
          href="/explore" 
          className="bg-white text-primary px-4 py-1.5 rounded-full text-sm font-medium hover:bg-primary hover:text-white transition-colors"
        >
          Explore
        </Link>
      </div>
    </nav>
  );
}
