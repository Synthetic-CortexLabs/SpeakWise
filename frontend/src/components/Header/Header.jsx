import React from 'react'
import './Header.css'
import { assets } from '../../assets/assets'

const Header = () => {
  return (
    <div className='header'>
        <img src={assets.landing_page_image} alt="" />
    </div>
  )
}

export default Header