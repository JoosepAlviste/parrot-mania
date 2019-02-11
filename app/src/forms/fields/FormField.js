import React, { Fragment } from 'react';
import { connect, getIn } from 'formik';
import { Col, FormGroup, Label, Input, InputGroup, FormText } from 'reactstrap';

import { FieldProps } from 'utils/types';


const MAX_GRID_SIZE = 12;

const FormField = ({ name, label, inputAddonPrepend, inputAddonAppend, formik, check, labelSize, ...props }) => {
    const error = getIn(formik.errors, name, null);
    const value = getIn(formik.values, name, undefined);
    const touched = getIn(formik.touched, name, false);

    let input = (
        <Input
            {...props}
            name={name}
            value={value}
            touched={`${touched}`}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            invalid={!!(touched && error)}
        />
    );

    if (inputAddonPrepend || inputAddonAppend) {
        input = (
            <InputGroup>
                {inputAddonPrepend || null}
                {input}
                {inputAddonAppend || null}
            </InputGroup>
        );
    }

    let inputComponent = (
        <Fragment>
            {input}
            {touched && error ? <FormText color="danger">{error}</FormText> : null}
        </Fragment>
    );
    if (labelSize !== null) {
        inputComponent = (
            <Col md={MAX_GRID_SIZE - labelSize}>
                {inputComponent}
            </Col>
        );
    }

    let labelComponent = null;
    if (label) {
        labelComponent = (
            <Label for={props.id || name} check={check} md={labelSize}>
                {label}
            </Label>
        );
    }

    return (
        <FormGroup row check={check}>
            {labelComponent}
            {inputComponent}
        </FormGroup>
    );
};

FormField.propTypes = FieldProps.props;
FormField.defaultProps = FieldProps.defaults;

export default connect(FormField);
