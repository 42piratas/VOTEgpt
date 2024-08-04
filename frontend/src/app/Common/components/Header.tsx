// src/components/Header.tsx
import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

interface HeaderSecondaryProps {
  position: 'center' | 'left' | 'right'; // Define appropriate positions
}

const Header: React.FC = () => {
  return (
    <div className='text-white text-center flex flex-col items-center gap-4'>
      <Image
        loading='eager'
        src='/vote-gpt-logo.png'
        alt='logo'
        width={350}
        height={350}
      />
    </div>
  );
};

export const HeaderSecondary: React.FC<HeaderSecondaryProps> = ({
  position,
}) => {
  return (
    <Link href='/'>
      <div
        className={`p-4 text-white flex flex-col ${
          position === 'center' ? 'items-center' : ''
        } gap-4`}
      >
        <Image
          loading='eager'
          src='/vote-gpt-logo.png'
          alt='logo'
          width={200}
          height={200}
        />
      </div>
    </Link>
  );
};

export default Header;
