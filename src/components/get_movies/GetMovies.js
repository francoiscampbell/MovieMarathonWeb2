import Immutable from 'immutable'
import PropTypes from 'prop-types'
import React from 'react'
import axios from 'axios'

import AddressForm from './AddressForm'
import Header from '../Header'


export default class GetMovies extends React.PureComponent {

    static propTypes = {
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
        const apiVersion = process.env.NODE_ENV === 'production' ?
            'v1.1' : 'mock'
        this.props.onLoading()
        axios.get(`/tms/${apiVersion}/movies/showings`, config)
            .then(resp => this.props.onMovies(Immutable.fromJS(resp.data)))
            .catch(error => console.log(error))
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