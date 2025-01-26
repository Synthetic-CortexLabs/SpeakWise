import React, { useState } from 'react';
import './Home.css';
import Header from '../../components/Header/Header';
import { assets } from '../../assets/assets';
import Footer from '../../components/Footer/Footer';
import Navbar from '../../components/Navbar/Navbar';

const Home = () => {
  const [activeImage, setActiveImage] = useState(0);
  const images = [assets.devfestUkMobile, assets.pyconNamibiaMobile];

  const nextImage = () => {
    setActiveImage((prev) => (prev + 1) % images.length);
  };

  const prevImage = () => {
    setActiveImage((prev) => (prev - 1 + images.length) % images.length);
  };

  // Images for the sliding track
  const sliderImages = [
    { src: assets.pyconAfrica, alt: 'PyCon Africa', className: 'pycon' },
    { src: assets.googleIoExtended1, alt: 'Google IO Extended' },
    { src: assets.devfest, alt: 'DevFest' },
    { src: assets.flutter1, alt: 'Flutter' },
  ];

  // Duplicate images to create the seamless effect
  const repeatedSliderImages = Array(5) // Change `5` to any number of times you want to repeat
  .fill(sliderImages)
  .flat();


  return (
    <div>
      <Navbar />
      <Header />
      <div className="frameworks-container">
        <div className="slide-track">
          {repeatedSliderImages.map((image, index) => (
            <div
              className={`slide ${image.className || ''}`}
              key={`${image.alt}-${index}`}
            >
              <img src={image.src} alt={image.alt} />
            </div>
          ))}
        </div>
      </div>
      <div className="devfest-info">
        <div className="devfest-info-left">
          <h1>
            Speak-<span>Wise</span>
          </h1>
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
        <div className="devfest-info-right">
          <img className="devfest-uk" src={assets.devfestUk} alt="" />
          <img className="devfest-namibia" src={assets.pyconNamibia} alt="" />
        </div>
        <div className="devfest-info-right-mobile">
          {images.map((img, index) => (
            <img
              key={index}
              src={img}
              alt=""
              className={index === activeImage ? 'active' : ''}
            />
          ))}
          <div className="carousel-controls">
            <img src={assets.chevronLeft} alt="Previous" onClick={prevImage} />
            <img src={assets.chevronRight} alt="Next" onClick={nextImage} />
          </div>
        </div>
      </div>
      <div className="how-it-works">
        <div className="how-it-works-top">
          <h1>
            See How It <span>Works</span>
          </h1>
          <p>
            How was your conference experience? Share your thoughts and help
            shape the future of speaking with Speak<span>Wise</span>.
          </p>
        </div>
        <div className="how-it-works-grid">
          <div className="how-it-works-grid-item">
            <img src={assets.EarthGlobe} alt="" />
            <b>Select a Country</b>
            <p>
              After you log on to Speak<span>Wise</span>, you go ahead to select
              the country in which the conference was hosted.
            </p>
          </div>
          <div className="how-it-works-grid-item">
            <img src={assets.Region} alt="" />
            <b>Select a Region</b>
            <p>
              In the selected country, you can now select the Region where the
              conference was held
            </p>
          </div>
          <div className="how-it-works-grid-item">
            <img src={assets.Conference} alt="" />
            <b>Select the Conference/Event</b>
            <p>
              Now you can go ahead and select the conference you attended, all
              conferences attended will be available here
            </p>
          </div>
          <div className="how-it-works-grid-item">
            <img src={assets.Calender} alt="" />
            <b>Choose the Day</b>
            <p>
              Normally, some conferences are hosted over several days, in which
              you select the day you attended.
            </p>
          </div>
          <div className="how-it-works-grid-item">
            <img src={assets.Training} alt="" />
            <b>Select the Speaker</b>
            <p>
              Now go ahead and select the speaker you want to rate or give a
              review.
            </p>
          </div>
          <div className="how-it-works-grid-item">
            <img src={assets.Thumbs} alt="" />
            <b>Give Speaker Feedback</b>
            <p>
              Go ahead and rate and give a speaker feedback, note your feedback
              is anonymous.
            </p>
          </div>
        </div>
      </div>
      <div className="home-contact-container">
        <div className="home-contact-container-top">
          <div className="home-contact-container-left">
            <h1>
              <span>Got Any Questions?</span>
            </h1>
            <h1>We&apos;ve Got Answers</h1>
          </div>
          <div className="home-contact-container-right">
            <input type="email" placeholder="Email" />
            <button>Connect</button>
          </div>
        </div>
        <div className="home-contact-container-bottom">
          <div className="home-contact-us">
            <p>Ready to get started?</p>
            <button>CONTACT US</button>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Home;
