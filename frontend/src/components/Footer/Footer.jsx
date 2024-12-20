import React from 'react'
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
                <div className='footer-links-left'>
                <a href='#home'>Home</a>
                <a href='#about'>About</a>
                <a href='#speakers'>Speakers</a>
                </div>
                <div className='footer-links-right'>
                <a href='#events'>Events</a>
                <a href='#review'>Review</a>
                <a href='#contact'>Contact us</a>
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