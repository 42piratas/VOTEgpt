// src/components/Footer.tsx
import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className='flex flex-col items-center'>
      <div className='flex gap-5 p-5'>
        <button className='border rounded-xl border-black p-3 hover:bg-black hover:text-white transition-colors duration-300 ease-in-out transform hover:scale-105'>
          <p className='text-sm'>Contribute</p>
        </button>

        <button className='border rounded-xl border-black p-3 hover:bg-black hover:text-white transition-colors duration-300 ease-in-out transform hover:scale-105'>
          <p className='text-sm'>Donate</p>
        </button>

        <button className='border rounded-xl border-black p-3 hover:bg-black hover:text-white transition-colors duration-300 ease-in-out transform hover:scale-105'>
          <p className='text-sm'>AI for good</p>
        </button>
      </div>
      <div className='flex gap-5 w-full justify-center border-t p-5'>
        <p className='gap-5'>Powered for AKASHA</p>
        <img
          src='https://cdn.homerun.co/50179/akasha-logo1598445024logo.png'
          alt='AKASHA Foundation'
          className='h-5 w-5 inline'
        />
      </div>
    </footer>
  );
};

export default Footer;
