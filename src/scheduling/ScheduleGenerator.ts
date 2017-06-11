import * as Immutable from 'immutable'

import {Movie, Theatre} from '../data_model/Movie'


export function getAvailableTheatres(movies: Immutable.Map<string, Movie>): Immutable.Map<string, Theatre> {
    return reorganizeMoviesIntoModel(movies)
        .filter(t => t.get('movies').size === movies.size)
        .toMap()
}

export function generateSchedule(theatre: Theatre) {

}

function reorganizeMoviesIntoModel(movies: Immutable.Map<string, Movie>): Immutable.Map<string, Theatre> {
    return movies.reduce((reduction, movie) => {
        const splitMovie = splitMovieByTheatre(movie)
        return splitMovie.reduce((reduction, theatre, theatreId) => {
            if (reduction.has(theatreId)) {
                const currentMovies = reduction.getIn([theatreId, 'movies'], Immutable.List())
                const newMovies = currentMovies.concat(theatre.get('movies'))
                return reduction.setIn([theatreId, 'movies'], newMovies)
            } else {
                return reduction.set(theatreId, theatre)
            }
        }, reduction)
    }, Immutable.Map<string, Theatre>())
}

function splitMovieByTheatre(movie: Movie): Immutable.Map<string, Theatre> {
    return movie.get('showtimes').reduce((reduction, showtime) => {
        const theatreId = showtime.getIn(['theatre', 'id'])

        if (!reduction.has(theatreId)) {
            const theatre = showtime.get('theatre')

            const validShowtimes = movie.get('showtimes')
                .filter(s => s.getIn(['theatre', 'id']) === theatreId)
                .map(s => s.delete('theatre'))
            const currentMovies = theatre.get('movies', Immutable.List())
            const newMovies = currentMovies.concat([movie.set('showtimes', validShowtimes)])
            return reduction.set(theatreId, theatre.set('movies', newMovies))
        } else {
            return reduction
        }
    }, Immutable.Map<string, Theatre>())
}
