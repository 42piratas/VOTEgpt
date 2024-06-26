import Image from 'next/image';

export default function BadgesArea() {
  return (
    <div className='flex gap-2 w-[300px] justify-between'>
      <a
        href='https://github.com/42piratas/VOTEgpt'
        target='_blank'
        rel='noreferrer'
      >
        <Image
          loading='eager'
          className='transition-colors duration-500 ease-in-out transform hover:scale-105'
          src={'/build_badge.jpg'}
          alt='Build Badge'
          width={100}
          height={100}
        />
      </a>
      <a
        href='https://github.com/42piratas/VOTEgpt'
        target='_blank'
        rel='noreferrer'
      >
        <Image
          loading='eager'
          className='transition-colors duration-500 ease-in-out transform hover:scale-105'
          src={'/donate_badge.jpg'}
          alt='Build Badge'
          width={100}
          height={100}
        />
      </a>
    </div>
  );
}
