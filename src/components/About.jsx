import { useTranslation } from 'react-i18next'

function About() {
  const { t } = useTranslation()

  return (
    <section id="about" className="about">
      <h2 className="about__title">{t('about.title')}</h2>
      <p className="about__text">{t('about.text')}</p>
    </section>
  )
}

export default About
