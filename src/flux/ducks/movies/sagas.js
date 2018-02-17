import axios from 'axios'
import {push} from 'react-router-redux'

import {
    API_URL_DEV,
    API_URL_PROD,
} from './constants'
import {
    call,
    put,
    takeEvery
} from 'redux-saga/effects'

import {
    FETCH_MOVIES,
    fetchMoviesError,
    fetchMoviesLoading,
    fetchMoviesSuccess,
    SELECT_MOVIES
} from './actions'


function* fetchMoviesSaga({payload: {lat, lng, date}}) {
    yield put(fetchMoviesLoading())
    const url = process.env.NODE_ENV === 'production' ?
        API_URL_PROD :
        API_URL_DEV
    try {
        const resp = yield call(
            axios.get,
            url,
            {
                params: {
                    lat,
                    lng,
                    startDate: date.format('YYYY-MM-DD'),
                }
            }
        )
        yield put(fetchMoviesSuccess(resp.data))
        yield put(push('/movies'))
    } catch (e) {
        debugger
        yield put(fetchMoviesError())
    }
}

function* selectMoviesSaga() {
    yield put(push('/schedulesSelector'))
}

export default function* moviesSagaWatcher() {
    yield takeEvery(FETCH_MOVIES, fetchMoviesSaga)
    yield takeEvery(SELECT_MOVIES, selectMoviesSaga)
}
