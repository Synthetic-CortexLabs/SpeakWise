import Image from 'next/image';

export default function AgencySection() {
  const logos = [
    { src: '/images/logos/gdg.png', alt: 'GDG Logo' },
    { src: '/images/logos/google-io.png', alt: 'Google I/O Extended Logo' },
    { src: '/images/logos/devfest.png', alt: 'DevFest Logo' },
    { src: '/images/logos/flutter.png', alt: 'Flutter Logo' },
  ];

  return (
    <section className="py-16 px-6">
      {/* Conference Logos */}
      <div className="container mx-auto mb-16">
        <div className="flex justify-between items-center">
          {logos.map((logo, index) => (
            <div key={index} className="w-32 h-12 relative">
              <Image
                src={logo.src}
                alt={logo.alt}
                fill
                className="object-contain"
              />
            </div>
          ))}
        </div>
      </div>

      {/* Agency Content */}
      <div className="container mx-auto grid grid-cols-2 gap-8 items-center">
        {/* Left Content */}
        <div>
          <h2 className="text-3xl font-bold mb-10">
            Our <span className="text-primary">Agency</span>
          </h2>
          <div className="space-y-6">
            <p className="text-base font-medium">
              Gives you access to conferences you attended.
            </p>
            <p className="text-base font-medium">
              Gives you an opportunity to review talks or conferences you attended.
            </p>
            <p className="text-base font-medium">
              Gives you the power to track your speaking engagements.
            </p>
          </div>
        </div>

        {/* Right Images */}
        <div className="relative h-[350px]">
          <div className="absolute right-0 top-0 w-[350px] h-[220px] rounded-xl overflow-hidden shadow-lg transform rotate-[-4deg]">
            <Image
              src="/images/conference-team.jpg"
              alt="Conference team"
              fill
              className="object-cover"
            />
          </div>
          <div className="absolute right-16 bottom-0 w-[350px] h-[220px] rounded-xl overflow-hidden shadow-lg transform rotate-[4deg]">
            <Image
              src="/images/conference-group.jpg"
              alt="Conference group"
              fill
              className="object-cover"
            />
          </div>
        </div>
      </div>
    </section>
  );
} 