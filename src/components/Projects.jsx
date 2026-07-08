const projects = [
  {
    title: 'E-Commerce Platform Revamp',
    description:
      'Rebuilt the product listing with lazy loading and Redis caching, reducing page load time by 50% and cutting server costs by 30%.',
    image: 'https://placehold.co/600x340/1f2028/c084fc?text=E-Commerce',
    github: 'https://github.com/PutoLim0226/ecommerce-platform',
    demo: 'https://ecommerce.putolim0226.dev',
  },
  {
    title: 'Real-Time Dashboard',
    description:
      'Designed a WebSocket-powered analytics dashboard that replaced 5-minute polling with instant updates, enabling the ops team to respond to incidents 3× faster.',
    image: 'https://placehold.co/600x340/1f2028/c084fc?text=Dashboard',
    github: 'https://github.com/PutoLim0226/realtime-dashboard',
    demo: 'https://dashboard.putolim0226.dev',
  },
  {
    title: 'CI/CD Pipeline Automation',
    description:
      'Automated the entire deployment workflow on Linux servers, shrinking release cycles from 2 days to 15 minutes and eliminating manual deployment errors.',
    image: 'https://placehold.co/600x340/1f2028/c084fc?text=CI%2FCD',
    github: 'https://github.com/PutoLim0226/cicd-automation',
    demo: 'https://cicd.putolim0226.dev',
  },
]

function Projects() {
  return (
    <section id="projects" className="projects">
      <h2 className="projects__title">Featured Projects</h2>
      <div className="projects__grid">
        {projects.map((project) => (
          <div key={project.title} className="projects__card">
            <img
              src={project.image}
              alt={project.title}
              className="projects__image"
            />
            <div className="projects__body">
              <h3 className="projects__name">{project.title}</h3>
              <p className="projects__desc">{project.description}</p>
              <div className="projects__links">
                <a
                  href={project.github}
                  className="projects__link projects__link--secondary"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  GitHub
                </a>
                <a
                  href={project.demo}
                  className="projects__link projects__link--primary"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Demo
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default Projects
