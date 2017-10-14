import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import React from 'react'

import AddressForm from 'src/components/get_movies/AddressForm'
import {fetchMovies} from 'src/flux/ducks/movies'
import Header from 'src/components/Header'
import Loading from 'src/components/Loading'


export class UnconnectedGetMovies extends React.PureComponent {

    static propTypes = {
        error: PropTypes.string.isRequired,
        fetchMovies: PropTypes.func.isRequired,
        isLoading: PropTypes.bool.isRequired,
    }

    render() {
        if (this.props.error) {
            return <div>{error.toString()}</div>
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
                    onSubmit={this.props.fetchMovies}
                />
            </div>
        )
    }
}

function mapStateToProps(state) {
    return {
        error: state.get('error'),
        isLoading: state.get('isLoading'),
    }
}

mapDispatchToProps = {
    fetchMovies
}

export default connect(mapStateToProps(), mapDispatchToProps)(UnconnectedGetMovies)