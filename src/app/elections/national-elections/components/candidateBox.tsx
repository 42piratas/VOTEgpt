'use client';

import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import { Bio } from '../../../Common/types/CandidateType';

// const CandidateBox: React.FC<{ candidate: Bio }> = ({ candidate }) => {
//   return (
//     <div className='flex justify-between max-w-xl rounded-lg border shadow-[5px_5px_20px_-4px_#4b4a4a34]'>
//       <Image
//         style={{
//           borderRadius: '.5rem 0 0 .5rem',
//         }}
//         src={candidate.image}
//         alt={candidate.name}
//         width={120}
//         height={120}
//         className='object-cover'
//       />
//       <div className='flex flex-col justify-between pl-4 px-2 py-2 gap-1'>
//         <span className='text-xl font-bold'>{`${candidate.name} (age ${candidate.age})`}</span>
//         <span>
//           <strong>Born:</strong>
//           {candidate.birth.year}, {candidate.birth.place}
//         </span>
//         <p className='text-sm'>
//           <strong>Current Party:</strong> {candidate.party.current}
//         </p>

//         <p className='text-sm'>
//           <strong>Keywords:</strong> {candidate.keywords.join(', ')}
//         </p>
//         <span title={candidate.notoriousFor.join(', ')} className='text-sm'>
//           <strong>Nothorious For:</strong> {candidate.notoriousFor.join(', ')}
//         </span>
//         <Link
//           href={`/candidate/${candidate.id}`}
//           className='text-blue-500 underline text-end'
//         >
//           Read More
//         </Link>
//       </div>
//     </div>
//   );
// };

const CandidateBox: React.FC<{ candidate: Bio }> = ({ candidate }) => {
  return (
    <figure className='rounded-xl p-8 shadow-lg flex flex-col items-center md:flex md:flex-row md:p-0'>
      <Image
        src={candidate.image}
        alt={candidate.name}
        width={150}
        height={150}
        className='object-cover rounded-[.5rem] md:rounded-[.5rem_0_0_.5rem]'
      />
      <div className='pt-6 md:p-8 text-center md:text-left space-y-4'>
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
