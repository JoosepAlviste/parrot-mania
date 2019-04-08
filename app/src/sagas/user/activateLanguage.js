import { takeLatest } from 'redux-saga/effects';
import Cookies from 'js-cookie';

import SETTINGS from 'settings';
import { SET_ACTIVE_LANGUAGE } from 'ducks/application';


function* setActiveLanguage(setActiveLanguageAction) {
    const currentLanguage = setActiveLanguageAction.language;
    const cookieLanguage = Cookies.get(SETTINGS.LANGUAGE_COOKIE_NAME);

    // Update language cookie
    if (currentLanguage !== cookieLanguage) {
        Cookies.set(SETTINGS.LANGUAGE_COOKIE_NAME, currentLanguage, { expires: 365 });
    }
}


export default function* activeLanguageWatcher() {
    yield takeLatest(SET_ACTIVE_LANGUAGE, setActiveLanguage);
}
