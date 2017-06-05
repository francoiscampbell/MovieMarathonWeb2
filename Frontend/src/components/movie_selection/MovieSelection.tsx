import * as React from 'react'
import {Movie} from '../../data_model/Movie'
import {reorganizeMoviesIntoModel} from '../../scheduling/ScheduleGenerator'
import SubmitCheckboxList, {ListItem} from './SubmitCheckboxList'

interface MovieSelectionProps {
    movies: Movie[]
}

interface MovieSelectionState {

}

export default class MovieSelection extends React.Component<MovieSelectionProps, MovieSelectionState> {
    render() {
        if (this.props.movies.length === 0) {
            return <h1>No movies found near that location</h1>
        }
        console.dir(reorganizeMoviesIntoModel(this.props.movies))
        const titles = this.props.movies.map(movie => {
            movie.toString = function () {
                return this.title
            }
            return new ListItem(movie, movie.title)
        })
        return <SubmitCheckboxList
            items={titles}
            onSubmit={console.dir}
        />
    }
}