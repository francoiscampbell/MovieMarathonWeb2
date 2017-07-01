import * as Immutable from 'immutable'
import * as React from "react"
import {FormEvent} from "react"

import DatePicker from "material-ui/DatePicker"
import * as moment from "moment"
//noinspection TypeScriptCheckImport
import RaisedButton from "material-ui/RaisedButton"
import GooglePlaceAutocomplete from 'material-ui-autocomplete-google-places'

interface AddressFormProps {
    onSubmit: (lat: number, lng: number, date: moment.Moment) => void
}

interface AddressFormState {
    addressErrorText: string
    date: moment.Moment
    lat: number
    lng: number
    focused: boolean
}

export default class AddressForm extends React.Component<AddressFormProps, AddressFormState> {

    defaultState = Immutable.fromJS({
        addressErrorText: '',
        date: moment(),
        lat: null,
        lng: null,
        focused: false
    })

    state = this.defaultState.toJS()

    render() {
        return (
            <form onSubmit={this.handleFormSubmit}>
                <GooglePlaceAutocomplete
                    errorText={this.state.addressErrorText}
                    hintText="Enter your address"
                    results={this.onLatLng}
                />
                <DatePicker
                    autoOk={true}
                    container="inline"
                    firstDayOfWeek={0}
                    fullWidth={true}
                    hintText="Choose date"
                    onChange={this.onDateSelected}
                />
                <RaisedButton
                    fullWidth={true}
                    label="Submit"
                    type="submit"
                />
            </form>
        )
    }

    onDateSelected = (_, date: any) => {
        this.setState({date: moment(date)})
    }

    onLatLng = (lat, lng) => {
        this.setState({
            addressErrorText: this.defaultState.get('addressErrorText'),
            lat,
            lng
        })
    }

    handleFormSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        if (this.validateForm()) {
            this.props.onSubmit(
                this.state.lat,
                this.state.lng,
                this.state.date)
        }
    }

    validateForm = () => {
        if (process.env.NODE_ENV !== 'production') {
            return true
        }
        if (this.state.lat === null || this.state.lng === null) {
            this.setState({
                addressErrorText: 'Please enter your address'
            })
            return false
        }
        return true
    }
}