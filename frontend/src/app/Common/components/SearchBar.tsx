'use client';
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Modal, Typography } from '@mui/material';
import Link from 'next/link';
import Image from 'next/image';
import CountryType from '../types/CountryType';
import { countries } from '../data/Countries';
import { ElectionLink } from './ElectionsLink';

export default function CountrySelect() {
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);

  const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

  const [countrySelected, setCountrySelected] =
    React.useState<CountryType | null>(null);

  return (
    <div className='flex flex-col items-center gap-2'>
      <Autocomplete
        onChange={(event, newValue) => {
          setCountrySelected(newValue);
          setOpen(true);
        }}
        id='country-select-demo'
        sx={{ width: 300 }}
        options={countries}
        autoHighlight
        getOptionLabel={(option) => option.label}
        renderOption={(props, option) => (
          <Box
            component='li'
            sx={{ '& > img': { mr: 2, flexShrink: 0 } }}
            {...props}
          >
            <Image
              loading='lazy'
              width={20}
              height={20}
              src={`https://flagcdn.com/w40/${option.code.toLowerCase()}.png`}
              alt={option.label}
              title={option.label}
            />
            {option.label}
          </Box>
        )}
        renderInput={(params) => (
          <TextField
            {...params}
            label='Choose a country'
            inputProps={{
              ...params.inputProps,
              autoComplete: 'new-password', // disable autocomplete and autofill
            }}
          />
        )}
      />
      <Link
        href='https://github.com/42piratas/VOTEgpt/wiki'
        className='text-lg text-[#2592BF] underline hover:text-[#1a749b]'
        target='_blank'
      >
        Learn how it works
      </Link>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby='modal-modal-title'
        aria-describedby='modal-modal-description'
      >
        <Box sx={style}>
          {countrySelected?.label != 'Romania' ? (
            <Typography id='modal-modal-title' variant='h6' component='h2'>
              Sorry ! We&apos;re not aware of any elections in{' '}
              {countrySelected?.label}
            </Typography>
          ) : (
            <>
              <div className='flex items-center gap-5 w-full '>
                <Image
                  loading='lazy'
                  width='50'
                  height='50'
                  src={`https://flagcdn.com/w40/${countrySelected?.code.toLowerCase()}.png`}
                  alt={countrySelected.label}
                  title={countrySelected.label}
                />
                <Typography id='modal-modal-title' variant='h6' component='h2'>
                  {countrySelected?.label}
                </Typography>
              </div>
              <Box sx={{ mt: 2 }} gap={2} display='flex' flexDirection='column'>
                <ElectionLink
                  href='/elections/national-elections'
                  description='National elections - 3 May 2025'
                />
                <ElectionLink
                  href='/elections/regional-elections'
                  description='Regional elections - 22 May 2025'
                />
              </Box>
            </>
          )}
        </Box>
      </Modal>
    </div>
  );
}
