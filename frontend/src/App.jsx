// import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './pages/Home/Home'
import { About } from './pages/About/About'
import Login from './pages/Login/Login'
import Events from './pages/Events/Events'
import Event from './pages/Event/Event'
import ScrollToTop from './components/ScrollToTop/ScrollToTop';
import { Toaster } from 'react-hot-toast';


const App = () => {
  return (
    <div className='app'>
      <Toaster position='top-right' />
      <ScrollToTop />
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/events' element={<Events/>}/>
        <Route path='/events/:eventId' element={<Event/>}/>
      </Routes>
    </div>
  )
}

export default App