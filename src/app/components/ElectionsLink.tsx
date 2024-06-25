import { Typography } from '@mui/material';
import Link from 'next/link';

export const ElectionLink = ({
  href,
  description,
}: {
  href: string;
  description: string;
}) => (
  <Link href={href}>
    <Typography id='modal-modal-description' className='p-4 border border-black rounded'>
      {description}
    </Typography>
  </Link>
);
