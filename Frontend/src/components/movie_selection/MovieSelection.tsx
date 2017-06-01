import * as React from 'react'
import {Movie} from '../../interfaces/Movie'
import SubmitCheckboxList from './SubmitCheckboxList'

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
        const titles = this.props.movies.map(movie => {
            return movie.title
        })
        return <SubmitCheckboxList
            items={titles}
            onSubmit={console.dir}
        />
    }
}