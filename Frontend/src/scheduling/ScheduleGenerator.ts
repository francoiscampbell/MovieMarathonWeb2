import * as Immutable from 'immutable'

import {Movie, Theatre} from '../data_model/Movie'


export function reorganizeMoviesIntoModel(movies: Movie[]): Theatre[] {
    let allTheatres = Immutable.Map<String, Theatre>()

    for (const movie of movies) {
        const splitMovie = splitMovieByTheatre(movie)
        splitMovie.forEach((value, key) => {
            if (allTheatres.has(key)) {
                allTheatres.get(key).movies.push(...value.movies)
            } else {
                allTheatres = allTheatres.set(key, value)
            }
        })
    }

    return allTheatres.toJS()
}

function splitMovieByTheatre(movie: Movie): Immutable.Map<String, Theatre> {
    let allTheatres = Immutable.Map<String, Theatre>()

    for (const showtime of movie.showtimes) {
        const theatreId = showtime.theatre.id

        if (!allTheatres.has(theatreId)) {
            const theatre = showtime.theatre
            allTheatres = allTheatres.set(theatreId, theatre)

            const validShowtimes = Immutable.fromJS(movie.showtimes)
                .filter(s => s.getIn(['theatre', 'id']) === theatreId)
                .map(s => s.delete('theatre'))
            if (!theatre.movies) {
                theatre.movies = []
            }
            theatre.movies.push(
                Immutable.fromJS(movie)
                    .set('showtimes', validShowtimes)
                    .toJS()
            )
        }
    }

    return allTheatres
}
