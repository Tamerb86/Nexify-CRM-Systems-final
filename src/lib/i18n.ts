// i18n Configuration for Nexify CRM Systems
// Supports: Arabic (AR), Norwegian (NO), English (EN)

import ar from '../translations/ar.json';
import no from '../translations/no.json';
import en from '../translations/en.json';

// Supported languages
export type Language = 'ar' | 'no' | 'en';
export const languagesList: Language[] = ['ar', 'no', 'en'];

// Default language
export const defaultLang: Language = 'no';

// Language configurations
export const languages: Record<Language, {
  name: string;
  nativeName: string;
  dir: 'ltr' | 'rtl';
  locale: string;
  flag: string;
}> = {
  ar: { name: 'Arabic', nativeName: 'العربية', dir: 'rtl', locale: 'ar-SA', flag: '🇸🇦' },
  no: { name: 'Norwegian', nativeName: 'Norsk', dir: 'ltr', locale: 'nb-NO', flag: '🇳🇴' },
  en: { name: 'English', nativeName: 'English', dir: 'ltr', locale: 'en-US', flag: '🇺🇸' }
};

// Translation data
const translations: Record<Language, typeof no> = { ar, no, en };

// Get translations for a language
export function getTranslations(lang: Language = defaultLang) {
  return translations[lang] || translations[defaultLang];
}

// Get nested translation value by key path (e.g., 'home.hero.title')
export function t(lang: Language, key: string): string {
  const keys = key.split('.');
  let value: any = translations[lang] || translations[defaultLang];
  
  for (const k of keys) {
    if (value && typeof value === 'object' && k in value) {
      value = value[k];
    } else {
      // Fallback to default language
      value = translations[defaultLang];
      for (const fallbackKey of keys) {
        if (value && typeof value === 'object' && fallbackKey in value) {
          value = value[fallbackKey];
        } else {
          return key;
        }
      }
      break;
    }
  }
  
  return typeof value === 'string' ? value : key;
}

// Get direction for a language
export function getDirection(lang: Language): 'ltr' | 'rtl' {
  return languages[lang].dir;
}

// Check if language is RTL
export function isRTL(lang: Language): boolean {
  return languages[lang].dir === 'rtl';
}

// URL Structure for each language
export const urlStructure: Record<Language, Record<string, string>> = {
  ar: {
    home: '/ar/',
    services: '/ar/خدمات',
    projects: '/ar/الاعمال',
    pricing: '/ar/الاسعار',
    about: '/ar/من-نحن',
    contact: '/ar/تواصل',
    blog: '/ar/مدونة',
    privacy: '/ar/الخصوصية',
    terms: '/ar/الشروط'
  },
  no: {
    home: '/no/',
    services: '/no/tjenester',
    projects: '/no/prosjekter',
    pricing: '/no/priser',
    about: '/no/om-oss',
    contact: '/no/kontakt',
    blog: '/no/blogg',
    privacy: '/no/personvern',
    terms: '/no/vilkar'
  },
  en: {
    home: '/en/',
    services: '/en/services',
    projects: '/en/projects',
    pricing: '/en/pricing',
    about: '/en/about',
    contact: '/en/contact',
    blog: '/en/blog',
    privacy: '/en/privacy',
    terms: '/en/terms'
  }
};

// Get URL for a page in a specific language
export function getLocalizedUrl(page: string, lang: Language): string {
  return urlStructure[lang]?.[page] || urlStructure[defaultLang][page] || '/';
}

// Get current language from URL path
export function getLangFromUrl(url: URL | string): Language {
  const pathname = typeof url === 'string' ? url : url.pathname;
  
  // Check for language prefix
  for (const lang of languagesList) {
    if (pathname.startsWith(`/${lang}/`) || pathname === `/${lang}`) {
      return lang;
    }
  }
  
  return defaultLang;
}

// Get page name from URL path
export function getPageFromUrl(url: URL | string): string {
  const pathname = typeof url === 'string' ? url : url.pathname;
  const lang = getLangFromUrl(pathname);
  
  // Find matching page
  for (const [page, path] of Object.entries(urlStructure[lang])) {
    if (pathname === path || pathname === path.slice(0, -1) || pathname + '/' === path) {
      return page;
    }
  }
  
  return 'home';
}

// Generate hreflang tags for a page
export function generateHreflangTags(page: string, baseUrl: string = 'https://nexifyhub.no'): string[] {
  const tags: string[] = [];
  
  for (const lang of languagesList) {
    const url = urlStructure[lang][page];
    if (url) {
      const hreflang = lang === 'no' ? 'nb' : lang;
      tags.push(`<link rel="alternate" hreflang="${hreflang}" href="${baseUrl}${url}" />`);
    }
  }
  
  // Add x-default (points to default language)
  tags.push(`<link rel="alternate" hreflang="x-default" href="${baseUrl}${urlStructure[defaultLang][page]}" />`);
  
  return tags;
}

// Generate canonical URL for a page
export function generateCanonicalUrl(page: string, lang: Language, baseUrl: string = 'https://nexifyhub.no'): string {
  const url = urlStructure[lang][page] || urlStructure[defaultLang][page];
  return `${baseUrl}${url}`;
}

// Get all alternate URLs for a page (for language switcher)
export function getAlternateUrls(page: string): Record<Language, string> {
  const urls: Record<Language, string> = {} as Record<Language, string>;
  
  for (const lang of languagesList) {
    urls[lang] = urlStructure[lang][page] || urlStructure[defaultLang][page];
  }
  
  return urls;
}

// Navigation items for each language
export function getNavItems(lang: Language) {
  const trans = getTranslations(lang);
  const urls = urlStructure[lang];
  
  return [
    { label: trans.nav.home, href: urls.home },
    { label: trans.nav.services, href: urls.services },
    { label: trans.nav.projects, href: urls.projects },
    { label: trans.nav.pricing, href: urls.pricing },
    { label: trans.nav.about, href: urls.about },
    { label: trans.nav.contact, href: urls.contact },
    { label: trans.nav.blog, href: urls.blog }
  ];
}

// Export all pages for static generation
export const allPages = ['home', 'services', 'projects', 'pricing', 'about', 'contact', 'blog', 'privacy', 'terms'];
