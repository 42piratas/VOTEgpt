// src/components/Footer.tsx
import React from 'react';
import BadgesArea from './Badges';

const Footer: React.FC = () => {
  return (
    <footer className='flex flex-col items-center gap-2 w-full bg-white bottom-0'>
      <BadgesArea />
      <div className='flex flex-col gap-2 w-full items-center border-t p-4'>
        <p className='gap-5'>
          ❤️ Made possible by{' '}
          <a href='https://www.akasha.org/' target='_blank' rel='noreferrer'>
            @AKASHA{' '}
          </a>
          <a href='https://www.mozilla.org/' target='_blank' rel='noreferrer'>
            @Mozilla{' '}
          </a>
          <a href='https://ethereum.org/' target='_blank' rel='noreferrer'>
            @Ethereum
          </a>
        </p>
      </div>
    </footer>
  );
};

export default Footer;
