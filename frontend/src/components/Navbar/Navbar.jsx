import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';
import { assets } from '../../assets/assets.js';

const Navbar = () => {
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleNavClick = () => {
    setIsMenuOpen(false);
  };

  const isEventsActive = location.pathname.startsWith('/events');

  return (
    <div className={`navbar-container ${isScrolled ? 'scrolled' : ''}`}>
      <div className='navbar-left'>
        <h1>Speak<span>Wise</span></h1>
      </div>

      {/* Hamburger Menu Button */}
      <div className={`hamburger ${isMenuOpen ? 'active' : ''}`} onClick={toggleMenu}>
        <span></span>
        <span></span>
        <span></span>
      </div>

      {/* Desktop Navigation */}
      <ul className='navbar-center desktop-nav'>
        <Link to='/' onClick={handleNavClick} className={location.pathname === '/' ? 'active' : ''}>Home</Link>
        <Link to='/about' onClick={handleNavClick} className={location.pathname === '/about' ? 'active' : ''}>About</Link>
        <Link to='/#speakers' onClick={handleNavClick} className={location.hash === '#speakers' ? 'active' : ''}>Speakers</Link>
        <Link to='/events' onClick={handleNavClick} className={isEventsActive ? 'active' : ''}>Events</Link>
        <Link to='/review' onClick={handleNavClick} className={location.pathname === '/review' ? 'active' : ''}>Review</Link>
      </ul>

      {/* Mobile Navigation */}
      <div className={`mobile-nav ${isMenuOpen ? 'active' : ''}`}>
        <ul>
          <li><Link to='/' onClick={handleNavClick} className={location.pathname === '/' ? 'active' : ''}>Home</Link></li>
          <li><Link to='/about' onClick={handleNavClick} className={location.pathname === '/about' ? 'active' : ''}>About</Link></li>
          <li><Link to='/#speakers' onClick={handleNavClick} className={location.hash === '#speakers' ? 'active' : ''}>Speakers</Link></li>
          <li><Link to='/events' onClick={handleNavClick} className={isEventsActive ? 'active' : ''}>Events</Link></li>
          <li><Link to='/review' onClick={handleNavClick} className={location.pathname === '/review' ? 'active' : ''}>Review</Link></li>
        </ul>
      </div>

      <div className='navbar-right'>
        <img src={assets.vector} alt="" />
        <Link to='/login'><button>Get Started</button></Link>
      </div>
    </div>
  );
};

export default Navbar;