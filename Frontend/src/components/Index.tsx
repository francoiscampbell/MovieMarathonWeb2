import * as React from 'react'
import {Movie} from '../data_model/Movie'
import GetMovies from './get_movies/GetMovies'
import MovieSelection from './movie_selection/MovieSelection'

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
        return this.getMovies()
    }


    private getMovies(): JSX.Element {
        return <GetMovies
            onLoading={() => this.setState({isLoadingMovies: true})}
            onMovies={(movies) => this.setState({movies, isLoadingMovies: false})}
        />
    }


    private static loading(): JSX.Element {
        return <span>Loading</span>
    }

    private static moviesList(movies: Movie[]): JSX.Element {
        return <MovieSelection movies={movies}/>
    }
}