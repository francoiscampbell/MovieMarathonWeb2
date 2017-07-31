import Immutable from 'immutable'
import moment from 'moment'


export function generateSchedules(movies) {
    const sortByDelay = true


    const processedMovies = processMovies(movies)
    const availableTheatres = getAvailableTheatres(processedMovies)

    const possibleSchedules = Immutable.List().withMutations(possibleSchedules => {
        availableTheatres.forEach(theatre => {
            const startTime = process.env.NODE_ENV !== 'production' ? moment(0): moment()
            generateSchedule(
                theatre,
                theatre.get('movies'),
                startTime,
                possibleSchedules,
                Immutable.List().asMutable()
            )
        })
    })

    if (sortByDelay) {
        return sortSchedulesByDelay(possibleSchedules)
    }
    return possibleSchedules
}

function processMovies(movies) {
    return movies.map(movie => {
        return movie
            .set('runTime', moment.duration(movie.get('runTime')))
            .set('showtimes', movie
                .get('showtimes')
                .map(s => s.set('dateTime', moment(s.get('dateTime'))))
                .sortBy(s => s.get('dateTime')))
    }).toList()
}

function getAvailableTheatres(movies) {
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
            }, Immutable.Map())
            .reduce((reduction, theatre, theatreId) => {
                if (reduction.has(theatreId)) {
                    const currentMovies = reduction.getIn([theatreId, 'movies'], Immutable.List())
                    const newMovies = currentMovies.concat(theatre.get('movies'))
                    return reduction.setIn([theatreId, 'movies'], newMovies)
                } else {
                    return reduction.set(theatreId, theatre)
                }
            }, reduction)
    }, Immutable.Map())
        .filter(t => t.get('movies').size === movies.size)
        .toMap()
}

function generateSchedule(theatre,
                          availableMovies,
                          startTime,
                          possibleSchedules, //mutable
                          currentPermutation) { //mutable
    if (availableMovies.size === 0 && !currentPermutation.isEmpty()) {
        //end condition for recursive algorithm. check for empty to avoid generating a schedule if the list of desired movies is empty at the start
        const schedule = makeSchedule(theatre, listCopy(currentPermutation))
        if (validateSchedule(schedule)) {
            possibleSchedules.unshift(schedule)
        }
        return
    }
    availableMovies.forEach((movie, movieIndex) => {
        let showtime = startTime
        while ((showtime = findNextShowtimeForMovie(movie, showtime)) !== undefined) {
            currentPermutation.push(movie.delete('showtimes').set('showtime', showtime))
            generateSchedule(
                theatre,
                availableMovies.delete(movieIndex),
                showtime.clone().add(movie.get('runTime')),
                possibleSchedules,
                currentPermutation)
            currentPermutation.pop()
        }
    })
}

function findNextShowtimeForMovie(movie, nextAvailableStartTime) {
    return movie.get('showtimes')
        .map(s => s.get('dateTime'))
        .find(showtime => validateShowtime(showtime, nextAvailableStartTime))
}

function validateShowtime(showtime, nextAvailableStartTime) {
    return showtime.isAfter(nextAvailableStartTime) //add more validation logic
}

function makeSchedule(theatre, movies) {
    const sortedMovies = movies.sortBy(m => m.get('showtime')).toList()

    let previousMovie = sortedMovies.first()
    let previousMovieShowtime = previousMovie.get('showtime').clone()

    const totalDelay = moment.duration(0)
    const delays = sortedMovies.shift().map(movie => {
        const showtime = movie.get('showtime').clone()
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

function validateSchedule(schedule) {
    return true
}

function sortSchedulesByDelay(schedules) {
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

function listCopy(list) {
    return list.map(item => item).toList()
}

