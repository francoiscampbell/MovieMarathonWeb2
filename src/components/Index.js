import Card from 'material-ui/Card'
import {connect} from 'react-redux'
import React from 'react'

import GetMovies from 'src/components/get_movies/GetMovies'
import MovieSelection from 'src/components/movie_selection/MovieSelection'
import SchedulesList from 'src/components/schedules_list/SchedulesList'
import {sortedMovies} from 'src/flux/ducks/movies'

export class UnconnectedIndex extends React.Component {

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
        return <GetMovies/>
    }


    loading() {
        return <Loading text="Loading"/>
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

function mapStateToProps(state) {
    return {
        movies: sortedMovies(state)
    }
}

export default connect(mapStateToProps)(UnconnectedIndex)