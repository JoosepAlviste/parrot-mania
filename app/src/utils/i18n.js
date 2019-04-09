import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import XHRBackend from 'i18next-xhr-backend';

const isClientSide = process && !process.release;

const options = {
    fallbackLng: 'en',
    load: 'languageOnly',  // No region-specific locales (en-US, de-DE, etc.)
    ns: ['translations'],
    defaultNS: 'translations',

    saveMissing: true,
    debug: true,

    interpolation: {
        escapeValue: false,  // Not needed for React
    },

    wait: isClientSide,
};

// In the browser use XHR backend and init react-i18next
if (isClientSide) {
    i18n
        .use(XHRBackend)
        .use(initReactI18next);
}

// Only initialize if i18next has not yet been initialized
if (!i18n.isInitialized) {
    i18n.init(options);
}

export default i18n;
