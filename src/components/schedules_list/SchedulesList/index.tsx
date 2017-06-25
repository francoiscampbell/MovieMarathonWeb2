import * as Immutable from 'immutable'
import * as React from 'react'

import axios from 'axios'
import * as humanizeDuration from 'humanize-duration'
import {
    Movie,
    Schedule
} from "../../../data_model/Movie"
import Timeline from 'react-visjs-timeline'


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
        imageUrlsToFetch: this.props.schedules.size > 0 ? this.props.schedules.first().get('movies').size : 0
    }

    componentWillMount() {
        this.fetchImageUrls()
    }

    render() {
        const visOptions = {
            format: {
                minorLabels: {
                    minute: 'h:mma',
                    hour: 'ha'
                }
            },
            orientation: 'both',
            showCurrentTime: false,
            showMajorLabels: true,
            stack: false,
            tooltip: {
                followMouse: true
            },
            type: 'range',
            verticalScroll: true,
            zoomKey: 'ctrlKey'
        }

        const items = this.props.schedules.flatMap((schedule, scheduleIndex) => {
            return schedule.get('movies').map((movie, movieIndex) => {
                const startTime = movie.get('showtime')
                const runTime = movie.get('runTime')
                const endTime = startTime.clone().add(runTime)
                const delay = schedule.getIn(['delays', movieIndex])
                const delayHtml = delay ? `<div>Delay until next movie: ${humanizeDuration(delay)}</div>` : ''

                const title = movie.get('title')
                const theatre = schedule.getIn(['theatre', 'name'])
                const tooltip = `
                    <div>
                        <div><h3>${title}</h3></div>
                        <div><h4>${theatre}</h4></div>
                        <div>Start time: ${startTime.format('dddd MMMM D YYYY, h:mm a')}</div> 
                        <div>Run time: ${humanizeDuration(runTime)}</div> 
                        <div>End time: ${endTime.format('dddd MMMM D YYYY, h:mm a')}</div> 
                        ${delayHtml}
                    </div>
                `
                return {
                    content: title,
                    end: endTime,
                    group: scheduleIndex + 1,
                    start: startTime,
                    title: tooltip
                }
            })
        })

        const groups = this.props.schedules.map((schedule, index) => {
            return {
                id: index + 1,
                content: schedule.getIn(['theatre', 'name'])
            }
        }).toJS()


        const hasSchedules = this.props.schedules.size > 0
        const colon = hasSchedules ? ':' : ''
        const timeline = hasSchedules ? (
            <Timeline
                groups={groups}
                items={items.toJS()}
                options={visOptions}
            />) : null
        const attribution = hasSchedules ? (
            <span>
                 Movie posters from <a href="https://www.themoviedb.org">TMDb</a>
             </span>
        ) : null
        return (
            <div>
                <h1>Generated {this.props.schedules.size} schedules{colon}</h1>
                {timeline}
                {attribution}
            </div>
        )
    }

    fetchImageUrls() {
        if (this.state.imageUrlsToFetch === 0) {
            return
        }

        this.props.schedules
            .first()
            .get('movies')
            .forEach(movie => {
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
                                imageUrls: this.state.imageUrls.set(movie, imageUrl)
                            })
                        }
                        this.setState({
                            imageUrlsToFetch: this.state.imageUrlsToFetch - 1
                        })
                    })
                    .catch(console.dir)
            })
    }
}