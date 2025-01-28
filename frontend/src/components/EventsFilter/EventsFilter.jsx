import React from 'react'
import './EventsFilter.css';
import { eventsFilter } from '../../assets/assets';

const EventsFilter = () => {
  return (
    <div className="events-filter">
        {eventsFilter.map((event) => (
            <button key={event._id} className='events-filter-button'>{event.name}</button>
        ))}
    </div>
  )
}

export default EventsFilter