import React from 'react'
import Card from 'material-ui/Card'

import GetMovies from './get_movies/GetMovies'
import Loading from './Loading'
import MovieSelection from './movie_selection/MovieSelection'
import SchedulesList from './schedules_list/SchedulesList'

export default class Index extends React.Component {

    state = {
        error: null,
        isLoading: false,
        movies: null,
        schedules: null
    }

    render() {
        return (
            <Card
                containerStyle={{
                    padding: '32px'
                }}
                style={{
                    maxWidth: '960px',
                    margin: 'auto',
                }}
            >
                {this.getContent()}
            </Card>
        )
    }

    getContent() {
        const {error, isLoading, movies, schedules} = this.state

        if (error) {
            return <div>{error.toString()}</div>
        }
        if (isLoading) {
            return this.loading()
        }
        if (schedules) {
            return this.schedulesList(schedules)
        }
        if (movies) {
            return this.moviesList(movies)
        }
        return this.getMovies()
    }


    loading() {
        return <Loading text="Loading"/>
    }


    getMovies() {
        return <GetMovies
            onError={error => this.setState({error})}
            onLoading={() => this.setState({isLoading: true})}
            onMovies={movies =>
                this.setState({
                    movies: movies.sortBy(movie => movie.get('title')).toList(),
                    isLoading: false
                })
            }
        />
    }

    moviesList(movies) {
        return <MovieSelection
            movies={movies}
            onLoading={() => this.setState({isLoading: true})}
            onSchedules={schedules => this.setState({schedules, isLoading: false})}
        />
    }

    schedulesList(schedules) {
        return <SchedulesList schedules={schedules}/>
    }
}