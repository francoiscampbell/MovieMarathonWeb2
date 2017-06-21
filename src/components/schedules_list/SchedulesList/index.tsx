import * as Immutable from 'immutable'
import * as React from 'react'
import {Schedule} from "../../../data_model/Movie"

import * as styles from './styles.scss'

interface SchedulesListProps {
    schedules: Immutable.List<Schedule>
}

export default function SchedulesList({schedules}: SchedulesListProps) {
    const items = schedules.map((schedule, index) => {
        const movies = schedule.get('movies').map((movie, index) => {
            const delay = schedule.getIn(['delays', index])
            const overlapOrDelay = delay < 0 ? 'Overlap' : 'Delay'
            const delayOrOverlapText = delay ? <p>{overlapOrDelay} of {delay.humanize()}</p> : null
            return (
                <div>
                    <div>
                        <img src={movie.get('')}/>
                    </div>
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

    const colon = schedules.size == 0 ? "schedules" : "schedules:"
    return (
        <div>
            <h1>Generated {schedules.size} {colon}</h1>
            {items}
        </div>
    )
}