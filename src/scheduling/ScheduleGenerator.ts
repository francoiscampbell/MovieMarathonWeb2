import * as Immutable from 'immutable'
import * as moment from 'moment'

import {
    Movie,
    Theatre,
    Schedule
} from '../data_model/Movie'


export function generateSchedules(movies: Immutable.List<Movie>): Immutable.List<Schedule> {
    const sortByDelay = true



    const processedMovies = processMovies(movies)
    const availableTheatres = getAvailableTheatres(processedMovies)

    const possibleSchedules = Immutable.List<Schedule>().asMutable()
    const currentPermutation = Immutable.Stack<Movie>().asMutable()
    availableTheatres.forEach(theatre => {
        generateSchedule(theatre, processedMovies.toStack(), moment().subtract(1, 'months'), possibleSchedules, currentPermutation)
    })
    if (sortByDelay) {
        sortSchedulesByDelay(possibleSchedules);
    }
    return possibleSchedules.toList()
}

function processMovies(movies: Immutable.List<Movie>): Immutable.List<Movie> {
    return movies.map(movie => {
        return movie
            .set('runTime', moment.duration(movie.get('runTime')))
            .set('showtimes', movie
                .get('showtimes')
                .map(showtime => {
                    return showtime.set('dateTime', moment(showtime.get('dateTime')))
                }))
    }).toList()
}

function getAvailableTheatres(movies: Immutable.List<Movie>): Immutable.Map<any, Theatre> {
    return movies.reduce((reduction, movie) => {
        return movie.get('showtimes')
            .reduce((reduction, showtime) => {
                const theatreId = showtime.getIn(['theatre', 'id'])
                if (reduction.has(theatreId)) {
                    return reduction
                } else {
                    const theatre = showtime.get('theatre')
                    const validShowtimes = movie.get('showtimes')
                        .filter(s => s.getIn(['theatre', 'id']) === theatreId)
                        .map(s => s.delete('theatre'))
                    const currentMovies = theatre.get('movies', Immutable.List())
                    const newMovies = currentMovies.concat([movie.set('showtimes', validShowtimes)])
                    return reduction.set(theatreId, theatre.set('movies', newMovies))
                }
            }, Immutable.Map<any, Theatre>())
            .reduce((reduction, theatre, theatreId) => {
                if (reduction.has(theatreId)) {
                    const currentMovies = reduction.getIn([theatreId, 'movies'], Immutable.List())
                    const newMovies = currentMovies.concat(theatre.get('movies'))
                    return reduction.setIn([theatreId, 'movies'], newMovies)
                } else {
                    return reduction.set(theatreId, theatre)
                }
            }, reduction)
    }, Immutable.Map<any, Theatre>())
        .filter(t => t.get('movies').size === movies.size)
        .toMap()
}

function generateSchedule(theatre: Theatre,
                          availableMovies: Immutable.Stack<Movie>,
                          startTime: moment.Moment,
                          possibleSchedules: Immutable.List<Schedule>, //mutable
                          currentPermutation: Immutable.Stack<Movie>): Immutable.List<Schedule> { //mutable
    if (availableMovies.size == 0 && !currentPermutation.isEmpty()) {
        //end condition for recursive algorithm. check for empty to avoid generating a schedule if the list of desired movies is empty at the start
        const schedule = makeSchedule(theatre, currentPermutation.toList())
        if (validateSchedule(schedule)) {
            possibleSchedules.unshift(schedule)
        }
        return
    }
    availableMovies.forEach(movie => {
        let showtime
        let nextAvailableStartTime = startTime
        while ((showtime = findNextShowtimeForMovie(movie, nextAvailableStartTime)) != null) {
            availableMovies = availableMovies.shift()
            currentPermutation = currentPermutation.unshift(
                movie.delete('showtimes').set('showtime', showtime))
            nextAvailableStartTime = nextAvailableStartTime.add(movie.get('runTime'))
            generateSchedule(theatre, availableMovies, nextAvailableStartTime, possibleSchedules, currentPermutation)
            currentPermutation.shift()
        }
    })
}

function findNextShowtimeForMovie(movie: Movie, nextAvailableStartTime: moment.Moment): moment.Moment {
    return movie.get('showtimes')
        .map(s => s.get('dateTime'))
        .sort()
        .find(showtime => validateShowtime(showtime, nextAvailableStartTime))
}

function validateShowtime(showtime: moment.Moment, nextAvailableStartTime: moment.Moment) {
    return showtime.isAfter(nextAvailableStartTime) //add more validation logic
}

function makeSchedule(theatre: Theatre, movies: Immutable.List<Movie>) {
    return Immutable.Map({
        theatre,
        movies
    })
}

function validateSchedule(schedule: Schedule): boolean {
    return true
}

function sortSchedulesByDelay(schedules: Immutable.List<Schedule>) {

}
