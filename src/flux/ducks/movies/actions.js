export const FETCH_MOVIES = 'movie-marathon/movies/FETCH_MOVIES'
export const FETCH_MOVIES_ERROR = 'movie-marathon/movies/FETCH_MOVIES_ERROR'
export const FETCH_MOVIES_LOADING = 'movie-marathon/movies/FETCH_MOVIES_LOADING'
export const FETCH_MOVIES_SUCCESS = 'movie-marathon/movies/FETCH_MOVIES_SUCCESS'
export const SELECT_MOVIES = 'movie-marathon/movies/SELECT_MOVIES'


export const fetchMovies = (lat, lng, date) => ({
    type: FETCH_MOVIES,
    payload: {
        lat,
        lng,
        date,
    }
})

export const fetchMoviesError = () => ({
    type: FETCH_MOVIES_ERROR,
})

export const fetchMoviesLoading = () => ({
    type: FETCH_MOVIES_LOADING,
})

export const fetchMoviesSuccess = movies => ({
    type: FETCH_MOVIES_SUCCESS,
    payload: movies,
})

export const selectMovies = selectedMovies => ({
    type: SELECT_MOVIES,
    payload: selectedMovies,
})
