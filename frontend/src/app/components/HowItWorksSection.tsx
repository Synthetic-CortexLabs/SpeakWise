import Image from 'next/image';

const ProcessCard = ({ icon, title, color }: { icon: string; title: string; color: string }) => (
  <div className="bg-white rounded-xl p-5 shadow-md relative">
    <div className={`absolute -top-4 -left-4 w-12 h-12 ${color} rounded-lg flex items-center justify-center`}>
      <Image
        src={icon}
        alt={title}
        width={20}
        height={20}
        className="text-white"
      />
    </div>
    <h3 className="text-base font-semibold mt-4">{title}</h3>
  </div>
);

export default function HowItWorksSection() {
  const processSteps = [
    {
      icon: '/images/icons/globe.svg',
      title: 'Region Selection',
      color: 'bg-[#00BCD4]'
    },
    {
      icon: '/images/icons/earth.svg',
      title: 'Country Selection',
      color: 'bg-[#00E676]'
    },
    {
      icon: '/images/icons/calendar.svg',
      title: 'Event Date',
      color: 'bg-[#AA00FF]'
    },
    {
      icon: '/images/icons/event.svg',
      title: 'Event Selection',
      color: 'bg-primary'
    },
    {
      icon: '/images/icons/review.svg',
      title: 'Event Review',
      color: 'bg-neutral-black'
    }
  ];

  return (
    <section className="py-16 px-6 bg-[#FFF5F2]">
      <div className="container mx-auto">
        {/* Section Header */}
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-3">
            See How It <span className="text-primary">Works</span>
          </h2>
          <p className="text-sm text-gray-600">
            Discover how <span className="text-primary font-medium">Speak</span>
            <span className="font-medium">Wise</span> can help you find everything you're looking for.
          </p>
        </div>

        {/* Process Cards */}
        <div className="grid grid-cols-3 gap-16 mb-16">
          {processSteps.slice(0, 3).map((step, index) => (
            <ProcessCard key={index} {...step} />
          ))}
        </div>
        
        {/* Bottom Row - Centered */}
        <div className="grid grid-cols-2 gap-16 max-w-2xl mx-auto">
          {processSteps.slice(3).map((step, index) => (
            <ProcessCard key={index} {...step} />
          ))}
        </div>
      </div>
    </section>
  );
} 