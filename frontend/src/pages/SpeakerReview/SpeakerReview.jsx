import React, { useState } from 'react'
import './SpeakerReview.css'
import Navbar from '../../components/Navbar/Navbar'
import { assets } from '../../assets/assets'
import Footer from '../../components/Footer/Footer'

const SpeakerReview = () => {
  // Add state for tracking selected ratings
  const [ratings, setRatings] = useState({
    engagement: null,
    clarity: null,
    contentDepth: null,
    speakerKnowledge: null,
    practicalRelevance: null
  });

  // Handler for rating clicks
  const handleRatingClick = (category, value) => {
    setRatings(prev => ({
      ...prev,
      [category]: value
    }));
  };

  return (
    <div className='speaker-review-container'>
        <Navbar/>
        <div className='speaker-review-header'>
            <h1>Speaker Feedback</h1>
            <p>Empowering Global Voices. Elevating Impact. Honest Feedback for Exceptional Speakers.</p>
        </div>
        <div className='speaker-review-body'>
            <div className='speaker-review-body-left'>
                <div className="speaker-profile">
                    <div className="speaker-profile-header">
                        <h1>Speaker Profile</h1>
                    </div>
                    <div className="speaker-profile-image">
                        <img src={assets.speakerProfileTestimg} alt="" />
                    </div>
                    <div className="speaker-profile-details">
                        <p>Fred Pekyi</p>
                        <p>Frontend web developer at Speakwise</p>
                    </div>
                    <div className="speaker-profile-rating">
                        <div className='a'>
                            <div>
                                <img src={assets.reviewCalender} alt="" />
                                <p>12</p>
                            </div>
                            <div>
                                <p>Sessions Given</p>
                            </div>
                        </div>
                        <div className='b'>
                            <div>
                                <img src={assets.people} alt="" />
                                <p>156</p>
                            </div>
                            <div>
                                <p>Total Attendees</p>
                            </div>
                        </div>
                        <div className='c'>
                            <div>
                                <img src={assets.trophy} alt="" />
                                <p>4.8</p>
                                <img src={assets.reviewFullStar} alt="" />
                                <img src={assets.reviewFullStar} alt="" />
                                <img src={assets.reviewFullStar} alt="" />
                                <img src={assets.reviewFullStar} alt="" />
                                <img src={assets.reviewHalfStar} alt="" />
                            </div>
                            <div>
                                <p>Average Rating</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="talk-session">
                    <div className="talk-session-header">
                        <h1>Talk Session</h1>
                    </div>
                    <div className="session-topic">
                        <h2>Reinforcement using Python,</h2>
                    </div>
                    <div className="event-details">
                        <h1>Event Details</h1>
                        <div className="event-details-table">
                           <table>
                            <tr>
                                <td>Name:</td>
                                <td>Python Ho</td>
                            </tr>
                            <tr>
                                <td>Date:</td>
                                <td>21 Sep - 25 Sep 2024</td>
                            </tr>
                            <tr>
                                <td>Location:</td>
                                <td>University and Health and Applied Science</td>
                            </tr>
                           </table>
                        </div>
                    </div>
                </div>
                <div className="speaker-socials">
                    <div className="speaker-socials-header">
                        <h1>Connect with the Speaker</h1>
                    </div>
                    <div className="speaker-socials-body">
                        <img src={assets.linkedin} alt="" />
                        <img src={assets.twitter} alt="" />
                        <img src={assets.facebook} alt="" />
                    </div>
                </div>
            </div>
            <div className='speaker-review-body-right'>
                <div className='speaker-rater-header'>
                    <h1>Speaker Feedback</h1>
                    <p>Please rate the speaker on the following criteria from 1 to 10</p>
                </div>
                <div className='Engagement'>
                    <h1>Engagement</h1>
                    <p>How well did the speaker maintain audience interest?</p>
                    <div className='Engagement-rating'>
                        {[1,2,3,4,5,6,7,8,9,10].map((num) => (
                            <p
                                key={num}
                                className={ratings.engagement === num ? 'active' : ''}
                                onClick={() => handleRatingClick('engagement', num)}
                            >
                                {num}
                            </p>
                        ))}
                    </div>
                </div>
                <div className='clarity'>
                    <h1>Clarity</h1>
                    <p>How clear and understandable was the presentation?</p>
                    <div className='clarity-rating'>
                        {[1,2,3,4,5,6,7,8,9,10].map((num) => (
                            <p
                                key={num}
                                className={ratings.clarity === num ? 'active' : ''}
                                onClick={() => handleRatingClick('clarity', num)}
                            >
                                {num}
                            </p>
                        ))}
                    </div>
                </div>
                <div className="content-depth">
                    <h1>Content Depth</h1>
                    <p>How would you rate the depth of the content covered? </p>
                    <div className='content-depth-rating'>
                        {[1,2,3,4,5,6,7,8,9,10].map((num) => (
                            <p
                                key={num}
                                className={ratings.contentDepth === num ? 'active' : ''}
                                onClick={() => handleRatingClick('contentDepth', num)}
                            >
                                {num}
                            </p>
                        ))}
                    </div>
                </div>
                <div className="speaker-knowledge">
                    <h1>Speaker Knowledge</h1>
                    <p>How knowledgeable did the speaker seem about the topic?</p>
                    <div className='speaker-knowledge-rating'>
                        {[1,2,3,4,5,6,7,8,9,10].map((num) => (
                            <p
                                key={num}
                                className={ratings.speakerKnowledge === num ? 'active' : ''}
                                onClick={() => handleRatingClick('speakerKnowledge', num)}
                            >
                                {num}
                            </p>
                        ))}
                    </div>
                </div>
                <div className="practical-relevance">
                    <h1>Practical Relevance</h1>
                    <p>How relevant was the content to practical applications?</p>
                    <div className='practical-relevance-rating'>
                        {[1,2,3,4,5,6,7,8,9,10].map((num) => (
                            <p
                                key={num}
                                className={ratings.practicalRelevance === num ? 'active' : ''}
                                onClick={() => handleRatingClick('practicalRelevance', num)}
                            >
                                {num}
                            </p>
                        ))}
                    </div>
                </div>
                <div className="additional-comments">
                    <h1>Additional Comments</h1>
                    <p>Share any additional feedback you have for the speaker </p>
                    <textarea name="" id="" cols="30" rows="20"></textarea>
                </div>
                <div className='submit-button'>
                    <button>Submit Feedback</button>
                </div>
            </div>
        </div>
        {/* Contact Container */}
      <div className="events-contact-container">
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
        <Footer/>
    </div>
    
  )
}

export default SpeakerReview