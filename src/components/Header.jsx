import { useTranslation } from 'react-i18next'

function Header() {
  const { t, i18n } = useTranslation()

  const toggleLanguage = () => {
    const newLang = i18n.language === 'en' ? 'zh-TW' : 'en'
    i18n.changeLanguage(newLang)
  }

  return (
    <header className="header">
      <a href="/" className="header__logo">PutoLim0226</a>
      <nav>
        <ul className="header__nav">
          <li><a href="#about" className="header__link">{t('header.about')}</a></li>
          <li><a href="#skills" className="header__link">{t('header.skills')}</a></li>
          <li><a href="#projects" className="header__link">{t('header.projects')}</a></li>
          <li>
            <button onClick={toggleLanguage} className="header__lang-btn">
              {i18n.language === 'en' ? '🇹🇼 中' : '🇺🇸 EN'}
            </button>
          </li>
        </ul>
      </nav>
    </header>
  )
}

export default Header
