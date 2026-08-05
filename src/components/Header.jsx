import { useState, useEffect } from 'react'
import { useTranslation } from 'react-i18next'

function Header() {
  const { t, i18n } = useTranslation()
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'dark')

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('theme', theme)
  }, [theme])

  const toggleLanguage = () => {
    const newLang = i18n.language === 'en' ? 'zh-TW' : 'en'
    i18n.changeLanguage(newLang)
  }

  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light')
  }

  return (
    <header className="header">
      <a href="/" className="header__logo">PutoLim0226</a>
      <nav>
        <ul className="header__nav">
          <li><a href="#about" className="header__link">{t('header.about')}</a></li>
          <li><a href="#skills" className="header__link">{t('header.skills')}</a></li>
          <li><a href="#projects" className="header__link">{t('header.projects')}</a></li>
          <li style={{ display: 'flex', gap: '0.5rem' }}>
            <button onClick={toggleTheme} className="header__lang-btn" aria-label="Toggle Theme">
              {theme === 'light' ? '🌙' : '☀️'}
            </button>
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
