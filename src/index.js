import React from 'react'
import ReactDOM from 'react-dom'

import injectTapEventPlugin from 'react-tap-event-plugin'

import Index from './components/Index'
//noinspection TypeScriptCheckImport
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

injectTapEventPlugin()

if (process.env.NODE_ENV !== 'production') {
    console.log('dev')
}

ReactDOM.render(
    <MuiThemeProvider>
        <Index/>
    </MuiThemeProvider>,
    document.getElementById('react-app')
)