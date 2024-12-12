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
        <div className="devfest-info">
          <div className='devfest-info-left'>
            <h1>Speak-<span>Wise</span></h1>
            <ul>
              <li>Gives you access to conferences you attended.</li>
              <li>Gives you an opportunity to review talks or conferences you attended.</li>
              <li>Gives you the power to track your speaking engagements.</li>
            </ul>
            <ul>
              <li>Gives you access to conferences you attended.</li>
              <li>Gives you an opportunity to review talks or conferences you attended.</li>
              <li>Gives you the power to track your speaking engagements.</li>
            </ul>
          </div>
          <div className='devfest-info-right'>
            <img className='devfest-uk' src={assets.devfestUk} alt="" />
            <img className='devfest-namibia' src={assets.pyconNamibia} alt="" />
          </div>
        </div>
        <div  className='how-it-works'>
          <h1>See How It <span>Works</span></h1>
          <div className='how-it-works-grid'>
            
          </div>
        </div>
    </div>
  )
}

export default Home