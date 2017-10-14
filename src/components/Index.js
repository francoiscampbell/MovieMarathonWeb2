import Card from 'material-ui/Card'
import {ConnectedRouter} from 'react-router-redux'
import React from 'react'
import {Route} from 'react-router-dom'

import GetMovies from 'components/get_movies/GetMovies'
import history from 'history'
import MovieSelection from 'components/movie_selection/MovieSelection'
import SchedulesList from 'components/schedules_list/SchedulesList'

export default function Index() {
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
            <ConnectedRouter history={history}>
                <div>
                    <Route
                        component={GetMovies}
                        exact
                        path="/"
                    />
                    <Route
                        component={MovieSelection}
                        path="/movies"
                    />
                    <Route
                        component={SchedulesList}
                        path="/schedules"
                    />
                </div>
            </ConnectedRouter>
        </Card>
    )
}