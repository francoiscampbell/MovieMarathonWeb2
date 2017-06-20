import * as Immutable from 'immutable'
import * as React from 'react'

import GetMovies from './get_movies/GetMovies'
import MovieSelection from './movie_selection/MovieSelection'
import SchedulesList from './schedules_list/SchedulesList'
import {Movie, Schedule} from '../data_model/Movie'


interface IndexState {
    isLoading: boolean
    movies: Immutable.List<Movie>,
    schedules: Immutable.List<Schedule>
}

export default class Index extends React.Component<undefined, IndexState> {

    state = {
        isLoading: false,
        movies: null,
        schedules: null
    }

    render() {
        const {isLoading, movies, schedules} = this.state

        if (isLoading) {
            return Index.loading()
        }
        if (schedules) {
            return Index.schedulesList(schedules)
        }
        if (movies) {
            return this.moviesList(movies)
        }
        return this.getMovies()
    }


    private static loading(): JSX.Element {
        return <span>Loading</span>
    }


    private getMovies(): JSX.Element {
        return <GetMovies
            onLoading={() => this.setState({isLoading: true})}
            onMovies={movies => this.setState({movies, isLoading: false})}
        />
    }

    private moviesList(movies: Immutable.List<Movie>): JSX.Element {
        return <MovieSelection
            movies={movies}
            onLoading={() => this.setState({isLoading: true})}
            onSchedules={schedules => this.setState({schedules, isLoading: false})}
        />
    }

    private static schedulesList(schedules: Immutable.List<Schedule>): JSX.Element {
        return <SchedulesList schedules={schedules} />
    }
}