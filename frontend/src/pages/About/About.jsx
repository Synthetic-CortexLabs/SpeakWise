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
        <p>Whichever tech conference you attended can be found here</p>
        <p>Gives you access to conferences you attended. <br />
            Gives you an opportunity to review talks or conferences you attended. <br />
            Gives you the power to track your speaking engagements.</p>
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
