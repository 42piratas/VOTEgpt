// src/components/Header.tsx
import React from 'react';

const Header: React.FC = () => {
  return (
    <header className='bg-gray-800 p-4 text-white text-center'>
      <h1 className='text-2xl'>VOTEGPT</h1>
      <span className='text-sm'>KNOW YOUR CANDIDATES, LEAD THE CHANGE</span>
    </header>
  );
};

export default Header;
