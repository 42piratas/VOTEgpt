// pages/index.tsx
import React from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import Footer from './components/Footer';
import BadgesArea from './components/Badges';

const Home: React.FC = () => {
  return (
    <div className='flex flex-col min-h-screen justify-between'>
      <main className='flex flex-col items-center justify-center gap-8 my-auto'>
        <Header />
        <SearchBar />
        <BadgesArea />
      </main>
      <Footer />
    </div>
  );
};

export default Home;
