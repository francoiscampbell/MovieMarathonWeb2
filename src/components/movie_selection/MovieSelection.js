import {connect} from 'react-redux'
import {createStructuredSelector} from 'reselect'
import Immutable from 'immutable'
import PropTypes from 'prop-types'
import React from 'react'

import Loading from 'components/Loading'
import SubmitCheckboxList from 'components/movie_selection/SubmitCheckboxList'
import {
    actions as moviesActions,
    selectors as moviesSelectors
} from 'flux/ducks/movies'


export class UnconnectedMovieSelection extends React.PureComponent {
    static propTypes = {
        isLoading: PropTypes.bool.isRequired,
        movies: PropTypes.instanceOf(Immutable.List).isRequired,
        selectMovies: PropTypes.func.isRequired
    }

    onSubmit = selectedIndices => {
        const selectedMovies = selectedIndices.map(index => {
            return this.props.movies.get(index)
        }).toList()
        this.props.selectMovies(selectedMovies)
    }

    render() {
        if (this.props.isLoading) {
            return (
                <Loading>
                    Loading movies
                </Loading>
            )
        }
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

const mapStateToProps = createStructuredSelector({
    isLoading: moviesSelectors.isLoadingSelector,
    movies: moviesSelectors.sortedMoviesSelector
})

const mapDispatchToProps = {
    selectMovies: moviesActions.selectMovies,
}

export default connect(mapStateToProps, mapDispatchToProps)(UnconnectedMovieSelection)