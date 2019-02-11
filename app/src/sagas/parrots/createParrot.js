import { push } from 'connected-react-router';
import { takeEvery, put } from 'redux-saga/effects';

import api from 'services/api';

const CREATE_PARROT = 'CREATE_PARROT';

export const createParrot = (name, link) => ({
    type: CREATE_PARROT,
    name,
    link,
});

function* createParrotSaga(createParrotAction) {
    try {
        const { name, link } = createParrotAction;
        yield api.parrots.list.post(null, { name, link });

        yield put(push('/parrots'));
    } catch (e) {
        console.log('Something went wrong!');
    }
}

export default function* createParrotWatcher() {
    yield takeEvery(CREATE_PARROT, createParrotSaga);
}
