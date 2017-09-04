import Immutable from 'immutable'
import PropTypes from 'prop-types'
import React from 'react'
import axios from 'axios'

import AddressForm from './AddressForm'
import Header from '../Header'


export default class GetMovies extends React.PureComponent {

    static propTypes = {
        onError: PropTypes.func.isRequired,
        onLoading: PropTypes.func.isRequired,
        onMovies: PropTypes.func.isRequired
    }

    onSubmit = (lat, lng, date) => {
        const config = {
            params: {
                lat,
                lng,
                startDate: date.format('YYYY-MM-DD')
            }
        }
        this.props.onLoading()
        const url = process.env.NODE_ENV === 'production' ?
            '//movie-marathon-api.herokuapp.com/v1.1/movies/showings' :
            'http://localhost:3000/v1.1/movies/showings'
        axios.get(url, config)
            .then(resp => this.props.onMovies(Immutable.fromJS(resp.data)))
            .catch(this.props.onError)
    }

    render() {
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
}