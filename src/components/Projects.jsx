import { useTranslation } from 'react-i18next'

const projects = [
  {
    id: 'caseprofile',
    image: 'mockups/caseprofile.jpg',
    github: null,
    demo: 'https://caseprofile2.asia.edu.tw/',
  },
  {
    id: 'huiyinseh',
    image: 'mockups/unnamed.jpg',
    github: null,
    demo: 'http://45.32.25.8:8080/',
  },
  {
    id: 'vintage',
    image: 'mockups/vintage.jpg',
    github: null,
    demo: 'https://putolim0226.github.io/vintage-e-commerce/',
  },
  {
    id: 'aurora',
    image: 'mockups/aurora.jpg',
    github: null,
    demo: 'https://putolim0226.github.io/aurora-coffee/',
  },
  {
    id: 'yhd',
    image: 'mockups/yhd.jpg',
    github: null,
    demo: 'https://yhd.tw/',
  },
  {
    id: 'playyhd',
    image: 'mockups/playyhd.jpg',
    github: null,
    demo: 'https://play.yhd.tw/',
  },
]

function Projects() {
  const { t } = useTranslation()

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
      <h2 className="projects__title">{t('projects.title')}</h2>
      <div className="projects__grid">
        {projects.map((project) => (
          <div 
            key={project.id} 
            className="projects__card"
            onMouseMove={(e) => handleMouseMove(e, e.currentTarget)}
            onMouseLeave={(e) => handleMouseLeave(e.currentTarget)}
          >
            <div className="projects__card-glare"></div>
            <img
              src={`${import.meta.env.BASE_URL}${project.image}`}
              alt={t(`projects.items.${project.id}.title`)}
              className="projects__image"
            />
            <div className="projects__body">
              <h3 className="projects__name">{t(`projects.items.${project.id}.title`)}</h3>
              <p className="projects__desc">{t(`projects.items.${project.id}.desc`)}</p>
              <div className="projects__links">
                {project.github && (
                  <a
                    href={project.github}
                    className="projects__link projects__link--secondary"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {t('projects.github')}
                  </a>
                )}
                {project.demo && (
                  <a
                    href={project.demo}
                    className="projects__link projects__link--primary"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {t('projects.demo')}
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
