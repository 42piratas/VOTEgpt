/* eslint-disable @next/next/no-img-element */
'use client';

import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import { Bio } from '../../../Common/types/CandidateType';

const CandidateBoxV2: React.FC<{ candidate: Bio }> = ({ candidate }) => {
  return (
    <Link href={`/candidate/${candidate.id}`}>
      <div className='group relative cursor-pointer overflow-hidden bg-white px-2 pt-6 pb-4 shadow-2xl ring-1 ring-gray-900/5 transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl sm:mx-auto sm:max-w-sm sm:rounded-lg sm:px-10'>
        <Image
          className='object-cover object-top w-full rounded-2xl aspect-[14/13]'
          src={candidate.image}
          alt={candidate.name}
          title={candidate.name}
          width={200}
          height={200}
        />
        <h3 className='text-lg mt-1 tracking-tight font-semibold'>
          {candidate.name}
        </h3>
        <div className=' text-base leading-7 text-gray-600 transition-all duration-300 '>
          <p className='text-base text-gray-400'>
            {candidate.party.current}
          </p>
          <p className='text-sm text-gray-700'>
            <strong>Platform</strong> {candidate.platform}
          </p>
          <p className='text-sm text-gray-700'>
            <strong>Keywords:</strong> {candidate.keywords.join(', ')}
          </p>
        </div>
        <div className='text-base font-semibold leading-7'>
          <p>
            <a href='#' className='text-sky-500 transition-all duration-300'>
              Read more &rarr;
            </a>
          </p>
        </div>
      </div>
    </Link>
  );
};

export default CandidateBoxV2;
