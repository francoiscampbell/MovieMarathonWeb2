import PropTypes from 'prop-types'
import React from 'react'

import DatePicker from 'material-ui/DatePicker'
import moment from 'moment'
import RaisedButton from 'material-ui/RaisedButton'
import GooglePlaceAutocomplete from 'material-ui-autocomplete-google-places'


export default class AddressForm extends React.Component {

    static propTypes = {
        onSubmit: PropTypes.func.isRequired,
    }

    defaultState = {
        addressErrorText: '',
        date: moment(),
        lat: null,
        lng: null,
        focused: false
    }

    state = this.defaultState

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
                    primary={true}
                    type="submit"
                />
            </form>
        )
    }

    onDateSelected = (_, date) => {
        this.setState({date: moment(date)})
    }

    onLatLng = (lat, lng) => {
        this.setState({
            addressErrorText: this.defaultState.addressErrorText,
            lat,
            lng
        })
    }

    handleFormSubmit = (event) => {
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