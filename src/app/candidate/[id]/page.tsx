import Footer from '@/app/common/components/Footer';
import { HeaderSecondary } from '@/app/common/components/Header';
import { CandidateInfo } from '@/app/common/data/CandidateData';
import Image from 'next/image';

export default function CandidatePage({ params }: { params: { id: string } }) {
  return (
    <>
      <HeaderSecondary />
      <div className='max-w-4xl mx-auto p-4 mb-28'>
        <div className='flex items-center space-x-4 mb-4'>
          <Image
            width={200}
            height={200}
            src={CandidateInfo[0].image}
            alt={CandidateInfo[0].name}
            className='object-contain rounded'
          />
          <div>
            <h1 className='text-3xl font-bold'>{CandidateInfo[0].name}</h1>
            <p className='text-gray-600'>{`Born: ${CandidateInfo[0].birth.year}, ${CandidateInfo[0].birth.place}`}</p>
            <p className='text-gray-600'>{`Age: ${CandidateInfo[0].age}`}</p>
            <p className='text-gray-600'>{`Education: ${CandidateInfo[0].education}`}</p>
          </div>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Biography</h2>
          <p className='text-gray-700 mt-2'>{CandidateInfo[0].bio}</p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Current Party</h2>
          <p className='text-gray-700 mt-2'>{CandidateInfo[0].party.current}</p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Previous Party</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].party.previous}
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>
            Previous Political Experience
          </h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].previousPoliticalExperience}
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Keywords</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].keywords.join(', ')}
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Notorious For</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].notoriousFor.join(', ')}
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Platform</h2>
          <p className='text-gray-700 mt-2'>{CandidateInfo[0].platform}</p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Endorsements</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].endorsements.join(', ')}
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Funding Sources</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].fundingSources.join(', ')}
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Criminal Records</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[0].criminalRecords.join(', ')}
          </p>
        </div>
        <div className='flex flex-col mb-4'>
          <h2 className='text-2xl font-semibold'>Policies</h2>
          <p>
            <strong>Abortion:</strong> {CandidateInfo[0].policies.abortion}
          </p>
          <p>
            <strong>Health Care:</strong> {CandidateInfo[0].policies.healthcare}
          </p>
          <p>
            <strong>Economy:</strong> {CandidateInfo[0].policies.economy}
          </p>
          <p>
            <strong>Immigration:</strong>{' '}
            {CandidateInfo[0].policies.immigration}
          </p>
          <p>
            <strong>Gun Control:</strong> {CandidateInfo[0].policies.gunControl}
          </p>
          <p>
            <strong>Climate Change:</strong>{' '}
            {CandidateInfo[0].policies.climateChange}
          </p>
          <p>
            <strong>Education:</strong> {CandidateInfo[0].policies.education}
          </p>
          <p>
            <strong>Taxes:</strong> {CandidateInfo[0].policies.taxes}
          </p>
          <p>
            <strong>LGBTQ Rights:</strong>{' '}
            {CandidateInfo[0].policies.lgbtqRights}
          </p>
          <p>
            <strong>Foreign Policy:</strong>{' '}
            {CandidateInfo[0].policies.foreignPolicy}
          </p>
          <p>
            <strong>Drug Policy:</strong> {CandidateInfo[0].policies.drugPolicy}
          </p>
          <p>
            <strong>Criminal Justice Reform:</strong>{' '}
            {CandidateInfo[0].policies.criminalJusticeReform}
          </p>
          <p>
            <strong>Military Spending:</strong>{' '}
            {CandidateInfo[0].policies.militarySpending}
          </p>
          <p>
            <strong>Voting Rights:</strong>{' '}
            {CandidateInfo[0].policies.votingRights}
          </p>
        </div>
        <div className='flex flex-col mb-4'>
          <h2 className='text-2xl font-semibold'>Links</h2>
          <a
            className='text-[#0073e6] underline hover:text-[#0056b3]'
            href={CandidateInfo[0].online.wikipedia}
            target='_blank'
            rel='noreferrer'
          >
            Wikipedia
          </a>
          <a
            className='text-[#0073e6] underline hover:text-[#0056b3]'
            href={CandidateInfo[0].online.officialWebsite}
            target='_blank'
            rel='noreferrer'
          >
            Official Website
          </a>
          <a
            className='text-[#0073e6] underline hover:text-[#0056b3]'
            href={CandidateInfo[0].online.truthSocial}
            target='_blank'
            rel='noreferrer'
          >
            Social
          </a>
        </div>
      </div>
      <Footer />
    </>
  );
}
