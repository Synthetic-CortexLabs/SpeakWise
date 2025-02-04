import React, { useState, useEffect } from 'react'
import './Events.css'
import Navbar from '../../components/Navbar/Navbar'
import { assets} from '../../assets/assets'
import { events } from '../../assets/Events and Conferences/events';
import Footer from '../../components/Footer/Footer';
import { useNavigate } from 'react-router-dom';
import EventsFilter from '../../components/EventsFilter/EventsFilter';
import { getEvents } from '../../services/api';
import{toast} from "react-hot-toast";
import axios from 'axios';

const Events = () => {
  const [selectedRegion, setSelectedRegion] = useState('');
  const [selectedCountry, setSelectedCountry] = useState('');
  const [isRegionDropdownOpen, setIsRegionDropdownOpen] = useState(false);
  const [isCountryDropdownOpen, setIsCountryDropdownOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const eventsPerPage = 6;
  const [regions, setRegions] = useState([]);
  const [countries, setCountries] = useState({});
  const navigate = useNavigate();
  const [isReviewConfirmModalOpen, setIsReviewConfirmModalOpen] = useState(false);
  const [isVerifyModalOpen, setIsVerifyModalOpen] = useState(false);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCountries = async () => {
      try {
        const response = await fetch('https://restcountries.com/v3.1/all');
        const data = await response.json();
        
        // Group countries by region
        const groupedByRegion = data.reduce((acc, country) => {
          const region = country.region;
          if (!acc[region]) {
            acc[region] = [];
          }
          acc[region].push(country.name.common);
          return acc;
        }, {});
        
        setRegions(Object.keys(groupedByRegion));
        setCountries(groupedByRegion);
      } catch (error) {
        console.error('Error fetching countries:', error);
      }
    };

    fetchCountries();
  }, []);


  const [eventData, setEventData] = useState({
    event_image: '',
    event_nickname: '',
    country: ''
  });

  useEffect(() => {
    // Replace with your actual API endpoint
    const apiUrl = `https://speakwise.onrender.com/api/events`;


    axios.get(apiUrl, {timeout: 7000})
      .then(response => {
        const data = response.data;
        setEventData({
          event_image: data.event_image,
          event_nickname: data.event_nickname,
          country: data.country[0].name // Assuming country is an array and we want the first item's name
        });
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data: ', error);
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className='loading'>
    <p>Loading Events...</p>
    <div className="loader"></div>
  </div>;
  if (error) return <div className='error'>
    <div className='error-message'>Failed to fetch events</div>
    {toast.error('Failed to fetch events')}
  </div>;






  const handleRegionClick = () => {
    setIsRegionDropdownOpen(!isRegionDropdownOpen);
    setIsCountryDropdownOpen(false);
  };

  const handleCountryClick = () => {
    setIsCountryDropdownOpen(!isCountryDropdownOpen);
  };

  const handleRegionSelect = (region) => {
    setSelectedRegion(region);
    setSelectedCountry('');
    setIsRegionDropdownOpen(false);
  };

  const handleCountrySelect = (country) => {
    setSelectedCountry(country);
    setIsCountryDropdownOpen(false);
  };

  const totalPages = Math.ceil(events.length / eventsPerPage);
  const indexOfLastEvent = currentPage * eventsPerPage;
  const indexOfFirstEvent = indexOfLastEvent - eventsPerPage;
  const currentEvents = events.slice(indexOfFirstEvent, indexOfLastEvent);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const handleStartReview = (event) => {
    setSelectedEvent(event);
    setIsReviewConfirmModalOpen(true);
  };

  const handleVerifyAndNavigate = (event) => {
    // Close both modals
    setIsVerifyModalOpen(false);
    setIsReviewConfirmModalOpen(false);
    
    // Navigate to event page
    navigate(`/events/${event.id}`, { state: { eventDetails: event } });
  };
 


  return (
    <div className='events-container'>
        <Navbar/>
        <div className='events-header'>
            <h1>Conferences & Events</h1>
            <p>All conferences and events here, local and international.</p>
        </div>
        <EventsFilter/>
        <div className="events-grid-container">
            <div className="country-and-region">
                <div className="region" onClick={handleRegionClick}>
                    <label htmlFor="region">Select Region</label>
                    <div className='selected-region'>{selectedRegion || "Select Region"} <img src={assets.dropDown} alt="dropDown" /></div>
                    {isRegionDropdownOpen && (
                        <div className="dropdown">
                            {regions.map((region) => (
                                <div key={region} onClick={() => handleRegionSelect(region)}>{region}</div>
                            ))}
                        </div>
                    )}
                </div>
                <div className="country" onClick={handleCountryClick}>
                    <label htmlFor="country">Country</label>
                    <div className='selected-country'>{selectedCountry || "Country"} <img src={assets.dropDown} alt="dropDown" /></div>
                    {isCountryDropdownOpen && selectedRegion && (
                        <div className="dropdown">
                            {countries[selectedRegion].map((country) => (
                                <div key={country} onClick={() => handleCountrySelect(country)}>{country}</div>
                            ))}
                        </div>
                    )}
                </div>
            </div>
            <p>All conference & Events in {selectedCountry}</p>
            <div className='events-grid'>
                {currentEvents.map((event) => (
                    <div className='event-card' key={event.id}>
                        <img src={eventData.event_image} alt={eventData.event_nickname} />
                        <div className='event-card-details'>
                        <div className="event-card-details-left">
                            <h3>{eventData.event_nickname}</h3>
                        <p>{eventData.country}</p>
                    </div>
                    <div className="event-card-details-right" onClick={() => handleStartReview(event)}>
                        <p>Start Review</p>
                        <img src={assets.reviewIcon} alt="reviewIcon" />
                    </div>
                    </div>

                </div>
            ))}
            </div>
            <div className='events-pagination-container'>
                <div className='events-pagination'>
                        <img src={assets.previous} alt="previous" onClick={() => handlePageChange(currentPage - 1)} disabled={currentPage === 1}/>
                {[...Array(totalPages).keys()].map((number) => (
                    <button
                        key={number + 1}
                        onClick={() => handlePageChange(number + 1)}
                        className={currentPage === number + 1 ? 'active' : ''}
                    >
                        {number + 1}
                    </button>
                ))}
                    <img src={assets.next} alt="next"  onClick={() => handlePageChange(currentPage + 1)} disabled={currentPage === totalPages}/>
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
        {isReviewConfirmModalOpen && (
        <div className="review-confirm-modal">
          <div className="review-confirm-modal-content">
            <img  className='close-modal-icon' src={assets.closeModal} alt="closeModal" onClick={() => setIsReviewConfirmModalOpen(false)} />
            <h1>Which one is you?</h1>



            <p>Let&apos;s us know where you watched this session from.</p>


            <div className='physical-or-youtube'>
              <div className='physical-or-youtube-left' onClick={() => {setIsVerifyModalOpen(true); setIsReviewConfirmModalOpen(false)}}>
                <img src={assets.physical} alt="physical" />
                <p>Physically Attended</p>
              </div>
              <div className='physical-or-youtube-right'>
                <img src={assets.youtube} alt="youtube" />
                <p>Watched on Youtube</p>
              </div>
            </div>
            <p>@Speak<span>Wise</span></p>


          </div>
        </div>
        )}
        {isVerifyModalOpen && (
        <div className='verify-modal'>
          <div className='verify-modal-content'>
            <img  className='close-modal-icon' src={assets.closeModal} alt="closeModal" onClick={() => {setIsVerifyModalOpen(false); setIsReviewConfirmModalOpen(false)}} />
            <h1>Lets verify you</h1>


            <p>We want to be sure you attended the conference. <br />Please provide your email below</p>
            <input type="email" placeholder='Enter your email' />
            <button onClick={() => handleVerifyAndNavigate(selectedEvent)}>Verify</button>
          </div>
        </div>
        )}
    </div>




  )
}

export default Events