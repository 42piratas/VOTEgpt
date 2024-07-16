import type { Metadata } from 'next';
import { Inter, Roboto } from 'next/font/google';
import './globals.css';
import Footer from './Common/components/Footer';

const inter = Inter({ subsets: ['latin'] });

// roboto fontconst roboto = Roboto({
const roboto = Roboto({
  weight: ['400', '700'],
  style: ['normal', 'italic'],
  subsets: ['latin'],
  display: 'swap',
});

export const metadata: Metadata = {
  title: 'VoteGPT',
  description: 'KNOW YOUR CANDIDATES, LEAD THE CHANGE',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en'>
      <body className={(roboto.className,"flex flex-col min-h-screen justify-between py-2")}>
        {children}
        <Footer />
      </body>
    </html>
  );
}
