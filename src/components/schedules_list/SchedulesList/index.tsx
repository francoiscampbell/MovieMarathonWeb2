import * as Immutable from 'immutable'
import * as React from 'react'
import axios from 'axios'
import {
    Movie,
    Schedule
} from "../../../data_model/Movie"
import Timeline from 'react-visjs-timeline'

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

        const options = {
            format: {
                minorLabels: {
                    minute: 'h:mma',
                    hour: 'ha'
                }
            },
            orientation: 'both',
            showCurrentTime: true,
            showMajorLabels: true,
            stack: false,
            zoomKey: 'ctrlKey'
        }

        const items = this.props.schedules.flatMap((schedule, index) => {
            return schedule.get('movies').map(movie => {
                const startTime = movie.get('showtime')
                const endTime = startTime.clone().add(movie.get('runTime'))
                const title = movie.get('title')
                return {
                    content: title,
                    end: endTime,
                    group: index + 1,
                    start: startTime,
                    type: 'range'
                }
            })
        })

        const groups = this.props.schedules.map((schedule, index) => {
            return {
                id: index + 1,
                content: schedule.getIn(['theatre', 'name'])
            }
        }).toJS()


        const colon = this.props.schedules.size > 0 ? ':' : ''
        return (
            <div>
                <h1>Generated {this.props.schedules.size} schedules{colon}</h1>
                <Timeline
                    groups={groups}
                    items={items.toJS()}
                    options={options}
                />
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