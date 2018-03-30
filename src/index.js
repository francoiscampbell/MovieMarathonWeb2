import createHistory from 'history/createMemoryHistory'
import injectTapEventPlugin from 'react-tap-event-plugin'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import {Provider} from 'react-redux'
import React from 'react'
import ReactDOM from 'react-dom'

import Index from 'components/Index'
import createStore from 'flux/createStore'


injectTapEventPlugin()

if (process.env.NODE_ENV !== 'production') {
    console.log('dev')
}

const history = createHistory()

ReactDOM.render(
    <Provider store={createStore(history)}>
        <MuiThemeProvider>
            <Index history={history}/>
        </MuiThemeProvider>
    </Provider>,
    document.getElementById('react-app')
)