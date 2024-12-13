import React, { useState } from 'react'
import './Navbar.css'
import { assets } from '../../assets/assets.js'

const Navbar = () => {
  const [page, setPage] = useState("home")
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen)
  }

  const handleNavClick = (pageName) => {
    setPage(pageName)
    setIsMenuOpen(false)
  }
  
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
          <a href='#home' onClick={()=>handleNavClick("home")} className={page==="home"?"active":""}>Home</a>
          <a href='#about' onClick={()=>handleNavClick("about")} className={page==="about"?"active":""}>About</a>
          <a href='#speakers' onClick={()=>handleNavClick("speakers")} className={page==="speakers"?"active":""}>Speakers</a>
          <a href='#events' onClick={()=>handleNavClick("events")} className={page==="events"?"active":""}>Events</a>
          <a href='#review' onClick={()=>handleNavClick("review")} className={page==="review"?"active":""}>Review</a>
        </ul>

        {/* Mobile Navigation */}
        <div className={`mobile-nav ${isMenuOpen ? 'active' : ''}`}>
          <ul>
            <li><a href='#home' onClick={()=>handleNavClick("home")} className={page==="home"?"active":""}>Home</a></li>
            <li><a href='#about' onClick={()=>handleNavClick("about")} className={page==="about"?"active":""}>About</a></li>
            <li><a href='#speakers' onClick={()=>handleNavClick("speakers")} className={page==="speakers"?"active":""}>Speakers</a></li>
            <li><a href='#events' onClick={()=>handleNavClick("events")} className={page==="events"?"active":""}>Events</a></li>
            <li><a href='#review' onClick={()=>handleNavClick("review")} className={page==="review"?"active":""}>Review</a></li>
          </ul>
        </div>

        <div className='navbar-right'>
          <img src={assets.vector} alt="" />
          <button>Get Started</button>
        </div>
    </div>
  )
}

export default Navbar