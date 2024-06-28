import Image from 'next/image';
import { HeaderSecondary } from '../../Common/components/Header';
import { CandidateInfo } from '../../Common/data/CandidateData';
import Footer from '../../Common/components/Footer';
import Link from 'next/link';

export default function CandidatePage({ params }: { params: { id: string } }) {
  const realId = parseInt(params.id) - 1;
  return (
    <div className='flex flex-col min-h-screen justify-normal'>
      <HeaderSecondary />
      <div className='max-w-4xl mx-auto p-4 mb-28'>
        <div className='flex items-center space-x-4 mb-4'>
          <Image
            width={200}
            height={200}
            src={CandidateInfo[realId].image}
            alt={CandidateInfo[realId].name}
            className='object-contain rounded'
          />
          <div>
            <h1 className='text-5xl font-bold'>{CandidateInfo[realId].name}</h1>
            <p className='text-gray-600'>
              <strong>Born:</strong>{' '}
              {`${CandidateInfo[realId].birth.year}, ${CandidateInfo[realId].birth.place}`}{' '}
            </p>
            <p className='text-gray-600'>
              <strong>Age:</strong> {`${CandidateInfo[realId].age}`}
            </p>
            <p className='text-gray-600'>
              <strong>Education:</strong> {`${CandidateInfo[realId].education}`}{' '}
              <Link
                href='#'
                className='text-[#2592BF] underline hover:text-[#1a749b]'
              >
                [*]
              </Link>
            </p>
          </div>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Biography</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].bio}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Current Party</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].party.current}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Previous Party</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].party.previous}{' '}
            <Link href='#' className='link'>
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>
            Previous Political Experience
          </h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].previousPoliticalExperience}[*]
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Keywords</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].keywords.join(', ')}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Notorious For</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].notoriousFor.join(', ')}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Platform</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].platform}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Endorsements</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].endorsements.join(', ')}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Funding Sources</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].fundingSources.join(', ')}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='mb-4'>
          <h2 className='text-2xl font-semibold'>Criminal Records</h2>
          <p className='text-gray-700 mt-2'>
            {CandidateInfo[realId].criminalRecords.join(', ')}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='flex flex-col mb-4'>
          <h2 className='text-2xl font-semibold'>Policies</h2>
          <p>
            <strong>Abortion:</strong> {CandidateInfo[realId].policies.abortion}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Health Care:</strong>{' '}
            {CandidateInfo[realId].policies.healthcare}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Economy:</strong> {CandidateInfo[realId].policies.economy}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Immigration:</strong>{' '}
            {CandidateInfo[realId].policies.immigration}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Gun Control:</strong>{' '}
            {CandidateInfo[realId].policies.gunControl}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Climate Change:</strong>{' '}
            {CandidateInfo[realId].policies.climateChange}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Education:</strong>{' '}
            {CandidateInfo[realId].policies.education}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Taxes:</strong> {CandidateInfo[realId].policies.taxes}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>LGBTQ Rights:</strong>{' '}
            {CandidateInfo[realId].policies.lgbtqRights}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Foreign Policy:</strong>{' '}
            {CandidateInfo[realId].policies.foreignPolicy}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Drug Policy:</strong>{' '}
            {CandidateInfo[realId].policies.drugPolicy}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Criminal Justice Reform:</strong>{' '}
            {CandidateInfo[realId].policies.criminalJusticeReform}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Military Spending:</strong>{' '}
            {CandidateInfo[realId].policies.militarySpending}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
          <p>
            <strong>Voting Rights:</strong>{' '}
            {CandidateInfo[realId].policies.votingRights}{' '}
            <Link
              href='#'
              className='text-[#2592BF] underline hover:text-[#1a749b]'
            >
              [*]
            </Link>
          </p>
        </div>
        <div className='flex flex-col mb-4'>
          <h2 className='text-2xl font-semibold'>Links</h2>
          <a
            className='text-[#0073e6] underline hover:text-[#0056b3]'
            href={CandidateInfo[realId].online.wikipedia}
            target='_blank'
            rel='noreferrer'
          >
            Wikipedia
          </a>
          <a
            className='text-[#0073e6] underline hover:text-[#0056b3]'
            href={CandidateInfo[realId].online.officialWebsite}
            target='_blank'
            rel='noreferrer'
          >
            Official Website
          </a>
          <a
            className='text-[#0073e6] underline hover:text-[#0056b3]'
            href={CandidateInfo[realId].online.truthSocial}
            target='_blank'
            rel='noreferrer'
          >
            Social
          </a>
        </div>
      </div>
      <Footer />
    </div>
  );
}
