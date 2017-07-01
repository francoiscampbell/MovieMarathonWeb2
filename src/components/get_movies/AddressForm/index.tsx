import * as React from 'react'

import {FormEvent} from 'react'
//noinspection TypeScriptCheckImport
import PlacesAutocomplete, {geocodeByAddress, getLatLng} from 'react-places-autocomplete'
import RaisedButton from "material-ui/RaisedButton"
import GooglePlaceAutocomplete from 'material-ui-autocomplete-google-places'

import * as styles from './addressform.scss'

interface AddressFormProps {
    onGeocodeSuccess: (LatLng) => void
}

interface AddressFormState {
    address: string
    focused: boolean
}

export default class AddressForm extends React.Component<AddressFormProps, AddressFormState> {

    state = {
        address: '7 Walmer Road, Toronto, ON, Canada',
        focused: false
    }

    render() {
        const classNames = {
            root: styles.root,
            input: styles.input
        }
        const hrClassName = this.state.focused ?
            styles.underlineActive : styles.underline
        const inputProps = {
            value: this.state.address,
            onBlur: this.onBlur,
            onChange: this.onChange,
            onFocus: this.onFocus
        }

        return (
            <form onSubmit={this.handleFormSubmit}>

                <div className={styles.container}>
                    <PlacesAutocomplete
                        classNames={classNames}
                        inputProps={inputProps}
                    />
                    <hr className={hrClassName} />
                </div>
                <RaisedButton
                    fullWidth={true}
                    label="Submit"
                    type="submit"
                />
            </form>
        )
    }

    onBlur = () => {
        this.setState({focused: false})
    }

    onChange = (address: string) => {
        this.setState({address})
    }

    onFocus = () => {
        this.setState({focused: true})
    }

    handleFormSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault()

        geocodeByAddress(this.state.address)
            .then(results => getLatLng(results[0]))
            .then(this.props.onGeocodeSuccess)
            .catch(error => console.error('Error', error))
    }
}