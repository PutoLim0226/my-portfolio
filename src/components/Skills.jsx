import { useTranslation } from 'react-i18next'

const skills = ['React', 'PHP', 'MySQL', 'Redis', 'Linux']

function Skills() {
  const { t } = useTranslation()

  return (
    <section id="skills" className="skills">
      <h2 className="skills__title">{t('skills.title')}</h2>
      <ul className="skills__list">
        {skills.map((skill) => (
          <li key={skill} className="skills__tag">{skill}</li>
        ))}
      </ul>
    </section>
  )
}

export default Skills
