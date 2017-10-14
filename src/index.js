import injectTapEventPlugin from 'react-tap-event-plugin'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import {Provider} from 'react-redux'
import React from 'react'
import ReactDOM from 'react-dom'

import Index from 'components/Index'
import store from 'flux/store'


injectTapEventPlugin()

if (process.env.NODE_ENV !== 'production') {
    console.log('dev')
}

ReactDOM.render(
    <Provider store={store}>
        <MuiThemeProvider>
            <Index/>
        </MuiThemeProvider>
    </Provider>,
    document.getElementById('react-app')
)