import heroImg from '../assets/hero.png'

function Hero() {
  return (
    <section className="hero">
      <div className="hero__content">
        <h1 className="hero__title">Hi, I'm PutoLim0226</h1>
        <p className="hero__subtitle">
          Full-stack developer who builds fast, scalable web applications. I turn
          complex business problems into clean, maintainable code.
        </p>
        <a href="#projects" className="hero__cta">View Projects</a>
      </div>
      <img src={heroImg} alt="PutoLim0226" className="hero__image" />
    </section>
  )
}

export default Hero
