import * as Immutable from 'immutable'
import * as React from 'react'

import {Movie} from '../../data_model/Movie'
import {getAvailableTheatres} from '../../scheduling/ScheduleGenerator'
import SubmitCheckboxList, {ListItem} from './SubmitCheckboxList'


interface MovieSelectionProps {
    movies: Immutable.Map<string, Movie>
}

export default function MovieSelection({movies}: MovieSelectionProps) {
    const onSubmit = (selectedMovies: Immutable.Map<string, Movie>) => {
        const availableTheatres = getAvailableTheatres(selectedMovies)
        console.dir(availableTheatres.toJS())
        availableTheatres.forEach(theatre => {

        })
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