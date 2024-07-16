import React from 'react';
import Header from './Common/components/Header';
import SearchBar from './Common/components/SearchBar';

const Home: React.FC = () => {
  return (
    <main className='flex flex-col items-center justify-center gap-8 my-auto'>
      <Header />
      <SearchBar />
    </main>
  );
};

export default Home;