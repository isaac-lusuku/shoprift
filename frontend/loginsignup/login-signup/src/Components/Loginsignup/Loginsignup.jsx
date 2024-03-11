import React from 'react';
import './Loginsignup.css';
import user_icon from '../Assets/person-icon.png';
import email_icon from '../Assets/email-icon.png';
import password_icon from '../Assets/password-icon.png';

export const Loginsignup = () => {
  return (
    <div className='container'>
    <div className='header'>
      <div className='text'>Sign Up</div>
      <div className='underline'></div>
    </div>
    <div className='inputs'>
      <div className='input'>
        <img src={user_icon} alt=""/>
        <input type='text'/>
      </div>
      <div className='input'>
        <img src={email_icon} alt=""/>
        <input type='email'/>
      </div>
      <div className='input'>
        <img src={password_icon} alt=""/>
        <input type='password'/>
      </div>
    </div>
    <div className='forgot-password'>Lost password?  <span>Click here</span></div>
    <div className='submit-container'>
      <div className='submit'>Sign Up</div>
      <div className='submit'>Login</div>
    </div>
  </div>
);
}
  
