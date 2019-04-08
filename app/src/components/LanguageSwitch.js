import React from 'react';
import { Button } from 'reactstrap';
import { useTranslation } from 'react-i18next';

import SETTINGS from 'settings';


const LanguageSwitch = () => {
    const { i18n } = useTranslation();
    return (
        <>
            <p>
                Active language: {i18n.language}
            </p>
            {SETTINGS.LANGUAGE_ORDER.map((languageCode) => (
                <Button
                    key={languageCode}
                    onClick={() => i18n.changeLanguage(languageCode)}
                    className="mr-2"
                >
                    {SETTINGS.LANGUAGES[languageCode]}
                </Button>
            ))}
        </>
    );
};

export default LanguageSwitch;
