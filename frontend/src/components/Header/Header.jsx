import React from 'react'
import { Link } from 'react-router-dom'
import './Header.css'


const Header = () => {
  return (
      <>
        <div className = 'header'>
          <div className = "header-contents">
            <h2>Have Access To <br/> <span>Conferences</span> You Attended?</h2>
            <p>Whichever tech conference you attended can be found here</p>
            <div className = "header-contents-buttons"> 
              <Link to='/login'><button className='get-started-button'>Get Started</button></Link>
              <button>Request Demo</button>
            </div>
          </div>
        </div>
      </>
      )
}

export default Header