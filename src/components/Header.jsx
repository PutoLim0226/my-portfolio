function Header() {
  return (
    <header className="header">
      <a href="/" className="header__logo">PutoLim0226</a>
      <nav>
        <ul className="header__nav">
          <li><a href="#about" className="header__link">About</a></li>
          <li><a href="#skills" className="header__link">Skills</a></li>
          <li><a href="#projects" className="header__link">Projects</a></li>
          <li><a href="#api-docs" className="header__link">API Docs</a></li>
        </ul>
      </nav>
    </header>
  )
}

export default Header
