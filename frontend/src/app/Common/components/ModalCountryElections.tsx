import React from 'react';
import { Box, Modal, Typography } from '@mui/material';
import Image from 'next/image';
import CountryType from '../types/CountryType';
import { common_messages } from '../messages';

interface IProps {
  open: boolean;
  handleClose: () => void;
  countrySelected: CountryType;
  electionData: any[];
  isDemocratic: boolean;
}

const ModalCountryElections: React.FC<IProps> = ({
  open,
  handleClose,
  countrySelected,
  electionData,
  isDemocratic,
}) => {
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
    <Modal
      open={open}
      onClose={handleClose}
      aria-labelledby='modal-modal-title'
      aria-describedby='modal-modal-description'
    >
      <Box sx={style}>
        {countrySelected.label && (
          <>
            <div className='flex w-full gap-5'>
                <Image
                  loading='lazy'
                  width='50'
                  height='50'
                  src={`https://flagcdn.com/w40/${countrySelected.code.toLowerCase()}.png`}
                  alt={countrySelected.label}
                  title={countrySelected.label}
                />
                <Typography id='modal-modal-title' variant='h6' component='h2'>
                  {countrySelected.label}
                </Typography>
              </div>
            <Box sx={{ mt: 2 }} gap={2} display='flex' flexDirection='column'>
              {/* <ElectionLink
                  href='/elections/national-elections'
                  description='National elections - 3 May 2025'
                />
                <ElectionLink
                  href='/elections/regional-elections'
                  description='Regional elections - 22 May 2025'
                /> */}
              <div>
                <span>
                  {electionData[0] ? (
                    <div>
                      <h3>
                        {Object.entries(electionData[0]).map(
                          ([key, value], index) => {
                            return (
                              <div key={index}>
                                <h3>
                                  {key}: {value?.toString()}
                                </h3>
                              </div>
                            );
                          }
                        )}
                      </h3>
                    </div>
                  ) : (
                    common_messages.not_found
                  )}
                </span>
              </div>
            </Box>
          </>
        )}
      </Box>
    </Modal>
  );
};

export default ModalCountryElections;
