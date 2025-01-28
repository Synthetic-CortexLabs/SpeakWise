import React, { useState, useEffect } from 'react'
import { useLocation, useParams } from 'react-router-dom';
import { events } from '../../assets/Events and Conferences/events';
import './Event.css';
import Navbar from '../../components/Navbar/Navbar';
import EventsFilter from '../../components/EventsFilter/EventsFilter';
import { assets } from '../../assets/assets';
import { sessions } from '../../assets/Sessions/sessions';
import Footer from '../../components/Footer/Footer';

const Event = () => {
  const [isDayDropdownOpen, setIsDayDropdownOpen] = useState(false);
  const [selectedDay, setSelectedDay] = useState('Day 1');
  const [currentPage, setCurrentPage] = useState(1);
  const [sessionsPerPage, setSessionsPerPage] = useState(8);
  const {eventId} = useParams();
  const location = useLocation();
  const eventDetails = location.state?.eventDetails || events.find(event => event.id === parseInt(eventId));

  useEffect(() => {
    const handleResize = () => {
      setSessionsPerPage(window.innerWidth <= 768 ? 4 : 8);
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  if (!eventDetails) {
    return <div>Event not found</div>;
  }

  const handleDayClick = () => {
    setIsDayDropdownOpen(!isDayDropdownOpen);
  };

  const handleDaySelect = (day) => {
    setSelectedDay(day);
    setIsDayDropdownOpen(false);
  };

  const totalPages = Math.ceil(sessions.length / sessionsPerPage);
  const indexOfLastSession = currentPage * sessionsPerPage;
  const indexOfFirstSession = indexOfLastSession - sessionsPerPage;
  const currentSessions = sessions.slice(indexOfFirstSession, indexOfLastSession);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  return (
    <div>
      <Navbar/>
      <div className="event-header">
        <h1>{eventDetails.title}</h1>
        <p>Annual Conference hosted in the {eventDetails.location.region} region in a town called {eventDetails.location.town}</p>
      </div>
      <EventsFilter/>
      <div className="event-grid-container">
        <div className="day-selector">
          <label htmlFor="day">Choose a Day <small>(if available)</small></label>
          <div className='selected-day' onClick={handleDayClick}>
            {selectedDay}<img src={assets.dropDown} alt="dropDown" />
          </div>
          {isDayDropdownOpen && (
            <div className="dropdown">
              <div onClick={() => handleDaySelect('Day 1')}>Day 1</div>
              <div onClick={() => handleDaySelect('Day 2')}>Day 2</div>
              <div onClick={() => handleDaySelect('Day 3')}>Day 3</div>
            </div>
          )}
        </div>
        <p>Select a Session</p>
        <div className='sessions-grid'>
          {currentSessions.map((session) => (
            <div className='session-card' key={session.id}>
              <img src={session.image} alt={session.name} />
              <div className='session-card-details'>
                <div className="session-card-details-left">
                  <h3>{session.name}</h3>
                  <p>Talk Title:</p>
                  <p>{session.description}</p>
                </div>
                <div className="session-card-details-right">
                  <p>Review</p>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className='events-pagination-container'>
          <div className='events-pagination'>
            <img 
              src={assets.previous} 
              alt="previous" 
              onClick={() => handlePageChange(currentPage - 1)} 
              style={{ opacity: currentPage === 1 ? 0.5 : 1, cursor: currentPage === 1 ? 'not-allowed' : 'pointer' }}
            />
            {[...Array(totalPages).keys()].map((number) => (
              <button
                key={number + 1}
                onClick={() => handlePageChange(number + 1)}
                className={currentPage === number + 1 ? 'active' : ''}
              >
                {number + 1}
              </button>
            ))}
            <img 
              src={assets.next} 
              alt="next"  
              onClick={() => handlePageChange(currentPage + 1)}
              style={{ opacity: currentPage === totalPages ? 0.5 : 1, cursor: currentPage === totalPages ? 'not-allowed' : 'pointer' }}
            />
          </div>
        </div>
      </div>
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

export default Event