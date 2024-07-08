// pages/index.tsx
import React from 'react';
import Header from './Common/components/Header';
import SearchBar from './Common/components/SearchBar';
import Footer from './Common/components/Footer';

const Home: React.FC = () => {
  return (
    <div className='flex flex-col min-h-screen justify-between'>
      <main className='flex flex-col items-center justify-center gap-8 my-auto'>
        <Header />
        <SearchBar />
      </main>
      <Footer />
    </div>
  );
};

export default Home;
