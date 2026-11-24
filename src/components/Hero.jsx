import heroImg from '../assets/hero.png'
import { useTranslation } from 'react-i18next'

function Hero() {
  const { t, i18n } = useTranslation()
  const resumeFile = i18n.language === 'en' ? 'resume_en.pdf' : 'resume_zh.pdf'

  return (
    <section className="hero">
      <div className="hero__content">
        <h1 className="hero__title">{t('hero.title')}</h1>
        <p className="hero__subtitle">{t('hero.subtitle')}</p>
        <div className="hero__actions">
          <a href="#projects" className="hero__cta">{t('hero.cta')}</a>
          <a
            href={`${import.meta.env.BASE_URL}${resumeFile}`}
            target="_blank"
            rel="noopener noreferrer"
            className="hero__cta hero__cta--secondary"
          >
            {t('hero.resumeCta')}
          </a>
        </div>
      </div>
      <img src={heroImg} alt="PutoLim0226" className="hero__image" />
    </section>
  )
}

export default Hero
