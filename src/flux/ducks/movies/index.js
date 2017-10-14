import axios from 'axios'
import Immutable from 'immutable'

import {
    API_URL_DEV,
    API_URL_PROD,
} from './constants'


const FETCH_MOVIES_ERROR = 'movie-marathon/movies/FETCH_MOVIES_ERROR'
const FETCH_MOVIES_LOADING = 'movie-marathon/movies/FETCH_MOVIES_LOADING'
const FETCH_MOVIES_SUCCESS = 'movie-marathon/movies/FETCH_MOVIES_SUCCESS'

const initialState = Immutable.fromJS({
    error: '',
    isLoading: false,
    movies: [],
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
        default:
            return state
    }
}

export function fetchMovies(lat, lng, date) {
    return dispatch => {
        dispatch(fetchMoviesLoading())
        const config = {
            params: {
                lat,
                lng,
                startDate: date.format('YYYY-MM-DD')
            }
        }
        const url = process.env.NODE_ENV === 'production' ?
            API_URL_PROD :
            API_URL_DEV
        axios.get(url, config)
            .then(resp => dispatch(fetchMoviesSuccess(resp.data)))
            .catch(() => dispatch(fetchMoviesError()))
    }
}

function fetchMoviesError() {
    return {
        type: FETCH_MOVIES_ERROR,
    }
}

function fetchMoviesLoading() {
    return {
        type: FETCH_MOVIES_LOADING,
    }
}

function fetchMoviesSuccess(movies) {
    return {
        type: FETCH_MOVIES_SUCCESS,
        payload: movies,
    }
}

export function sortedMovies(state) {
    return state.get('movies').sortBy(movie => movie.get('title')).toList()
}