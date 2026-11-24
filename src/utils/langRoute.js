export const SUPPORTED_LANGS = {
  EN: 'en',
  ZH: 'zh-TW',
  ZH_CN_ROUTE: 'zh_cn'
}

export function getLangFromUrl() {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '')
  let path = window.location.pathname
  if (base && path.startsWith(base)) {
    path = path.slice(base.length)
  }
  path = path.replace(/^\/+|\/+$/g, '')
  const firstSegment = path.split('/')[0]?.toLowerCase()

  if (firstSegment === 'zh_cn' || firstSegment === 'zh' || firstSegment === 'zh-tw' || firstSegment === 'zh-cn') {
    return 'zh-TW'
  }
  if (firstSegment === 'en') {
    return 'en'
  }
  return null
}

export function syncUrlWithLang(lang, replace = false) {
  const routeSegment = lang === 'en' ? 'en' : 'zh_cn'
  const base = import.meta.env.BASE_URL
  const newUrl = `${base}${routeSegment}${window.location.hash}`
  if (replace) {
    window.history.replaceState(null, '', newUrl)
  } else {
    window.history.pushState(null, '', newUrl)
  }
}
