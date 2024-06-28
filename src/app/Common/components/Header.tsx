// src/components/Header.tsx
import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

const Header: React.FC = () => {
  return (
    <Link href='/'>
      <div className=' p-4 text-white text-center flex flex-col items-center gap-4'>
        <Image
          loading='eager'
          src='/votegpt_logo.jpg'
          alt='logo'
          width={350}
          height={350}
        />
        <span className='text-black'>
          Know your candidates, lead the change
        </span>
      </div>
    </Link>
  );
};

export const HeaderSecondary: React.FC = () => {
  return (
    <Link href='/'>
      <div className=' p-4 text-white flex flex-col gap-4'>
        <Image
          loading='eager'
          src='/votegpt_logo.jpg'
          alt='logo'
          width={200}
          height={200}
        />
        <span className='text-black'>
          Know your candidates, lead the change
        </span>
      </div>
    </Link>
  );
};

export default Header;
