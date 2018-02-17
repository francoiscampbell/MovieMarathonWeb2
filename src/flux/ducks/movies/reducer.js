import Immutable from 'immutable'


import {
    FETCH_MOVIES_ERROR,
    FETCH_MOVIES_LOADING,
    FETCH_MOVIES_SUCCESS,
    SELECT_MOVIES,
} from './actions'


const initialState = Immutable.fromJS({
    error: '',
    isLoading: false,
    movies: [],
    selectedMovies: [],
})

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case FETCH_MOVIES_ERROR:
            return state.merge({
                error: 'Error fetching movies',
                isLoading: false,
            })
        case FETCH_MOVIES_LOADING:
            return state.merge({
                error: '',
                isLoading: true,
            })
        case FETCH_MOVIES_SUCCESS:
            return state.merge({
                error: '',
                isLoading: false,
                movies: Immutable.fromJS(action.payload)
            })
        case SELECT_MOVIES: {
            return state.merge({
                error: '',
                isLoading: false,
                selectedMovies: action.payload
            })
        }
        default:
            return state
    }
}