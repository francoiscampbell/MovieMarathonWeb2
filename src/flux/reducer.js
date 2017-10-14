import Immutable from 'immutable'
import {routerReducer as router} from 'react-router-redux'

import movies from 'flux/ducks/movies'


function combineReducers(reducers) {
    const reducersImmutable = Immutable.fromJS(reducers)
    return function(state = new Immutable.Map(), action) {
        return reducersImmutable.map((reducer, name) => reducer(state.get(name), action))
    }
}

export default combineReducers({
    movies,
    router
})