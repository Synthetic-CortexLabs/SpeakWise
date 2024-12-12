import React, { useState } from 'react'
import './Navbar.css'
import { assets } from '../../assets/assets.js'

const Navbar = () => {
  const [page, setPage] = useState("home")
  
  return (
    <div className='navbar-container'>
        <div className='navbar-left'>
          <h1>Speak<span>Wise</span></h1>
        </div>
        <ul className='navbar-center'>
          <a href='#home' onClick={()=>setPage("home")} className={page==="home"?"active":""}>Home</a>
          <a href='#about' onClick={()=>setPage("about")} className={page==="about"?"active":""}>About</a>
          <a href='#speakers' onClick={()=>setPage("speakers")} className={page==="speakers"?"active":""}>Speakers</a>
          <a href='#events' onClick={()=>setPage("events")} className={page==="events"?"active":""}>Events</a>
          <a href='#review' onClick={()=>setPage("review")} className={page==="review"?"active":""}>Review</a>
        </ul>
        <div className='navbar-right'>
          <img src={assets.vector} alt="" />
          <button>Get Started</button>
        </div>
    </div>
  )
}

export default Navbar