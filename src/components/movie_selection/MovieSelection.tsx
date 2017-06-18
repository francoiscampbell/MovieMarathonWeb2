import * as Immutable from 'immutable'
import * as React from 'react'

import {Movie, Schedule} from '../../data_model/Movie'
import {generateSchedules} from '../../scheduling/ScheduleGenerator'
import SubmitCheckboxList, {ListItem} from './SubmitCheckboxList'


interface MovieSelectionProps {
    movies: Immutable.List<Movie>,
    onLoading: () => void,
    onSchedules: (schedules: Immutable.List<Schedule>) => void
}

export default function MovieSelection({movies, onLoading, onSchedules}: MovieSelectionProps) {
    const onSubmit = (selectedMovies: Immutable.List<Movie>) => {
        onLoading()
        onSchedules(generateSchedules(selectedMovies))
    }

    if (movies.size === 0) {
        return <h1>No movies found near that location</h1>
    }
    const titles = movies.map(movie => {
        movie.toString = function () {
            return this.get('title')
        }
        return new ListItem<Movie, string>(movie, movie.toString())
    })
    return (
        <SubmitCheckboxList
            items={titles}
            onSubmit={onSubmit}
            sort={true}
        />
    )
}