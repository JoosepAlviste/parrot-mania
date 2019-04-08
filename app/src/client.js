import '@tg-resources/fetch-runtime';
import { loadableReady } from '@loadable/component';
import React from 'react';
import { hydrate } from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'connected-react-router';
import Cookies from 'js-cookie';
import { RenderChildren } from 'tg-named-routes';
import { useSSR } from 'react-i18next';

import configureStore from 'configuration/configureStore';
import routes from 'configuration/routes';
import { setActiveLanguage } from 'sagas/user/activateLanguage';
import SETTINGS from 'settings';
import Sentry from 'services/sentry';
import i18n from 'utils/i18next';


// Configure Sentry only in production
if (process.env.NODE_ENV === 'production') {
    Sentry.init({
        dsn: SETTINGS.RAVEN_PUBLIC_DSN,
    });
}

// Store initial state in variable
const initialState = window.__initial_state__ || {};

// If not in development, clear the value attached to window
if (process.env.NODE_ENV === 'production') {
    window.__initial_state__ = null;
}

const { store, history } = configureStore(initialState);

// Get correct language from store and cookies
const stateLanguage = i18n.language;
const cookieLanguage = Cookies.get(SETTINGS.LANGUAGE_COOKIE_NAME);

// Get valid language
const currentLanguage = stateLanguage || cookieLanguage || SETTINGS.DEFAULT_LANGUAGE;


const App = ({ appRoutes }) => {
    // Load translations that were sent with the initial HTML from the server
    useSSR(
        /* eslint-disable no-underscore-dangle */
        window.__initial_i18n_store__,
        window.__initial_language__,
        /* eslint-enable no-underscore-dangle */
    );

    return (
        <Provider store={store}>
            <ConnectedRouter history={history}>
                <RenderChildren routes={appRoutes} />
            </ConnectedRouter>
        </Provider>
    );
};

const renderApp = (appRoutes) => {
    hydrate(
        <App appRoutes={appRoutes} />,
        document.getElementById('root'),
    );
};


loadableReady().then(() => {
    // Update language if necessary
    if (stateLanguage !== currentLanguage) {
        store.dispatch(setActiveLanguage(currentLanguage));
        i18n.changeLanguage(currentLanguage);
    }

    renderApp(routes);
});

if (module.hot) {
    module.hot.accept('./configuration/routes', () => {
        renderApp(routes);
    });
}
