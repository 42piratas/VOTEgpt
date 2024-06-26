'use client';

import { Candidate } from '@/app/Common/types';
import { Box, Modal } from '@mui/material';
import Image from 'next/image';
import React, { useState } from 'react';
import style from 'styled-jsx/style';

const CandidateInformationModal: React.FC<{ candidate: Candidate }> = ({
  candidate,
}) => {
  const [open, setOpen] = useState(false);
  const handleClose = () => setOpen(false);
  return (
    <div className='max-w-xl border rounded-lg shadow-md flex justify-between'>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby='modal-modal-title'
        aria-describedby='modal-modal-description'
      >
        <Box sx={style}>
          <Image
            src={candidate.image}
            alt={candidate.name}
            width={200}
            height={200}
            className='mx-auto'
            objectFit='contain'
            objectPosition='center'
          />
          <div className='flex flex-col justify-between px-2 py-4 '>
            <h3 className='text-2xl'>{candidate.name}</h3>
            <p>Party: {candidate.party}</p>
            <span title={candidate.description}>
              {candidate.description.length > 300
                ? candidate.description.slice(0, 100) + '...'
                : candidate.description}
            </span>
          </div>
        </Box>
      </Modal>
    </div>
  );
};

const CandidateBox: React.FC<{ candidate: Candidate }> = ({ candidate }) => {
  const [open, setOpen] = useState(false);

  return (
    <>
      <div className='max-w-xl border rounded-lg shadow-md flex justify-between'>
        <Image
          src={candidate.image}
          alt={candidate.name}
          width={200}
          height={200}
          className='mx-auto'
          objectFit='contain'
          objectPosition='center'
        />
        <div className='flex flex-col justify-between px-2 py-4 '>
          <h3 className='text-2xl'>{candidate.name}</h3>
          <p>Party: {candidate.party}</p>
          <span title={candidate.description}>
            {candidate.description.length > 300
              ? candidate.description.slice(0, 100) + '...'
              : candidate.description}
          </span>
          <button
            onClick={() => setOpen(true)}
            className='w-fit bg-[#238FB8] text-white p-2 rounded-lg self-end m-4'
          >
            More
          </button>
        </div>
      </div>
      {open && <CandidateInformationModal candidate={candidate} />}
    </>
  );
};

export default CandidateBox;
