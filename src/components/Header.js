import PropTypes from 'prop-types'
import React from 'react'

export default class Header extends React.PureComponent {
    static propTypes = {
        description: PropTypes.string,
        titleText: PropTypes.string
    }

    render() {
        return (
            <div>
                <h1>{this.props.titleText}</h1>
                <p>{this.props.description}</p>
            </div>
        )
    }
}