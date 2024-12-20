import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';
import { assets } from '../../assets/assets.js';

const Navbar = () => {
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleNavClick = () => {
    setIsMenuOpen(false);
  };

  return (
    <div className='navbar-container'>
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
        <Link to='/#events' onClick={handleNavClick} className={location.hash === '#events' ? 'active' : ''}>Events</Link>
        <Link to='/#review' onClick={handleNavClick} className={location.hash === '#review' ? 'active' : ''}>Review</Link>
      </ul>

      {/* Mobile Navigation */}
      <div className={`mobile-nav ${isMenuOpen ? 'active' : ''}`}>
        <ul>
          <li><Link to='/' onClick={handleNavClick} className={location.pathname === '/' ? 'active' : ''}>Home</Link></li>
          <li><Link to='/about' onClick={handleNavClick} className={location.pathname === '/about' ? 'active' : ''}>About</Link></li>
          <li><Link to='/#speakers' onClick={handleNavClick} className={location.hash === '#speakers' ? 'active' : ''}>Speakers</Link></li>
          <li><Link to='/#events' onClick={handleNavClick} className={location.hash === '#events' ? 'active' : ''}>Events</Link></li>
          <li><Link to='/#review' onClick={handleNavClick} className={location.hash === '#review' ? 'active' : ''}>Review</Link></li>
        </ul>
      </div>

      <div className='navbar-right'>
        <img src={assets.vector} alt="" />
        <button>Get Started</button>
      </div>
    </div>
  );
};

export default Navbar;