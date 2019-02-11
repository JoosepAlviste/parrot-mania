import { put } from 'redux-saga/effects';

import { receiveParrots } from 'ducks/parrots';
import api from 'services/api';

export default function* fetchUserParrots() {
    try {
        const parrots = yield api.parrots.list.fetch();
        yield put(receiveParrots(parrots));
    } catch (err) {
        console.error('Something went wrong!');
    }
}
