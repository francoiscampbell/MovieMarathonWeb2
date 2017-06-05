import * as React from 'react'

import {FormEvent} from 'react'
import PlacesAutocomplete, {geocodeByAddress, getLatLng} from 'react-places-autocomplete'


interface AddressFormProps {
    onGeocodeSuccess: (LatLng) => void
}

interface AddressFormState {
    address: string
}

export default class AddressForm extends React.Component<AddressFormProps, AddressFormState> {

    state = {
        address: '7 Walmer Road, Toronto, ON, Canada'
    }

    render() {
        const inputProps = {
            value: this.state.address,
            onChange: this.onChange
        }

        return (
            <form onSubmit={this.handleFormSubmit}>
                <PlacesAutocomplete inputProps={inputProps}/>
                <button type="submit">Submit</button>
            </form>
        )
    }

    onChange = (address: string) => {
        this.setState({address})
    }

    handleFormSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault()

        geocodeByAddress(this.state.address)
            .then(results => getLatLng(results[0]))
            .then(this.props.onGeocodeSuccess)
            .catch(error => console.error('Error', error))
    }
}