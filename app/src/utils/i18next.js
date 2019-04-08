import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n
    .use(initReactI18next)
    .init({
        lng: 'et',
        fallbackLng: 'en',
        debug: true,

        interpolation: {
            escapeValue: false,
        },

        resources: {
            en: {
                translation: {
                    'Hello world!': 'Hello world!',
                },
            },
            et: {
                translation: {
                    'Hello world!': 'Tere maailm!',
                },
            },
        },
    });

export default i18n;
