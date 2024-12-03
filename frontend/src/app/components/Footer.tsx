import Link from 'next/link';
import Image from 'next/image';

export default function Footer() {
  const socialLinks = [
    { href: 'https://twitter.com/speakwise', icon: '/images/social/twitter.svg', label: 'Twitter' },
    { href: 'https://instagram.com/speakwise', icon: '/images/social/instagram.svg', label: 'Instagram' },
    { href: 'https://facebook.com/speakwise', icon: '/images/social/facebook.svg', label: 'Facebook' },
    { href: 'https://linkedin.com/company/speakwise', icon: '/images/social/linkedin.svg', label: 'LinkedIn' },
  ];

  const navLinks = [
    { href: '/', label: 'Home' },
    { href: '/about', label: 'About' },
    { href: '/speakers', label: 'Speakers' },
    { href: '/events', label: 'Events' },
    { href: '/review', label: 'Review' },
    { href: '/contact', label: 'Contact us' },
  ];

  return (
    <footer className="bg-black text-white py-16">
      <div className="container mx-auto px-6">
        {/* Logo */}
        <div className="text-center mb-12">
          <Link href="/" className="text-3xl font-bold inline-block">
            Speak<span className="text-primary">Wise</span>
          </Link>
        </div>

        {/* Navigation */}
        <nav className="mb-12">
          <ul className="flex justify-center space-x-8">
            {navLinks.map((link) => (
              <li key={link.label}>
                <Link 
                  href={link.href}
                  className="hover:text-primary transition-colors"
                >
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        {/* Social Links */}
        <div className="flex justify-center space-x-6 mb-12">
          {socialLinks.map((social) => (
            <a
              key={social.label}
              href={social.href}
              target="_blank"
              rel="noopener noreferrer"
              className="w-10 h-10 flex items-center justify-center"
            >
              <Image
                src={social.icon}
                alt={social.label}
                width={24}
                height={24}
                className="text-white"
              />
            </a>
          ))}
        </div>

        {/* Copyright */}
        <div className="text-center text-sm">
          <p className="mb-2">Copyright © 2024 SpeakWise</p>
          <p>All Rights Reserved.</p>
        </div>
      </div>
    </footer>
  );
} 