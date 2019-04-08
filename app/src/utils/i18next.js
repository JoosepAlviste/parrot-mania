import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n
    .use(initReactI18next)
    .init({
        fallbackLng: 'en',
        debug: true,

        interpolation: {
            escapeValue: false,
        },

        resources: {
            en: {
                translation: {
                    'Hello world!': 'Hello world!',
                    'Signup': 'Signup',
                    'Login': 'Login',
                    'Logout': 'Logout',
                    'Admin panel': 'Admin panel',
                    'Restricted view': 'Restricted view',
                    'Page not Found': 'Page not found',
                    'Insufficient permissions': 'Insufficient permissions',
                    'You don\'t have permissions to access this page':
                        'You don\'t have permissions to access this page',
                    'Forgot password': 'Forgot password',
                },
            },
            et: {
                translation: {
                    'Hello world!': 'Tere maailm!',
                    'Signup': 'Registreeru',
                    'Login': 'Logi sisse',
                    'Logout': 'Logi välja',
                    'Admin panel': 'Administratsioon',
                    'Restricted view': 'Piiratud vaade',
                    'Page not Found': 'Lehekülge ei leitud',
                    'Insufficient permissions': 'Pole piisavalt õigusi',
                    'You don\'t have permissions to access this page':
                        'Teil pole piisavalt õigusi, et seda lehekülge näha',
                    'Forgot password': 'Unustasid parooli?',
                },
            },
        },
    });

export default i18n;
