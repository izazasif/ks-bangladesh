import { watchEffect } from 'vue'

const SITE = 'KSI Bangladesh'
const BASE_URL = 'https://ks-bangladesh.vercel.app'
const DEFAULT_IMAGE = `${BASE_URL}/logo.png`

function setMeta(attr, name, content) {
  let el = document.querySelector(`meta[${attr}="${name}"]`)
  if (!el) {
    el = document.createElement('meta')
    el.setAttribute(attr, name)
    document.head.appendChild(el)
  }
  el.setAttribute('content', content)
}

function setLink(rel, href) {
  let el = document.querySelector(`link[rel="${rel}"]`)
  if (!el) {
    el = document.createElement('link')
    el.setAttribute('rel', rel)
    document.head.appendChild(el)
  }
  el.setAttribute('href', href)
}

export function useSEO({ title, description, keywords, image, type = 'website', path = '' }) {
  watchEffect(() => {
    const fullTitle = title ? `${title} | ${SITE}` : SITE
    const img = image || DEFAULT_IMAGE
    const canonical = `${BASE_URL}${path}`

    // Basic
    document.title = fullTitle
    setMeta('name', 'description', description || '')
    if (keywords) setMeta('name', 'keywords', keywords)

    // Open Graph
    setMeta('property', 'og:title', fullTitle)
    setMeta('property', 'og:description', description || '')
    setMeta('property', 'og:image', img)
    setMeta('property', 'og:url', canonical)
    setMeta('property', 'og:type', type)
    setMeta('property', 'og:site_name', SITE)
    setMeta('property', 'og:locale', 'en_BD')

    // Twitter Card
    setMeta('name', 'twitter:card', 'summary_large_image')
    setMeta('name', 'twitter:title', fullTitle)
    setMeta('name', 'twitter:description', description || '')
    setMeta('name', 'twitter:image', img)

    // Canonical
    setLink('canonical', canonical)
  })
}
