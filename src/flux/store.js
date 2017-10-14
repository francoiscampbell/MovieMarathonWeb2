import {
    applyMiddleware,
    createStore,
} from 'redux'
import {routerMiddleware} from 'react-router-redux'
import thunkMiddleware from 'redux-thunk'

import history from 'history'
import reducer from 'flux/reducer'


const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
const enhancers = composeEnhancers(
    applyMiddleware(
        thunkMiddleware,
        routerMiddleware(history),
    )
)

export default createStore(reducer, enhancers)