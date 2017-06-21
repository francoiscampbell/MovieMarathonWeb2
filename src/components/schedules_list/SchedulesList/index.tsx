import * as Immutable from 'immutable'
import * as React from 'react'
import {Schedule} from "../../../data_model/Movie"

import * as styles from './styles.scss'

interface SchedulesListProps {
    schedules: Immutable.List<Schedule>
}

interface SchedulesListState {
    imageUrls: Immutable.List<string>
}

export default class SchedulesList extends React.PureComponent<SchedulesListProps, SchedulesListState> {
    state = {
        imageUrls: Immutable.List<string>().setSize(this.props.schedules.size).set(0, '/tmdbimg/t/p/w154/ewVHnq4lUiovxBCu64qxq5bT2lu.jpg')
    }

    render() {
        const items = this.props.schedules.map((schedule, index) => {
            const movies = schedule.get('movies').map((movie, index) => {
                const delay = schedule.getIn(['delays', index])
                const overlapOrDelay = delay < 0 ? 'Overlap' : 'Delay'
                const delayOrOverlapText = delay ? <p>{overlapOrDelay} of {delay.humanize()}</p> : null
                return (
                    <div>
                        <img
                            className={styles.moviePoster}
                            src={this.state.imageUrls.get(index)}
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
            </div>
        )
    }
}