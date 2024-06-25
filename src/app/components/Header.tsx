// src/components/Header.tsx
import React from 'react';
import Image from 'next/image';

const Header: React.FC = () => {
  return (
    <header className=' p-4 text-white text-center flex flex-col items-center my-5'>
      <Image src='/votegpt_logo.jpg' alt='logo' width={200} height={200} />
      <span className='text-black'>
        Know your candidates, lead the change
      </span>
    </header>
  );
};

export default Header;
