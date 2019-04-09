import { takeLatest } from 'redux-saga/effects';
import Cookies from 'js-cookie';

import SETTINGS from 'settings';

const SET_ACTIVE_LANGUAGE = 'sagas/user/SET_ACTIVE_LANGUAGE';

export const setActiveLanguage = (language) => ({
    type: SET_ACTIVE_LANGUAGE,
    language,
});


function setActiveLanguageSaga(setActiveLanguageAction) {
    const currentLanguage = setActiveLanguageAction.language;
    const cookieLanguage = Cookies.get(SETTINGS.LANGUAGE_COOKIE_NAME);

    // Update language cookie
    if (currentLanguage !== cookieLanguage) {
        Cookies.set(SETTINGS.LANGUAGE_COOKIE_NAME, currentLanguage, { expires: 365 });
    }
}


export default function* activeLanguageWatcher() {
    yield takeLatest(SET_ACTIVE_LANGUAGE, setActiveLanguageSaga);
}
