/* eslint-disable @next/next/no-img-element */
'use client';

import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import { Bio } from '../../../Common/types/CandidateType';

const CandidateBox: React.FC<{ candidate: Bio }> = ({ candidate }) => {
  return (
    <figure className='rounded-xl border-2 m-2 flex flex-col items-center md:flex md:flex-row md:p-0'>
      <img
        src={candidate.image}
        alt={candidate.name}
        className='rounded-[.5rem] my-2 md:my-0 object-contain md:object-cover w-40 h-40 md:w-48 md:h-full md:rounded-[.5rem_0_0_.5rem]'
      />
      <div className='pt-6 md:p-8 text-center md:text-left'>
        <blockquote>
          <p className='text-lg font-bold'>
            {`${candidate.name} (age ${candidate.age})`}
          </p>
        </blockquote>
        <figcaption className='font-medium'>
          <div>
            <span className='text-sm'>
              <strong>Born:</strong>
              {candidate.birth.year}, {candidate.birth.place}
            </span>
          </div>
          <div>
            <span className='text-sm'>
              <strong>Current Party:</strong> {candidate.party.current}
            </span>
          </div>
          <div>
            <span className='text-sm'>
              <strong>Keywords:</strong> {candidate.keywords.join(', ')}
            </span>
          </div>
          <div>
            <span title={candidate.notoriousFor.join(', ')} className='text-sm'>
              <strong>Nothorious For:</strong>{' '}
              {candidate.notoriousFor.join(', ')}
            </span>
          </div>
          <div className='w-full flex justify-center md:justify-end'>
            <Link
              href={`/candidate/${candidate.id}`}
              className='text-blue-500 underline md:text-end'
            >
              Read More
            </Link>
          </div>
        </figcaption>
      </div>
    </figure>
  );
};

export default CandidateBox;
