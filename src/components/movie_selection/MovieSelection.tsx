import * as Immutable from 'immutable'
import * as React from 'react'

import {Movie, Schedule} from '../../data_model/Movie'
import {generateSchedules} from '../../scheduling/ScheduleGenerator'
import SubmitCheckboxList from './SubmitCheckboxList'


interface MovieSelectionProps {
    movies: Immutable.List<Movie>,
    onLoading: () => void,
    onSchedules: (schedules: Immutable.List<Schedule>) => void
}

export default function MovieSelection({movies, onLoading, onSchedules}: MovieSelectionProps) {
    const onSubmit = (selectedIndices: Immutable.List<number>) => {
        onLoading()
        const selectedMovies = selectedIndices.map(index => {
            return movies.get(index)
        }).toList()
        onSchedules(generateSchedules(selectedMovies))
    }

    if (movies.size === 0) {
        return <h1>No movies found near that location</h1>
    }
    const titles = movies.map(movie => movie.get('title')).toList()
    return (
        <SubmitCheckboxList
            items={titles}
            onSubmit={onSubmit}
            sort={true}
        />
    )
}