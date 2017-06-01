import * as React from 'react'
import axios from 'axios'

import AddressForm from './AddressForm'
import Header from './Header'
import {LatLng} from '../interfaces/LatLng'
import {Movie} from '../interfaces/Movie'

interface IndexState {
    isLoadingMovies: boolean
    movies: Movie[]
}

export default class Index extends React.Component<undefined, IndexState> {

    state = {
        isLoadingMovies: false,
        movies: null
    }

    render() {
        const {isLoadingMovies, movies} = this.state

        if (isLoadingMovies) {
            return Index.loading()
        }
        if (movies) {
            return Index.moviesList(movies)
        }
        return this.index()
    }


    private index(): JSX.Element  {
        return (
            <div>
                <Header
                    description="This app helps plan movie marathons at Canadian and US movie theatres."
                    titleText="Movie Marathon"
                />
                <div>Enter your address:</div>
                <AddressForm
                    onGeocodeSuccess={this.onGeocodeSuccess}
                />
            </div>
        )

    }

    private onGeocodeSuccess = (latLng: LatLng) => {
        const config = {
            params: {
                lat: latLng.lat,
                lng: latLng.lng
            }
        }
        this.setState({isLoadingMovies: true})
        axios.get('/movies', config)
            .then(response => this.setState({
                isLoadingMovies: false,
                movies: response.data
            }))
            .catch(error => console.log(error))
    }

    private static loading(): JSX.Element {
        return <span>Loading</span>
    }

    private static moviesList(movies: Movie[]): JSX.Element  {
        const elements = movies.map(movie=> {
            return <li>{movie.title}</li>
        })
        return (
            <ul>
                {elements}
            </ul>
        )
    }
}