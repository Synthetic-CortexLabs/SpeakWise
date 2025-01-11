import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './pages/Home/Home'
import { About } from './pages/About/About'
import Login from './pages/Login/Login'
import Events from './pages/Events/Events'

const App = () => {
  return (
    <div className='app'>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/events' element={<Events/>}/>
      </Routes>
    </div>
  )
}

export default App