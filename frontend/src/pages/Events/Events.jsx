import React, { useState } from 'react'
import './Events.css'
import Navbar from '../../components/Navbar/Navbar'
import { assets, eventsFilter } from '../../assets/assets'
import { events } from '../../assets/Events and Conferences/events';
import Footer from '../../components/Footer/Footer';

const regions = ['Africa', 'Asia', 'Europe'];
const countries = {
  Africa: ['Ghana', 'Nigeria', 'Kenya'],
  Asia: ['India', 'China', 'Japan'],
  Europe: ['Germany', 'France', 'UK'],
};

const Events = () => {
  const [selectedRegion, setSelectedRegion] = useState('');
  const [selectedCountry, setSelectedCountry] = useState('');
  const [isRegionDropdownOpen, setIsRegionDropdownOpen] = useState(false);
  const [isCountryDropdownOpen, setIsCountryDropdownOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const eventsPerPage = 6;

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

  return (
    <div className='events-container'>
        <Navbar/>
        <div className='events-header'>
            <h1>Conferences & Events</h1>
            <p>All conferences and events here, local and international.</p>
        </div>
        <div className="events-filter">
            {eventsFilter.map((event) => (
                <button key={event._id} className='events-filter-button'>{event.name}</button>
            ))}
        </div>
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
                        <img src={event.image} alt={event.title} />
                        <div className='event-card-details'>
                        <div className="event-card-details-left">
                            <h3>{event.title}</h3>
                        <p>{event.location}</p>
                    </div>
                    <div className="event-card-details-right">
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
    </div>
  )
}

export default Events