import type { Metadata } from 'next';
import { Inter, Roboto } from 'next/font/google';
import './globals.css';

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
      <body className={roboto.className}>{children}</body>
    </html>
  );
}
