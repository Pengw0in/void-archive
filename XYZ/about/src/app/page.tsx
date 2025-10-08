'use client';

import React, { useEffect, useRef, useState } from 'react';

const CreativeDirectorPage: React.FC = () => {
  const svgRef = useRef<SVGSVGElement>(null);
  const offsetRef = useRef(0);
  const animationRef = useRef<number | null>(null);

  // Initialize with a default width that matches the server
  const [windowSize, setWindowSize] = useState({
    width: 1600, // Default width
    height: 200
  });

  // Handle client-side initialization and window resizing
  useEffect(() => {
    setWindowSize({
      width: window.innerWidth,
      height: 200
    });

    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: 200
      });
    };

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);

  useEffect(() => {
    const numberOfWaves = 4;
    const speed = 1;
    const amplitude = Math.min(80, windowSize.width * 0.1);
    const containerWidth = windowSize.width;

    const generateWavePath = (offset: number): string => {
      const points: [number, number][] = [];
      const segments = 100; // Increase segments for smoother curves
    
      for (let i = 0; i <= segments; i++) {
        const x = (i / segments) * windowSize.width; // Use full width
        const normalizedX = i / segments;
        const taper = Math.sin(Math.PI * normalizedX);
    
        const y = (windowSize.height / 2) +
          Math.sin(normalizedX * 10 + offset) * amplitude * taper *
          Math.sin(offset / 2) *
          Math.sin(normalizedX * 3);
    
        points.push([x, y]);
      }
    
      return `M 0,${windowSize.height / 2} ` + // Start at (0, center)
        points.map(([x, y]) => `L ${x},${y}`).join(' ') + 
        ` L ${windowSize.width},${windowSize.height / 2}`; // End at full width
    };    

    const animate = (timestamp: number) => {
      if (!svgRef.current) return;

      offsetRef.current = (timestamp / 1000) * speed;
      const paths = svgRef.current.getElementsByTagName('path');

      Array.from(paths).forEach((path, index) => {
        const phase = (index / numberOfWaves) * Math.PI * 2;
        path.setAttribute('d', generateWavePath(offsetRef.current + phase));
      });

      animationRef.current = requestAnimationFrame(animate);
    };

    // Start animation on client side
    if (typeof window !== 'undefined') {
      animationRef.current = requestAnimationFrame(animate);
    }

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [windowSize]);

  return (
    <div className="min-h-screen bg-black text-white p-8">
      {/* Header */}
      <header className="flex justify-between items-center mb-12">
        <div>
          <h1 className="text-1xl font-light">Lohith Srikar.</h1>
          <p className="text-xs opacity-60">CyberSecurity& Game Development</p>
        </div>
        <nav className="flex gap-6 text-sm">
          <a href="https://github.com/Pengw0in" className="opacity-60 hover:opacity-100 transition-opacity">Github</a>
          <a href="https://discordapp.com/users/876134632905666621" className="opacity-60 hover:opacity-100 transition-opacity">Discord</a>
          <a href="https://www.linkedin.com/in/lohith-srikar-71132b316/" className="opacity-60 hover:opacity-100 transition-opacity">Linkedin</a>
        </nav>
      </header>

      {/* Animated Waveform */}
      <div className="my-24 w-full flex justify-center overflow-hidden">
        <svg
          ref={svgRef}
          width="100%" // Responsive width
          height="200"
          viewBox={`0 0 ${windowSize.width} ${windowSize.height}`} // Dynamic viewBox
          preserveAspectRatio="xMidYMid slice" // Keeps vertical centering
          style={{ backgroundColor: 'black' }}
        >
          {Array.from({ length: 5 }).map((_, index) => (
            <path
              key={index}
              stroke="white"
              fill="none"
              strokeWidth="2"
              strokeOpacity={`${0.8 - index * 0.15}`}
              d=""
            />
          ))}
        </svg>
      </div>
      <div className="min-h-screen bg-black text-white p-8">

{/* Big Text Section */}
<div className="mb-20">
  <h1 className="text-5xl md:text-8xl font-serif font-light leading-tight">
    Echoes Beyond<br />
    the Vile Unseen
  </h1>
</div>

  {/* Main Content */}
  
  <div className="mt-40 grid grid-cols-12 gap-8">

{/* Info Section (Left) */}
<div className="col-span-12 md:col-span-4 text-left relative">
  <h3 className="text-lg font-light mb-6">Info</h3>
  <div className="absolute top-0 left-0 h-full w-px bg-gray-500 opacity-30 md:block hidden"></div>

  <div className="space-y-6 text-sm text-gray-400 leading-relaxed">
    <div className="relative">
      <span className="absolute left-0 w-2 h-2 bg-gray-400 rounded-full -ml-1"></span>
      <p className="font-medium text-white">Bachelor of Technology</p>
      <p className="italic">Computer Science — 2024–2028</p>
      <p className="opacity-70">GITAM University</p>
    </div>

    <div className="relative">
      <span className="absolute left-0 w-2 h-2 bg-gray-400 rounded-full -ml-1"></span>
      <p className="font-medium text-white">Intermediate</p>
      <p className="italic">Science — 2022–2024</p>
      <p className="opacity-70">Sri Chaitanya</p>
    </div>

    <div className="relative">
      <span className="absolute left-0 w-2 h-2 bg-gray-400 rounded-full -ml-1"></span>
      <p className="font-medium text-white">School</p>
      <p className="italic">Primary ED — 20XX–2022</p>
      <p className="opacity-70">Sri Chaitanya & SFS</p>
    </div>
  </div>
</div>

{/* Main Content (Right) */}
<div className="col-span-12 md:col-span-8 space-y-6 text-lg font-light leading-relaxed opacity-90">
  <p>
    A dreamer adrift in code and constellations,<br />
    Shaping galaxies where silence sings,<br />
    And pixels bloom like forgotten stars.
  </p>
  <p>
    Explorer of the unconventional,<br />
    Where drifting worlds and ancient rhythms collide,<br />
    A quiet architect of stories untold—
  </p>
  <p>
    Forever chasing the spaces between,<br />
    Where mystery lingers and meaning hides.
  </p>
  <p>
    Forever lost in the drift, yet always found<br />
    In the spaces between worlds unknown.
  </p>
</div>

</div>

    </div>
    </div>
  );
};

export default CreativeDirectorPage;
