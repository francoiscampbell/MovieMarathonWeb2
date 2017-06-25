import * as injectTapEventPlugin from 'react-tap-event-plugin';

import * as React from 'react'
import * as ReactDOM from 'react-dom'

import Index from './components/Index'
//noinspection TypeScriptCheckImport
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

injectTapEventPlugin()

ReactDOM.render(
    <MuiThemeProvider>
        <Index/>
    </MuiThemeProvider>,
    document.getElementById('react-app')
)