import {
    applyMiddleware,
    createStore,
} from 'redux'
import createSagaMiddleware from 'redux-saga'
import {routerMiddleware} from 'react-router-redux'

import {sagaWatcher as moviesSagaWatcher} from './ducks/movies'
import reducer from 'flux/reducer'

export default history => {
    const sagaMiddleware = createSagaMiddleware()

    const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
    const enhancers = composeEnhancers(
        applyMiddleware(
            sagaMiddleware,
            routerMiddleware(history),
        )
    )

    const sagaWatchers = [
        moviesSagaWatcher
    ]

    const store = createStore(reducer, enhancers)

    sagaWatchers.forEach(sagaMiddleware.run)

    return store
}
