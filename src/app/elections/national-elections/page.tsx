// pages/index.tsx
import React from 'react';
import Header from '../../components/Header';
import Footer from '../../components/Footer';
import Image from 'next/image';
import CandidateBox from './components/candidateBox';
import { CandidatesPresidentialELections } from './data';

const NationalElections: React.FC = () => {
  return (
    <div className='flex flex-col min-h-screen justify-between'>
      <main className='flex flex-col items-center justify-center'>
        <Header />
        <div className='flex flex-col items-center gap-2 my-2'>
          <div className='flex gap-2'>
            <Image
              loading='lazy'
              width={50}
              height={50}
              src={`https://flagcdn.com/w20/ro.png`}
              alt='Romania Flag'
            />
            <h2 className='text-2xl'>Romania</h2>
          </div>
          <span className='text-sm'>National Elections 03 may 2025</span>
        </div>
        <div>
          {CandidatesPresidentialELections.map((candidate, index) => (
            <CandidateBox key={index} candidate={candidate} />
          ))}
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default NationalElections;
