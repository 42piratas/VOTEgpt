'use client';
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Link from 'next/link';
import Image from 'next/image';
import CountryType from '../types/CountryType';
import { ElectionLink } from './ElectionsLink';
import { electionsController } from '@/app/controller/getData';
import ModalCountryElections from './ModalCountryElections';
import { common_messages } from '../messages';

export default function CountrySelect() {
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);
  const [electionData, setElectionData] = React.useState([
    { Elections: 'Searching' },
  ]);
  const [countrySelected, setCountrySelected] = React.useState<CountryType>({
    code: '',
    label: '',
  });
  const [countries, setContries] = React.useState<CountryType[]>([
    {
      code: '',
      label: '',
    },
  ]);
  const [isDemocratic, setIsDemocratic] = React.useState<boolean>(false);

  React.useEffect(() => {
    const fetchData = async () => {
      const result = await electionsController.CountriesData();
      console.log(result);
      setContries(result);
    };
    fetchData();
  }, []);

  // request election data
  const handleSubmitData = async (
    newValue: {
      code: string;
      label: string;
    } | null
  ) => {
    try {
      // colocar mensagem de busca
      setElectionData([
        {
          Elections: common_messages.searching,
        },
      ]);
      console.log(newValue?.label);
      const result =
        newValue?.label &&
        (await electionsController.ElectionData(newValue?.label));

      if (result === undefined) {
        setElectionData([
          {
            Elections: common_messages.information_not_found,
          },
        ]);
        return;
      }
      if (!result) {
        setElectionData([
          {
            Elections: 'This country is not democratic',
          },
        ]);
        return;
      }
      setElectionData(result?.elections);
    } catch (error) {
      console.error('Error:', error);
      // setResponse('Failed to get response from ChatGPT');
    }
  };

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

  return (
    <div className='flex flex-col items-center gap-2'>
      <Autocomplete
        onChange={(event, newValue) => {
          setCountrySelected(newValue || { code: '', label: '' });
          handleSubmitData(newValue);
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
              autoComplete: 'new-password',
            }}
          />
        )}
      />
      <div className='flex w-full justify-center gap-4'>
        <Link
          href='https://github.com/42piratas/VOTEgpt/wiki'
          className='text-lg text-[#2592BF] underline hover:text-[#1a749b]'
          target='_blank'
        >
          How it works
        </Link>
        <Link
          href='https://github.com/42piratas/VOTEgpt/issues/new'
          className='text-lg text-[#2592BF] underline hover:text-[#1a749b]'
          target='_blank'
        >
          Feedback/Report
        </Link>
      </div>
      <ModalCountryElections
        open={open}
        handleClose={handleClose}
        countrySelected={countrySelected}
        electionData={electionData}
        isDemocratic={isDemocratic}
      />
    </div>
  );
}
