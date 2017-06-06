import * as Immutable from 'immutable'

import {Movie, Theatre} from '../data_model/Movie'


export function getAvailableTheatres(movies: Immutable.Map<String, Movie>): Immutable.Map<String, Theatre> {
    return reorganizeMoviesIntoModel(movies)
        .filter(t => t.get('movies').size === movies.size)
        .toMap()
}

function reorganizeMoviesIntoModel(movies: Immutable.Map<String, Movie>): Immutable.Map<String, Theatre> {
    let allTheatres = Immutable.Map<String, Theatre>()

    movies.forEach(movie => {
        const splitMovie = splitMovieByTheatre(movie)
        splitMovie.forEach((theatre, theatreId) => {
            if (allTheatres.has(theatreId)) {
                const currentMovies = allTheatres.getIn([theatreId, 'movies'], Immutable.List())
                const newMovies = currentMovies.concat(theatre.get('movies'))
                allTheatres = allTheatres.setIn([theatreId, 'movies'], newMovies)
            } else {
                allTheatres = allTheatres.set(theatreId, theatre)
            }
        })
    })

    return allTheatres
}

function splitMovieByTheatre(movie: Movie): Immutable.Map<String, Theatre> {
    let allTheatres = Immutable.Map<String, Theatre>()

    movie.get('showtimes').forEach(showtime => {
        const theatreId = showtime.getIn(['theatre', 'id'])

        if (!allTheatres.has(theatreId)) {
            const theatre = showtime.get('theatre')

            const validShowtimes = movie.get('showtimes')
                .filter(s => s.getIn(['theatre', 'id']) === theatreId)
                .map(s => s.delete('theatre'))
            const currentMovies = theatre.get('movies', Immutable.List())
            const newMovies = currentMovies.concat([movie.set('showtimes', validShowtimes)])
            allTheatres = allTheatres.set(theatreId, theatre.set('movies', newMovies))
        }
    })

    return allTheatres
}
