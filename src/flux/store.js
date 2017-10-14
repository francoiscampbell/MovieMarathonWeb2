import {
    applyMiddleware,
    createStore,
} from 'redux'
import thunkMiddleware from 'redux-thunk'

import reducer from 'src/flux/reducer'


export default createStore(reducer, applyMiddleware(thunkMiddleware))