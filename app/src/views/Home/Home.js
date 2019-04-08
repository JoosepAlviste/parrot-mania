import React from 'react';
import { Helmet } from 'react-helmet';
import { useTranslation } from 'react-i18next';

import withView from 'decorators/withView';
import LanguageSwitch from 'components/LanguageSwitch';
import logo from 'styles/images/react.svg';

import styles from './Home.module.css';
import './Home.css';


const Home = () => {
    const { t } = useTranslation();

    return (
        <div className="Home">
            <Helmet>
                <title>Welcome to Razzle</title>
            </Helmet>
            <div className="Home-header">
                <img src={logo} className="Home-logo" alt="logo" />
                <h2>Welcome to Razzle</h2>
            </div>
            <h3>{t('Hello world!')}</h3>
            <p className="Home-intro">
                To get started, add routes to <code>src/configuration/routes.js</code> or{' '}
                edit <code>src/views/Home/index.js</code> and save to reload.
            </p>
            <ul className="Home-resources">
                <li>
                    <a className={styles['special-link']} href="https://github.com/jaredpalmer/razzle">Docs</a>
                </li>
                <li>
                    <a className={styles['special-link']} href="https://github.com/jaredpalmer/razzle/issues">Issues</a>
                </li>
            </ul>
            <ul className="Home-resources">
                <LanguageSwitch />
            </ul>
        </div>
    );
};

export default withView()(Home);
