import Image from 'next/image';

export default function BadgesArea() {
  return (
    <div className='flex gap-2 w-[300px] items-center justify-between p-2'>
      <a href='https://github.com/42piratas/VOTEgpt/blob/main/CONTRIBUTE.md'>
        <Image
          loading='eager'
          className='transition-colors duration-500 ease-in-out transform hover:scale-105'
          src={'/build_badge.jpg'}
          alt='Build Badge'
          width={110}
          height={100}
        />
      </a>
      <a href='https://github.com/42piratas/VOTEgpt/blob/main/LICENSE.txt'>
        <Image
          loading='eager'
          className='transition-colors duration-500 ease-in-out transform hover:scale-105'
          src={'/copyleft_badge.jpg'}
          alt='Copyleft Badge'
          width={120}
          height={100}
        />
      </a>
      <a href='#'>
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
