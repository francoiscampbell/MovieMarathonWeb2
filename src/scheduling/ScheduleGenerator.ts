import * as Immutable from "immutable"
import * as moment from "moment"


import {Movie, Schedule, Theatre} from "../data_model/Movie"


export function generateSchedules(movies: Immutable.List<Movie>): Immutable.List<Schedule> {
    const sortByDelay = true


    const processedMovies = processMovies(movies)
    const availableTheatres = getAvailableTheatres(processedMovies)

    const possibleSchedules = Immutable.List<Schedule>().withMutations(possibleSchedules => {
        availableTheatres.forEach(theatre => {
            generateSchedule(
                theatre,
                processedMovies,
                moment().subtract(1, 'months'),
                possibleSchedules,
                Immutable.List<Movie>().asMutable()
            )
        })
    })

    if (sortByDelay) {
        return sortSchedulesByDelay(possibleSchedules)
    }
    return possibleSchedules
}

function processMovies(movies: Immutable.List<Movie>): Immutable.List<Movie> {
    return movies.map(movie => {
        return movie
            .set('runTime', moment.duration(movie.get('runTime')))
            .set('showtimes', movie
                .get('showtimes')
                .map(s => s.set('dateTime', moment(s.get('dateTime'))))
                .sortBy(s => s.get('dateTime')))
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
                          availableMovies: Immutable.List<Movie>,
                          startTime: moment.Moment,
                          possibleSchedules: Immutable.List<Schedule>, //mutable
                          currentPermutation: Immutable.List<Movie>): Immutable.List<Schedule> { //mutable
    if (availableMovies.size == 0 && !currentPermutation.isEmpty()) {
        //end condition for recursive algorithm. check for empty to avoid generating a schedule if the list of desired movies is empty at the start
        const schedule = makeSchedule(theatre, listCopy(currentPermutation))
        if (validateSchedule(schedule)) {
            possibleSchedules.unshift(schedule)
        }
        return
    }
    availableMovies.forEach(movie => {
        let showtime
        let nextAvailableStartTime = startTime
        while ((showtime = findNextShowtimeForMovie(movie, nextAvailableStartTime)) != null) {
            currentPermutation.push(movie.delete('showtimes').set('showtime', showtime))
            nextAvailableStartTime = showtime.clone().add(movie.get('runTime'))
            generateSchedule(theatre, availableMovies.shift(), nextAvailableStartTime, possibleSchedules, currentPermutation)
            currentPermutation.pop()
        }
    })
}

function findNextShowtimeForMovie(movie: Movie, nextAvailableStartTime: moment.Moment): moment.Moment {
    return movie.get('showtimes')
        .map(s => s.get('dateTime'))
        .find(showtime => validateShowtime(showtime, nextAvailableStartTime))
}

function validateShowtime(showtime: moment.Moment, nextAvailableStartTime: moment.Moment) {
    return showtime.isAfter(nextAvailableStartTime) //add more validation logic
}

function makeSchedule(theatre: Theatre, movies: Immutable.List<Movie>): Schedule {
    const sortedMovies = movies.sortBy(m => m.get('showtime')).toList()

    let previousMovie = sortedMovies.first()
    let previousMovieShowtime: moment.Moment = previousMovie.get('showtime').clone()

    const totalDelay = moment.duration(0)
    const delays = sortedMovies.shift().map(movie => {
        const showtime: moment.Moment = movie.get('showtime').clone()
        const delay = showtime.diff(previousMovieShowtime.add(previousMovie.get('runTime')))
        const delayDuration = moment.duration(delay)

        previousMovie = movie
        previousMovieShowtime = showtime

        totalDelay.add(delayDuration)
        return delayDuration
    })

    return Immutable.Map({
        theatre,
        movies: sortedMovies,
        delays,
        totalDelay
    })
}

function validateSchedule(schedule: Schedule): boolean {
    return true
}

function sortSchedulesByDelay(schedules: Immutable.List<Schedule>): Immutable.List<Schedule> {
    return schedules
        .sort((a, b) => {
            const totalDelayA = a.get('totalDelay')
            const totalDelayB = b.get('totalDelay')
            const diff = totalDelayA - totalDelayB
            if (diff !== 0) {
                return diff
            }

            const startTimeA = a.getIn(['movies', 0, 'showtime'])
            const startTimeB = b.getIn(['movies', 0, 'showtime'])
            if (startTimeA.isBefore(startTimeB)) {
                return -1
            }
            if (startTimeA.isAfter(startTimeB)) {
                return 1
            }
            return 0
        })
        .toList()
}

function listCopy<T>(list: Immutable.List<T>): Immutable.List<T> {
    return list.map(item => item).toList()
}

