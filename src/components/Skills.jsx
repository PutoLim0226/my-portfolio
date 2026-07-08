const skills = ['React', 'PHP', 'MySQL', 'Redis', 'Linux']

function Skills() {
  return (
    <section id="skills" className="skills">
      <h2 className="skills__title">Tech Stack</h2>
      <ul className="skills__list">
        {skills.map((skill) => (
          <li key={skill} className="skills__tag">{skill}</li>
        ))}
      </ul>
    </section>
  )
}

export default Skills
