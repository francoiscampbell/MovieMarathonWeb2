import { createSelector } from 'reselect'

import {generateSchedules} from 'scheduling/ScheduleGenerator'


const moviesSelector = state => state.get('movies')

export const isLoadingSelector = state => state.getIn(['movies', 'isLoading'])

export const sortedMoviesSelector = createSelector(
    moviesSelector,
    moviesState => moviesState.get('movies').sortBy(movie => movie.get('title')).toList()
)

export function schedulesSelector(state) {
    return generateSchedules(state.getIn(['movies', 'selectedMovies']))
}