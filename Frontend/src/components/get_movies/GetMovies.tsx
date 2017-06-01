import * as React from 'react'
import axios from 'axios'

import AddressForm from './AddressForm'
import Header from '../Header'
import {LatLng} from '../../interfaces/LatLng'

interface GetMoviesProps {
    onLoading: () => void
    onMovies: (Array) => void
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
            .then(resp => onMovies(resp.data))
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