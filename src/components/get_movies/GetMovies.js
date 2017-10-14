import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import {push} from 'react-router-redux'
import React from 'react'

import AddressForm from 'components/get_movies/AddressForm'
import {fetchMovies} from 'flux/ducks/movies'
import Header from 'components/Header'
import Loading from 'components/Loading'


export class UnconnectedGetMovies extends React.PureComponent {

    static propTypes = {
        error: PropTypes.string.isRequired,
        fetchMovies: PropTypes.func.isRequired,
        goToNextStep: PropTypes.func.isRequired,
        isLoading: PropTypes.bool.isRequired,
    }

    render() {
        if (this.props.error) {
            return <div>{this.props.error.toString()}</div>
        }
        if (this.props.isLoading) {
            return <Loading text="Loading movies"/>
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
        this.props.fetchMovies(lat, lng, date).then(this.props.goToNextStep())
    }
}

function mapStateToProps(state) {
    const movieState = state.get('movies')
    return {
        error: movieState.get('error'),
        isLoading: movieState.get('isLoading'),
    }
}

const mapDispatchToProps = {
    fetchMovies,
    goToNextStep: () => push('/movies')
}

export default connect(mapStateToProps, mapDispatchToProps)(UnconnectedGetMovies)