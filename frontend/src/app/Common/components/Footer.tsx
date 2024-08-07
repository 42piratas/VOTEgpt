// src/components/Footer.tsx
import React from 'react';
import BadgesArea from '../components/Badges';

const Footer: React.FC = () => {
  return (
    <footer className='flex flex-col items-center gap-2 w-full bg-white bottom-0'>
      <BadgesArea />
      {/* <div className='flex flex-col gap-2 w-full items-center border-t p-4'>
        <p className='gap-5'>
          ❤️ Made possible by{' '}
          <a href='https://www.akasha.org/' className='text-[#2592BF] underline hover:text-[#1a749b]' target='_blank' rel='noreferrer'>
            @AKASHA{' '}
          </a>
        </p>
      </div> */}
    </footer>
  );
};

export default Footer;
