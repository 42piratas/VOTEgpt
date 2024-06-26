// src/components/Header.tsx
import React from 'react';
import Image from 'next/image';

const Header: React.FC = () => {
  return (
    <header className=' p-4 text-white text-center flex flex-col items-center gap-4'>
      <Image loading='eager' src='/votegpt_logo.jpg' alt='logo' width={200} height={200} />
      <span className='text-black border-b-2'>
        Know your candidates, lead the change
      </span>
    </header>
  );
};

export default Header;
