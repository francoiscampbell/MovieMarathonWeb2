import {connect} from 'react-redux'
import Immutable from 'immutable'
import PropTypes from 'prop-types'
import {push} from 'react-router-redux'
import React from 'react'

import SubmitCheckboxList from 'components/movie_selection/SubmitCheckboxList'
import {
    selectMovies,
    sortedMovies
} from 'flux/ducks/movies'


export class UnconnectedMovieSelection extends React.PureComponent {
    static propTypes = {
        goToNextStep: PropTypes.func.isRequired,
        movies: PropTypes.instanceOf(Immutable.List).isRequired,
        selectMovies: PropTypes.func.isRequired
    }

    onSubmit = selectedIndices => {
        const selectedMovies = selectedIndices.map(index => {
            return this.props.movies.get(index)
        }).toList()
        this.props.selectMovies(selectedMovies)
        this.props.goToNextStep()
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

function mapStateToProps(state) {
    return {
        movies: sortedMovies(state)
    }
}

const mapDispatchToProps = {
    selectMovies,
    goToNextStep: () => push('/schedules')
}

export default connect(mapStateToProps, mapDispatchToProps)(UnconnectedMovieSelection)