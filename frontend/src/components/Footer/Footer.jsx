import React from 'react'
import { Link } from 'react-router-dom'
import './Footer.css'
import { assets } from '../../assets/assets'

const Footer = () => {
  return (
    <div className="footer">
          <div className='footer-top'>
            <h1>Speak<span>Wise</span></h1>
          </div>
            <div className='footer-middle'>
            <div className='footer-links'>
                <ul className='footer-links-left'>
                <Link to='/'>Home</Link>
                <Link to='/about'>About</Link>
                <Link to='#speakers'>Speakers</Link>
                </ul>
                <div className='footer-links-right'>
                <Link to='/events'>Events</Link>
                <Link to='#review'>Review</Link>
                <Link to='#contact'>Contact us</Link>
                </div>
            </div>
            </div>
          <div className='footer-bottom'>
            <div className='social-icons'>
              <img src={assets.twitter} alt="" />
              <img src={assets.linkedin} alt="" />
              <img src={assets.instagram} alt="" />
              <img src={assets.facebook} alt="" />
            </div>
            <div className='footer-bottom'>
              <p> Copyright© 2024. SpeakWise. <br/> All rights reserved.</p>
            </div>
          </div>
        </div>
  )
}

export default Footer