// pages/index.tsx
import React from 'react';
import Image from 'next/image';
import CandidateBox from './components/candidateBox';
import { CandidateInfo } from '../../../common/data/CandidateData';
import { HeaderSecondary } from '../../../common/components/Header';
import Footer from '../../../common/components/Footer';
const NationalElections: React.FC = () => {
  return (
    <div className='flex flex-col min-h-screen justify-normal'>
      <HeaderSecondary />
      <main className='flex flex-col items-center top-0 min-h-[74vh]'>
        <div className='flex flex-col items-center gap-2 my-2'>
          <div className='flex gap-2'>
            <Image
              loading='lazy'
              width={80}
              height={50}
              src='https://flagcdn.com/w1280/ro.png'
              alt='Romania Flag'
              title='Romania Flag'
            />
            <h1 className='text-5xl'>Romania</h1>
          </div>
          <span className='text-xl'>National Elections 03 may 2025</span>
        </div>
        <div className='grid gap-4 mb-16 lg:grid-cols-2 lg:overflow-auto'>
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
