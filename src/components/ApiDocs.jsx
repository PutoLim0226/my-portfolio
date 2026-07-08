import { useState, useEffect } from 'react'

function ApiDocs() {
  const [html, setHtml] = useState('')

  useEffect(() => {
    fetch(new URL('../docs/api_docs.html', import.meta.url).href)
      .then((res) => res.text())
      .then(setHtml)
  }, [])

  return (
    <section id="api-docs" className="api-docs">
      <h2 className="api-docs__title">API Documentation</h2>
      <div
        className="api-docs__content"
        dangerouslySetInnerHTML={{ __html: html }}
      />
    </section>
  )
}

export default ApiDocs
