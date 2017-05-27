import * as React from 'react'
import PlacesAutocomplete, {geocodeByAddress, getLatLng} from 'react-places-autocomplete'
import {FormEvent} from 'react'


interface AddressFormProps {

}

interface AddressFormState {
    address: string
}

export default class AddressForm extends React.Component<AddressFormProps, AddressFormState> {

    state = {
        address: ''
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

        console.log('form submitted')
    }
}