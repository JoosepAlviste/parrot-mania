import React from 'react';
import PropTypes from 'prop-types';
import { Helmet } from 'react-helmet';
import { connect } from 'react-redux';

import SETTINGS from 'settings';
import { applicationSelectors } from 'ducks/application';


const DefaultHeader = ({ activeLanguage, canonical }) => (
    <Helmet titleTemplate="%s - Parrot mania" defaultTitle="Parrot mania">
        <html lang={activeLanguage} />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta charSet="utf-8" />
        <body className="bg-light" />
        <meta name="description" content="Default description" />
        <link rel="canonical" href={`${SETTINGS.SITE_URL}${canonical}`} />
    </Helmet>
);

DefaultHeader.propTypes = {
    activeLanguage: PropTypes.string.isRequired,
    canonical: PropTypes.string.isRequired,
};


const mapStateToProps = (state) => ({
    activeLanguage: applicationSelectors.activeLanguage(state),
});

export default connect(
    mapStateToProps,
)(DefaultHeader);
