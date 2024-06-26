'use client';

import { Candidate } from '@/app/Common/types';
import Image from 'next/image';
import React from 'react';

const CandidateBox: React.FC<{ candidate: Candidate }> = ({ candidate }) => {
  return (
    <div className='max-w-2xl border rounded-lg shadow-md flex justify-between'>
      <Image
        style={{
          borderRadius: '.5rem 0 0 .5rem',
        }}
        src={candidate.image}
        alt={candidate.name}
        width={250}
        height={200}
        className='mx-auto'
        objectFit='cover'
        objectPosition='center'
      />
      <div className='flex flex-col justify-between px-2 py-5 gap-2'>
        <h3 className='text-2xl'>{`${candidate.name} (age ${candidate.age})`}</h3>
        <p>
          <strong>Current Party:</strong> {candidate.partyCurrent}
        </p>
        <p>
          <strong>Keywords:</strong> {candidate.keyworkds}
        </p>
        <span title={candidate.bio}>
          <strong>Bio:</strong> {candidate.bio}
        </span>
        <span title={candidate.nothoriousFor}>
          <strong>Nothorious For:</strong> {candidate.nothoriousFor}
        </span>
      </div>
    </div>
  );
};

export default CandidateBox;
