import Navbar from './components/Navbar';
import HeroSection from './components/HeroSection';
import AgencySection from './components/AgencySection';
import HowItWorksSection from './components/HowItWorksSection';
import FaqSection from './components/FaqSection';
import Footer from './components/Footer';

export default function Home() {
  return (
    <main className="min-h-screen">
      <Navbar />
      <HeroSection />
      <AgencySection />
      <HowItWorksSection />
      <FaqSection />
      <Footer />
    </main>
  );
}
