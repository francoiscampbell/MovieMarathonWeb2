import * as React from "react"
import {FormEvent} from "react"

import DatePicker from "material-ui/DatePicker"
import * as moment from "moment"
//noinspection TypeScriptCheckImport
import PlacesAutocomplete, {geocodeByAddress, getLatLng} from "react-places-autocomplete"
import RaisedButton from "material-ui/RaisedButton"
import GooglePlaceAutocomplete from 'material-ui-autocomplete-google-places'

interface AddressFormProps {
    onSubmit: (lat: number, lng: number, date: moment.Moment) => void
}

interface AddressFormState {
    date: moment.Moment
    lat: number
    lng: number
    focused: boolean
}

export default class AddressForm extends React.Component<AddressFormProps, AddressFormState> {

    state = {
        date: moment(),
        lat: 0,
        lng: 0,
        focused: false
    }

    render() {
        return (
            <form onSubmit={this.handleFormSubmit}>
                <GooglePlaceAutocomplete
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
        this.setState({lat, lng})
    }

    handleFormSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        this.props.onSubmit(
            this.state.lat,
            this.state.lng,
            this.state.date)
    }
}