import React from 'react'
import './About.css'
import Navbar from '../../components/Navbar/Navbar'
import { team_members } from '../../assets/assets'
import ContactUs from '../../components/ContactUs/ContactUs'
import Footer from '../../components/Footer/Footer'

export const About = () => {
  return (
    <div>
      <Navbar/>
      <div className="about-header">
        <h1>What we do?</h1>
        <p>A Conference feedback platform that facilitates speaker feedback, provides analytics for organizers, and enhances the conference experience for attendees.</p>
      </div>
      <div className="mission-and-values">
        <h1>Building Global Speakers</h1>
        <div className="missions">
          <div>
            <button>Mission Statement</button>
            <p>Empowering conference organizers and speakers to deliver exceptional experiences through meaningful feedback and analytics.</p>
          </div>
          <div>
            <button>Our Story</button>
            <p>Speak<span>Wise</span> was founded with the goal of revolutionizing the way conferences are organized and experienced. Our team is passionate about creating a platform that helps speakers improve and attendees have a better time.</p>
          </div>
        </div>
        <h1>Values</h1>
        <div className="values">
          <div><p>Transparency</p></div>
          <div><p>Collaboration</p></div>
          <div><p>Continuous Improvement</p></div>
        </div>
      </div>
      <div className="meet-our-team">
        <h1>Meet our team</h1>
        <p>Join us!</p>
        <div className="team-container">
          {team_members.map(member => (
            <div key={member._id} className="team-member">
              <div className="team-member-image-container">
                <img src={member.image} alt={member.name} className="team-member-image" />
                <h2 className='team-member-name-mobile'>{member.name}</h2>
              </div>
              <div className="team-member-info">
                <h2 className='team-member-name-desktop'>{member.name}</h2>
                <p>{member.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
      <ContactUs/>
      <Footer/>
    </div>
  )
}
