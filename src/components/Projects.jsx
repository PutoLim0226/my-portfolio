const projects = [
  {
    title: 'Case Profile System',
    description: 'An academic profile and case study management system with dynamic data visualization.',
    image: '/mockups/caseprofile.jpg',
    github: null,
    demo: 'https://caseprofile2.asia.edu.tw/',
  },
  {
    title: 'Data Dashboard Nexus',
    description: 'A powerful backend management dashboard with real-time analytics and task tracking.',
    image: '/mockups/unnamed.jpg',
    github: null,
    demo: 'http://45.32.25.8:8080/',
  },
  {
    title: 'Vintage E-Commerce',
    description: 'A high-end e-commerce platform for vintage treasures featuring seamless cart operations.',
    image: '/mockups/vintage.jpg',
    github: 'https://github.com/PutoLim0226/vintage-e-commerce',
    demo: null,
  },
  {
    title: 'Aurora Coffee',
    description: 'A glowing, immersive online coffee shop experience with interactive menus.',
    image: '/mockups/aurora.jpg',
    github: 'https://github.com/PutoLim0226/aurora-coffee',
    demo: null,
  },
  {
    title: 'AIGem Dashboard',
    description: 'A next-generation AI model performance monitoring dashboard.',
    image: '/mockups/aigem.jpg',
    github: 'https://github.com/PutoLim0226/AIGem',
    demo: null,
  },
  {
    title: 'YHD Corporate Site',
    description: 'A sleek, digital transformation corporate landing page for YHD.',
    image: '/mockups/yhd.jpg',
    github: null,
    demo: 'https://yhd.tw/',
  },
  {
    title: 'Play YHD',
    description: 'An interactive gaming portal with vibrant neon themes and community features.',
    image: '/mockups/playyhd.jpg',
    github: null,
    demo: 'https://play.yhd.tw/',
  },
]

function Projects() {
  const handleMouseMove = (e, card) => {
    const rect = card.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    
    const centerX = rect.width / 2
    const centerY = rect.height / 2
    
    const rotateX = ((y - centerY) / centerY) * -10
    const rotateY = ((x - centerX) / centerX) * 10
    
    card.style.setProperty('--x', `${x}px`)
    card.style.setProperty('--y', `${y}px`)
    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`
  }

  const handleMouseLeave = (card) => {
    card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`
  }

  return (
    <section id="projects" className="projects">
      <h2 className="projects__title">Featured Projects</h2>
      <div className="projects__grid">
        {projects.map((project) => (
          <div 
            key={project.title} 
            className="projects__card"
            onMouseMove={(e) => handleMouseMove(e, e.currentTarget)}
            onMouseLeave={(e) => handleMouseLeave(e.currentTarget)}
          >
            <div className="projects__card-glare"></div>
            <img
              src={project.image}
              alt={project.title}
              className="projects__image"
            />
            <div className="projects__body">
              <h3 className="projects__name">{project.title}</h3>
              <p className="projects__desc">{project.description}</p>
              <div className="projects__links">
                {project.github && (
                  <a
                    href={project.github}
                    className="projects__link projects__link--secondary"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    GitHub
                  </a>
                )}
                {project.demo && (
                  <a
                    href={project.demo}
                    className="projects__link projects__link--primary"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Demo
                  </a>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default Projects
