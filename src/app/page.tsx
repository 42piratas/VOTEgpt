// pages/index.tsx
import React from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import Footer from './components/Footer';

const Home: React.FC = () => {
  return (
    <div className='flex flex-col min-h-screen justify-between'>
      <main className='flex flex-col items-center justify-center'>
        <Header />
        <SearchBar />
      </main>
      <Footer />
    </div>
  );
};

export default Home;
