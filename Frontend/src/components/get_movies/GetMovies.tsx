import * as Immutable from 'immutable'
import * as React from 'react'
import axios from 'axios'

import AddressForm from './AddressForm'
import Header from '../Header'
import {LatLng} from '../../data_model/LatLng'
import {Movie} from '../../data_model/Movie'

interface GetMoviesProps {
    onLoading: () => void
    onMovies: (action: Immutable.Map<string, Movie>) => void
}

export default function GetMovies({onLoading, onMovies}: GetMoviesProps) {
    const onGeocodeSuccess = (latLng: LatLng) => {
        const config = {
            params: {
                lat: latLng.lat,
                lng: latLng.lng
            }
        }
        onLoading()
        axios.get('/movies', config)
            .then(resp => onMovies(Immutable.fromJS(resp.data)))
            .catch(error => console.log(error))
    }

    return (
        <div>
            <Header
                description="This app helps plan movie marathons at Canadian and US movie theatres."
                titleText="Movie Marathon"
            />
            <div>Enter your address:</div>
            <AddressForm
                onGeocodeSuccess={onGeocodeSuccess}
            />
        </div>
    )
}