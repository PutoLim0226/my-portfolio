import { useState, useEffect } from 'react'
import { useTranslation } from 'react-i18next'
import { syncUrlWithLang } from '../utils/langRoute'

function Header() {
  const { t, i18n } = useTranslation()
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'dark')

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('theme', theme)
  }, [theme])

  const toggleLanguage = () => {
    const isEn = i18n.language === 'en'
    const newLang = isEn ? 'zh-TW' : 'en'
    i18n.changeLanguage(newLang)
    syncUrlWithLang(newLang, false)
  }

  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light')
  }

  const resumeFile = i18n.language === 'en' ? 'resume_en.pdf' : 'resume_zh.pdf'
  const logoHref = `${import.meta.env.BASE_URL}${i18n.language === 'en' ? 'en' : 'zh_cn'}`

  return (
    <header className="header">
      <a href={logoHref} className="header__logo">PutoLim0226</a>
      <nav>
        <ul className="header__nav">
          <li><a href="#about" className="header__link">{t('header.about')}</a></li>
          <li><a href="#skills" className="header__link">{t('header.skills')}</a></li>
          <li><a href="#projects" className="header__link">{t('header.projects')}</a></li>
          <li>
            <a
              href={`${import.meta.env.BASE_URL}${resumeFile}`}
              target="_blank"
              rel="noopener noreferrer"
              className="header__link"
            >
              {t('header.resume')}
            </a>
          </li>
          <li className="header__actions">
            <button onClick={toggleTheme} className="header__lang-btn" aria-label="Toggle Theme">
              {theme === 'light' ? '🌙' : '☀️'}
            </button>
            <button onClick={toggleLanguage} className="header__lang-btn">
              {i18n.language === 'en' ? '中' : 'EN'}
            </button>
          </li>
        </ul>
      </nav>
    </header>
  )
}

export default Header
