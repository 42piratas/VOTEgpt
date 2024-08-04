// src/components/Footer.tsx
import React from 'react';
import BadgesArea from '../components/Badges';

const Footer: React.FC = () => {
  return (
    <footer className='flex flex-col items-center gap-2 w-full bg-white bottom-0'>
      <BadgesArea />
    </footer>
  );
};

export default Footer;
