import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import React from 'react'

import AddressForm from 'components/get_movies/AddressForm'
import {actions as moviesActions} from 'flux/ducks/movies'
import Header from 'components/Header'


export class UnconnectedGetMovies extends React.PureComponent {
    static propTypes = {
        error: PropTypes.string.isRequired,
        fetchMovies: PropTypes.func.isRequired,
    }

    render() {
        if (this.props.error) {
            return <div>{this.props.error.toString()}</div>
        }
        return (
            <div>
                <Header
                    description="This app helps plan movie marathons at Canadian and US movie theatres."
                    titleText="Movie Marathon"
                />
                <AddressForm
                    onSubmit={this.onSubmit}
                />
            </div>
        )
    }

    onSubmit = (lat, lng, date) => {
        this.props.fetchMovies(lat, lng, date)
    }
}

function mapStateToProps(state) {
    const movieState = state.get('movies')
    return {
        error: movieState.get('error'),
    }
}

const mapDispatchToProps = {
    fetchMovies: moviesActions.fetchMovies,
}

export default connect(mapStateToProps, mapDispatchToProps)(UnconnectedGetMovies)