import * as Immutable from 'immutable'
import * as React from 'react'
import axios from 'axios'
import {
    Movie,
    Schedule
} from "../../../data_model/Movie"

import * as styles from './styles.scss'
import {generateSchedules} from "../../../scheduling/ScheduleGenerator"

interface SchedulesListProps {
    schedules: Immutable.List<Schedule>
}

interface SchedulesListState {
    imageUrls: Immutable.Map<Movie, string>,
    imageUrlsToFetch: number
}

export default class SchedulesList extends React.PureComponent<SchedulesListProps, SchedulesListState> {
    state = {
        imageUrls: Immutable.Map<Movie, string>(),
        imageUrlsToFetch: -1
    }

    render() {
        if (this.state.imageUrlsToFetch === -1) {
            this.fetchImageUrls()
        }
        const items = this.props.schedules.map((schedule, index) => {
            const movies = schedule.get('movies').map((movie, index) => {
                const delay = schedule.getIn(['delays', index])
                const overlapOrDelay = delay < 0 ? 'Overlap' : 'Delay'
                const delayOrOverlapText = delay ? <p>{overlapOrDelay} of {delay.humanize()}</p> : null
                return (
                    <div>
                        <img
                            className={styles.moviePoster}
                            src={this.state.imageUrls.get(movie)}
                        />
                        <span className={styles.movieTitle}>{movie.get('title')}</span>
                        <span className={styles.showtime}>{movie.get('showtime').toString()}</span>
                        {delayOrOverlapText}
                    </div>
                )
            })
            return (
                <div>
                    <h2>Schedule {index + 1} at {schedule.getIn(['theatre', 'name'])}:</h2>
                    {movies}
                </div>
            )
        })

        const colon = this.props.schedules.size == 0 ? "schedules" : "schedules:"
        return (
            <div>
                <h1>Generated {this.props.schedules.size} {colon}</h1>
                {items}
                <span>
                    Movie posters from <a href="https://www.themoviedb.org">TMDb</a>
                </span>
            </div>
        )
    }

    fetchImageUrls() {
        const movies = this.props.schedules.first().get('movies')
        this.setState({imageUrlsToFetch: movies.size})
        movies.forEach(movie => {
            const config = {
                params: {
                    query: movie.get('title'),
                    language: movie.get('titleLang'),
                    year: movie.get('releaseYear'),
                }
            }
            axios.get('/tmdb/3/search/movie', config)
                .then(resp => {
                    if (resp.data.results[0]) {
                        const imageUrl = `/tmdbimg/t/p/w154/${resp.data.results[0].poster_path}`
                        this.setState({
                            imageUrls: this.state.imageUrls.set(movie, imageUrl),
                            imageUrlsToFetch: this.state.imageUrlsToFetch - 1
                        })
                    } else {
                        this.setState({
                            imageUrlsToFetch: this.state.imageUrlsToFetch - 1
                        })
                    }
                })
                .catch(console.dir)
        })
    }
}