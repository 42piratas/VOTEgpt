'use client';

import { Bio, Candidate } from '@/app/common/types/CandidateType';
import Image from 'next/image';
import Link from 'next/link';
import React from 'react';

const CandidateBox: React.FC<{ candidate: Bio }> = ({ candidate }) => {
  return (
    <div className='flex justify-between max-w-xl rounded-lg border shadow-[5px_5px_20px_-4px_#4b4a4a34]'>
      <Image
        style={{
          borderRadius: '.5rem 0 0 .5rem',
        }}
        src={candidate.image}
        alt={candidate.name}
        width={150}
        height={150}
        className='object-cover'
      />
      <div className='flex flex-col justify-between pl-4 px-2 py-2 gap-1'>
        <span className='text-xl font-bold'>{`${candidate.name} (age ${candidate.age})`}</span>
        <span>
          <strong>Born:</strong>
          {candidate.birth.year}, {candidate.birth.place}
        </span>
        <p>
          <strong>Current Party:</strong> {candidate.party.current}
        </p>
        <p>
          <strong>Keywords:</strong> {candidate.keywords.join(', ')}
        </p>
        <span title={candidate.bio}>
          <strong>Bio:</strong> {candidate.bio}
        </span>
        <span title={candidate.notoriousFor.join(', ')}>
          <strong>Nothorious For:</strong> {candidate.notoriousFor.join(', ')}
        </span>
        <Link
          href={`/candidate/${candidate.id}`}
          className='text-blue-500 underline text-end'
        >
          Read More
        </Link>
      </div>
    </div>
  );
};

export default CandidateBox;
