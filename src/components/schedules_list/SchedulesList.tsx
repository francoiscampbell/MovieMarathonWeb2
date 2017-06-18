import * as Immutable from 'immutable'
import * as React from 'react'
import {Schedule} from "../../data_model/Movie"

interface SchedulesListProps {
    schedules: Immutable.List<Schedule>
}

export default function SchedulesList({schedules}: SchedulesListProps) {
    const items = schedules.map((schedule, index) => {
        const movies = schedule.get('movies').map(movie => {
            return (
                <div>
                    <p>{movie.get('title')}</p>
                    <p>{movie.get('showtime').toString()}</p>
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

    const colon = schedules.size == 0 ? "schedules." : "schedules:"
    return (
        <div>
            <h1>Generated {schedules.size} {colon}</h1>
            {items}
        </div>
    )
}