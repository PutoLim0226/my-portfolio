import { useEffect } from 'react'
import { useTranslation } from 'react-i18next'
import Header from './components/Header'
import Hero from './components/Hero'
import About from './components/About'
import Skills from './components/Skills'
import Projects from './components/Projects'
import Footer from './components/Footer'
import { getLangFromUrl, syncUrlWithLang } from './utils/langRoute'

function App() {
  const { i18n } = useTranslation()

  useEffect(() => {
    // 1. Check if URL contains language (/en or /zh_cn)
    const urlLang = getLangFromUrl()
    if (urlLang) {
      if (i18n.language !== urlLang) {
        i18n.changeLanguage(urlLang)
      }
    } else {
      // Root access: default to English as requested or stored language
      const savedLang = localStorage.getItem('i18nextLng')
      const initialLang = (savedLang === 'zh-TW' || savedLang === 'zh_cn') ? 'zh-TW' : 'en'
      i18n.changeLanguage(initialLang)
      syncUrlWithLang(initialLang, true)
    }

    // 2. Listen to browser popstate (back/forward)
    const handlePopState = () => {
      const popLang = getLangFromUrl()
      if (popLang && i18n.language !== popLang) {
        i18n.changeLanguage(popLang)
      }
    }

    window.addEventListener('popstate', handlePopState)
    return () => window.removeEventListener('popstate', handlePopState)
  }, [i18n])

  return (
    <>
      <Header />
      <Hero />
      <About />
      <Skills />
      <Projects />
      <Footer />
    </>
  )
}

export default App
