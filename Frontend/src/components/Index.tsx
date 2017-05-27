import * as React from 'react'

import AddressForm from './AddressForm'
import Header from './Header'

export default class Index extends React.Component<undefined, undefined> {
    render() {
        return (
            <div>
                <Header
                    description="This app helps plan movie marathons at Canadian and US movie theatres."
                    titleText="Movie Marathon"
                />
                <AddressForm/>
            </div>
        )
    }
}