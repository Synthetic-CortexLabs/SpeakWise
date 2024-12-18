import React, { useState } from 'react';
import './Login.css';
import { assets } from '../../../assets/assets';

const Login = () => {
  const [view, setView] = useState('buttons');
  const [showPassword, setShowPassword] = useState(false);
  const [animate, setAnimate] = useState(true);
 

  // This section is responsible for handling the state of the login view and password visibility
  // The animate state is used to control the animation of the view transition
  // The showPassword state is used to toggle the visibility of the password input field
  const handleViewChange = (newView) => {
    setAnimate(false);
    setTimeout(() => {
      setView(newView);
      setAnimate(true);
    }, 10);
  };

  return (
    <div className='login-container'>
      <div className={`login-left ${animate ? 'animate' : ''}`}>
        <h1>
          Speak<span>Wise</span>
        </h1>
        {view === 'buttons' && (
          <>
            <img src={assets.blackImage} alt='' />
            <h2>You need to track your Speaking engagements?</h2>
            <p>
              Whichever tech conference you attended recently, you can find your
              favorite speaking sessions and leave reviews and feedback.
            </p>
          </>
        )}
        {(view === 'signin' || view === 'signup') && (
          <>
            {view === 'signin' && <img src={assets.googleIo} alt="" />}
            {view === 'signup' && <img src={assets.speakwise} alt="" />}
            <h2>Review talks from <span>conferences</span> you attended</h2>
            <p>
              Whichever tech conference you attended recently, you can find your
              favorite speaking sessions and leave reviews and feedback.
            </p>
          </>
        )}
      </div>
      <div className='login-right'>
        {view === 'buttons' && (
          <div className='sign-in-options'>
            <h1>
              Speak<span>Wise</span>
            </h1>
            <p>Select User Type</p>
            <button onClick={() => handleViewChange('signin')}>Sign in as Attendee</button>
            <button onClick={() => handleViewChange('signin')}>Sign in as Speaker</button>
            <button onClick={() => handleViewChange('signin')}>Sign in as Organizer</button>
            <p>
              Don&apos;t have an account?{' '}
              <span onClick={() => handleViewChange('signup')}>Sign up</span>
            </p>
          </div>
        )}
        {view === 'signin' && (
          <div className='sign-in-form'>
            <h1>Welcome back!</h1>
             <p>
              Don&apos;t have an account?{' '}
              <span onClick={() => handleViewChange('signup')}>Sign up</span>
            </p>
            <form>
              <div>
                <label>Email Address</label>
                <input type='email'  />
              </div>
              <div>
                <label>Password</label>
                <input type={showPassword ? 'text' : 'password'} />
                {showPassword ? (
                  <img src={assets.eyeOpen} alt="" onClick={() => setShowPassword(false)} />
                ) : (
                  <img src={assets.eyeClosed} alt="" onClick={() => setShowPassword(true)} />
                )}
              </div>
              <button type='submit'>Sign In</button>
            </form>
            <p>Forgot Password? <span>Recover</span></p>
           
          </div>
        )}
        {view === 'signup' && (
          <div className='sign-up-form'>
            <h1>Create account</h1>
             <p>
              Already have an account?{' '}
              <span onClick={() => handleViewChange('signin')}>Sign In</span>
            </p>
            <form>
              <label>Your Name</label>
              <input type='text' />
              <label>Your Nationality</label>
              <input type='text'  />
              <label>Email Address</label>
              <input type='email' />
              <label>Password</label>
              <input type='password' />
              <button type='submit'>Create Account</button>
            </form>
           
          </div>
        )}
        {(view === 'buttons') && (
        <div className='connect'>
          <p>Connect with us</p>
          <div className='socials'>
            <img src={assets.linkedinBlack} alt='' />
            <img src={assets.twitterBlack} alt='' />
          </div>
        </div>
        )}
      </div>
    </div>
  );
};

export default Login;
