import Image from 'next/image';

function Button({ children }: { children: React.ReactNode }) {
  return (
    <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded '>
      {children}
    </button>
  );
}

export default function BadgesArea() {
  return (
    <div className='flex gap-2 items-center justify-between p-2'>
      <a href='#'>
        <Button>DONATE</Button>
      </a>
      <a
        href='https://github.com/42piratas/VOTEgpt/blob/main/CONTRIBUTE.md'
        target='_blank'
      >
        <Button>BUIDL</Button>
      </a>
      <a
        href='https://github.com/42piratas/VOTEgpt/blob/main/LICENSE.md'
        target='_blank'
      >
        <Button>GPL-3.0</Button>
      </a>
    </div>
  );
}
