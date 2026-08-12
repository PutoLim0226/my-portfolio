import { useTranslation } from 'react-i18next'

const skillCategories = [
  { id: 'frontend', items: ['React', 'Tailwind CSS'] },
  { id: 'backend', items: ['PHP'] },
  { id: 'database', items: ['MySQL', 'Postgres', 'SQLite', 'Redis'] },
  { id: 'infrastructure', items: ['Linux', 'Nginx'] }
]

function Skills() {
  const { t } = useTranslation()

  return (
    <section id="skills" className="skills">
      <h2 className="skills__title">{t('skills.title')}</h2>
      <div className="skills__categories">
        {skillCategories.map((category) => (
          <div key={category.id} className="skills__category">
            <h3 className="skills__category-title">{t(`skills.${category.id}`)}</h3>
            <ul className="skills__list">
              {category.items.map((skill) => (
                <li key={skill} className="skills__tag">{skill}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </section>
  )
}

export default Skills
