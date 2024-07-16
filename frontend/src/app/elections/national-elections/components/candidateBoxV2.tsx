/* eslint-disable @next/next/no-img-element */
'use client';

import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import { Bio } from '../../../Common/types/CandidateType';

const CandidateBoxV2: React.FC<{ candidate: Bio }> = ({ candidate }) => {
  return (
    <Link
      className='max-w-64 bg-slate-50 p-5 rounded shadow-xl cursor-pointer border'
      href={`/candidate/${candidate.id}`}
    >
      <Image
        className='object-cover object-top w-full rounded-2xl aspect-[14/13]'
        src={candidate.image}
        alt={candidate.name}
        title={candidate.name}
        width={200}
        height={200}
      />
      <h3 className='text-xl mt-2 tracking-tight font-semibold'>
        {`${candidate.name} (age ${candidate.age})`}
      </h3>
      <p className='text-base text-gray-500'>{candidate.party.current}</p>
      <p className='text-gray-500'>{candidate.keywords.join(', ')}</p>
    </Link>
  );
};

export default CandidateBoxV2;
