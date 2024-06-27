// pages/index.tsx
import React from 'react';
import { HeaderSecondary } from '@/app/common/components/Header';
import Footer from '@/app/common/components/Footer';
import Image from 'next/image';
import CandidateBox from './components/candidateBox';
import { CandidateInfo } from '../../common/data/CandidateData';
const NationalElections: React.FC = () => {
  return (
    <div className='flex flex-col min-h-screen'>
      <HeaderSecondary />
      <main className='flex flex-col items-center justify-around min-h-3/6 my-2'>
        <div className='flex flex-col items-center gap-2 my-2'>
          <div className='flex gap-2'>
            <Image
              loading='lazy'
              width={80}
              height={50}
              src={`https://flagcdn.com/w20/ro.png`}
              alt='Romania Flag'
            />
            <h1 className='text-5xl'>Romania</h1>
          </div>
          <span className='text-xl'>National Elections 03 may 2025</span>
        </div>
        <div className='grid lg:grid-cols-2 gap-4 lg:overflow-auto'>
          {CandidateInfo.map((candidate, index) => (
            <CandidateBox key={index} candidate={candidate} />
          ))}
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default NationalElections;
