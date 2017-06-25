import * as React from 'react'

import {FormEvent} from 'react'
//noinspection TypeScriptCheckImport
import PlacesAutocomplete, {geocodeByAddress, getLatLng} from 'react-places-autocomplete'
import RaisedButton from "material-ui/RaisedButton"


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
                <RaisedButton
                    fullWidth={true}
                    label="Submit"
                    type="submit"
                />
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