import React from 'react';
import { Container } from 'reactstrap';
import { connect } from 'react-redux';

import withView from 'decorators/withView';

const ParrotsList = ({ parrots }) => (
    <Container>
        <h1>Here are your parrots!</h1>
        <ul>
            {parrots.map((parrot) => (
                <li key={parrot.id}>
                    <a href={parrot.link}>{parrot.name}</a>
                </li>
            ))}
        </ul>
    </Container>
);

const mapStateToProps = (state) => ({
    parrots: state.parrots.parrots,
});

const ParrotsListConnector = connect(
    mapStateToProps,
)(ParrotsList);

export default withView()(ParrotsListConnector);
