import React from 'react'
import './Home.css'
import Header from '../../components/Header/Header'
import { assets } from '../../assets/assets'

const Home = () => {
  return (
    <div>
        <Header/>
        <div className='frameworks-container'>
          <img src={assets.pyconAfrica} alt="" />
          <img src={assets.googleIoExtended1} alt="" />
          <img src={assets.devfest} alt="" />
          <img src={assets.flutter1} alt="" />
        </div>
        <div className="devfest-info">
          <div className='devfest-info-left'>
            <h1>Speak-<span>Wise</span></h1>
            <ul>
              <li>Gives you access to conferences you attended.</li>
              <li>Gives you an opportunity to review talks or conferences you attended.</li>
              <li>Gives you the power to track your speaking engagements.</li>
            </ul>
            <ul>
              <li>Gives you access to conferences you attended.</li>
              <li>Gives you an opportunity to review talks or conferences you attended.</li>
              <li>Gives you the power to track your speaking engagements.</li>
            </ul>
          </div>
          <div className='devfest-info-right'>
            <img className='devfest-uk' src={assets.devfestUk} alt="" />
            <img className='devfest-namibia' src={assets.pyconNamibia} alt="" />
          </div>
        </div>
        <div  className='how-it-works'>
        <div className="how-it-works-top">
          <h1>See How It <span>Works</span></h1>
          <p>How was your conference experience? Share your thoughts and help shape the future of speaking with Speak<span>Wise</span>.</p>
        </div>
        <div className='how-it-works-grid'>
          <div className='how-it-works-grid-item'>
            <img src={assets.EarthGlobe} alt="" />
            <b>Select a Country</b>
            <p>After you logon to Speak<span>Wise</span>, you go ahead to select the country in which the conference was hosted.</p>
          </div>
          <div className='how-it-works-grid-item'>
            <img src={assets.Region} alt="" />
            <b>Select a Region</b>
            <p>In the selected country, you can now select the Region where the conference was held</p>
          </div>
          <div className='how-it-works-grid-item'>
            <img src={assets.Conference} alt="" />
            <b>Select the Conference/Event</b>
            <p>Now you can go ahead and select the conference you attended, all conferences attended will be available here</p>
          </div>
          <div className='how-it-works-grid-item'>
            <img src={assets.Calender} alt="" />
            <b>Choose the Day</b>
            <p>Normally, some conferences are hosted over several days, in which you select the day you attended.</p>
          </div>
          <div className='how-it-works-grid-item'>
            <img src={assets.Training} alt="" />
            <b>Select the Speaker</b>
            <p>Now go ahead and select the speaker you want rate or give review.</p>
          </div>
          <div className='how-it-works-grid-item'>
            <img src={assets.Thumbs} alt="" />
            <b>Give Speaker Feedback</b>
            <p>Go ahead and rate and give a speaker a feedback, note your feedback are anonymous.</p>
          </div>
        </div>
        </div>
        <div className="contact-container">
        <div className="contact-container-top">
            <div className="contact-container-left">
            <h1><span>Got Any Questions?</span></h1>
            <h1>We&apos;ve Got Answers</h1>
          </div>
          <div className="contact-container-right">
            <input type="email" placeholder='Email' />
            <button>Connect</button>
          </div>
        </div>
        <div className="contact-container-bottom">
          <div className="contact-us">
            <p>Ready to get started?</p>
            <button>CONTACT US</button>
        </div>
        </div>
        </div> 
        <div className="footer">
          <div className='footer-top'>
            <h1>Speak<span>Wise</span></h1>
          </div>
          <div className='footer-middle'>
            <ul>
              <a href='#home'>Home</a>
              <a href='#about'>About</a>
              <a href='#speakers'>Speakers</a>
              <a href='#events'>Events</a>
              <a href='#review'>Review</a>
              <a href='#contact'>Contact Us</a>
            </ul>
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
        
    </div>
  )
}

export default Home