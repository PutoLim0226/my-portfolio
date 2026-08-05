import { useTranslation } from 'react-i18next'

function Footer() {
  const { t } = useTranslation()
  return (
    <footer className="footer">
      <p className="footer__text">
        {t('footer.text')}{' '}
        <a href="https://react.dev" className="footer__link" target="_blank" rel="noopener noreferrer">React</a>
        {' '}+{' '}
        <a href="https://vite.dev" className="footer__link" target="_blank" rel="noopener noreferrer">Vite</a>
      </p>
    </footer>
  )
}

export default Footer
