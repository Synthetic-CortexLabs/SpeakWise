import Image from 'next/image';
import Link from 'next/link';

export default function HeroSection() {
  return (
    <section className="relative min-h-screen bg-neutral-black overflow-hidden">
      {/* Background Image */}
      <div className="absolute inset-0 z-0">
        <Image
          src="/images/conference-bg.jpg"
          alt="Conference background"
          fill
          className="object-cover opacity-40"
          priority
        />
      </div>

      {/* World Map Overlay */}
      <div className="absolute inset-0 z-10 opacity-15">
        <Image
          src="/images/world-map.png"
          alt="World map"
          fill
          className="object-contain"
          priority
        />
      </div>

      {/* Content */}
      <div className="relative z-20 container mx-auto px-6 flex items-center min-h-screen">
        <div className="max-w-xl pt-20">
          <h1 className="text-4xl sm:text-5xl font-bold text-white mb-4 leading-tight">
            Have access<br />
            to <span className="text-primary">conferences</span><br />
            you attended?
          </h1>
          <p className="text-base text-gray-300 mb-8">
            Whichever tech conference you attended<br />
            can be found here
          </p>
          <Link
            href="/get-started"
            className="inline-block bg-primary text-white px-6 py-2.5 rounded-full text-sm font-semibold hover:bg-primary-harsh transition-colors"
          >
            Get Started
          </Link>
        </div>

        {/* Featured Image */}
        <div className="absolute right-6 top-1/2 transform -translate-y-1/2 w-[400px] h-[250px] rounded-xl overflow-hidden shadow-xl">
          <Image
            src="/images/conference-feature.jpg"
            alt="Conference feature"
            fill
            className="object-cover"
          />
        </div>
      </div>
    </section>
  );
}
