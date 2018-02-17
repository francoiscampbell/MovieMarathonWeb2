import Immutable from 'immutable'
import PropTypes from 'prop-types'
import React from 'react'
import styled from 'styled-components'

import Checkbox from 'material-ui/Checkbox'
import RaisedButton from 'material-ui/RaisedButton'


const SubmitButtonTop = styled(RaisedButton)`
    margin-bottom: 32px;
`

const SubmitButtonBottom = styled(RaisedButton)`
    margin-top: 32px;
`

export default class SubmitCheckboxList extends React.PureComponent {

    static propTypes = {
        items: PropTypes.instanceOf(Immutable.List),
        onSubmit: PropTypes.func,
        sort: PropTypes.bool
    }

    static defaultProps = {
        items: Immutable.List(),
        onSubmit: () => {
        },
        sort: false
    }

    componentDidMount() {
        console.dir(styles)
    }

    render() {
        this.selected = this.props.items.map(_ => false).toMap()
        const listItems = this.props.items.map((item, index) => {
            return (
                <ListItemCheckbox
                    index={index}
                    key={index}
                    label={item}
                    onChange={this.onCheckboxChange}/>
            )
        })

        return (
            <form onSubmit={this.handleFormSubmit}>
                <SubmitButtonTop
                    fullWidth={true}
                    label="Submit"
                    primary={true}
                    type="submit"
                />
                {listItems}
                <SubmitButtonBottom
                    fullWidth={true}
                    label="Submit"
                    primary={true}
                    type="submit"
                />
            </form>
        )
    }

    onCheckboxChange = (index, checked) => {
        this.selected = this.selected.set(index, checked)
    }

    handleFormSubmit = (event) => {
        event.preventDefault()
        this.props.onSubmit(this.selected
            .filter(item => item)
            .keySeq()
            .toList()
        )
    }
}


class ListItemCheckbox extends React.PureComponent {
    static propTypes = {
        index: PropTypes.number,
        label: PropTypes.string,
        onChange: PropTypes.func.isRequired
    }

    render() {
        return (
            <Checkbox
                label={this.props.label}
                onCheck={event => this.props.onChange(this.props.index, event.target.checked)}
            />
        )
    }
}