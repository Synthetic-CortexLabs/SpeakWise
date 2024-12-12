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
    </div>
  )
}

export default Home