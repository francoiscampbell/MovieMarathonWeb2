import Immutable from 'immutable'
import PropTypes from 'prop-types'
import React from 'react'

import {generateSchedules} from '../../scheduling/ScheduleGenerator'
import SubmitCheckboxList from './SubmitCheckboxList'


export default class MovieSelection extends React.PureComponent {
    static propTypes = {
        movies: PropTypes.instanceOf(Immutable.List),
        onLoading: PropTypes.func,
        onSchedules: PropTypes.func
    }

    onSubmit = (selectedIndices) => {
        this.props.onLoading()
        const selectedMovies = selectedIndices.map(index => {
            return this.props.movies.get(index)
        }).toList()
        this.props.onSchedules(generateSchedules(selectedMovies))
    }

    render() {
        if (this.props.movies.size === 0) {
            return <h1>No movies found near that location</h1>
        }
        const titles = this.props.movies.map(movie => movie.get('title')).toList()
        return (
            <SubmitCheckboxList
                items={titles}
                onSubmit={this.onSubmit}
                sort={true}
            />
        )
    }
}