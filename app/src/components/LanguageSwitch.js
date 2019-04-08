import React, { useCallback } from 'react';
import { Button } from 'reactstrap';
import { useTranslation } from 'react-i18next';
import { connect } from 'react-redux';
import * as PropTypes from 'prop-types';

import SETTINGS from 'settings';
import { setActiveLanguage } from 'sagas/user/activateLanguage';


const LanguageSwitch = ({ onSwitch }) => {
    const { t, i18n } = useTranslation();
    const changeLanguage = useCallback((languageCode) => {
        i18n.changeLanguage(languageCode);
        onSwitch(languageCode);
    }, [i18n, onSwitch]);

    return (
        <>
            <p>
                {t('Active language')}: {i18n.language}
            </p>
            {SETTINGS.LANGUAGE_ORDER.map((languageCode) => (
                <Button
                    key={languageCode}
                    onClick={() => changeLanguage(languageCode)}
                    className="mr-2"
                >
                    {SETTINGS.LANGUAGES[languageCode]}
                </Button>
            ))}
        </>
    );
};

LanguageSwitch.propTypes = {
    onSwitch: PropTypes.func.isRequired,
};

const mapDispatchToProps = (dispatch) => ({
    onSwitch: (languageCode) => dispatch(setActiveLanguage(languageCode)),
});

export default connect(
    null,
    mapDispatchToProps,
)(LanguageSwitch);
