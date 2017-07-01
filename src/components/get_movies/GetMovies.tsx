import * as Immutable from "immutable"
import * as React from "react"
import axios from "axios"
import * as moment from "moment"

import AddressForm from "./AddressForm"
import Header from "../Header"
import {Movie} from "../../data_model/Movie"

interface GetMoviesProps {
    onLoading: () => void
    onMovies: (action: Immutable.List<Movie>) => void
}

export default function GetMovies({onLoading, onMovies}: GetMoviesProps) {
    const onSubmit = (lat: number, lng: number, date: moment.Moment) => {
        const config = {
            params: {
                lat,
                lng,
                startDate: date.format('YYYY-MM-DD')
            }
        }
        const apiVersion = process.env.NODE_ENV === 'production' ?
            'v1.1' : 'mock'
        onLoading()
        axios.get(`/tms/${apiVersion}/movies/showings`, config)
            .then(resp => onMovies(Immutable.fromJS(resp.data)))
            .catch(error => console.log(error))
    }

    return (
        <div>
            <Header
                description="This app helps plan movie marathons at Canadian and US movie theatres."
                titleText="Movie Marathon"
            />
            <AddressForm
                onSubmit={onSubmit}
            />
        </div>
    )
}