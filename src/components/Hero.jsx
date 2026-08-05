import heroImg from '../assets/hero.png'
import { useTranslation } from 'react-i18next'

function Hero() {
  const { t } = useTranslation()

  return (
    <section className="hero">
      <div className="hero__content">
        <h1 className="hero__title">{t('hero.title')}</h1>
        <p className="hero__subtitle">{t('hero.subtitle')}</p>
        <a href="#projects" className="hero__cta">{t('hero.cta')}</a>
      </div>
      <img src={heroImg} alt="PutoLim0226" className="hero__image" />
    </section>
  )
}

export default Hero
