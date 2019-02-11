import { combineReducers } from 'redux';

export const RECEIVE_PARROTS = 'parrots/RECEIVE_PARROTS';

const parrotsReducer = (state = [], action) => {
    switch (action.type) {
        case RECEIVE_PARROTS:
            return action.parrots;
        default:
            return state;
    }
};

export default combineReducers({
    parrots: parrotsReducer,
});

// Action creators

export const receiveParrots = (parrots) => ({
    type: RECEIVE_PARROTS,
    parrots,
});
