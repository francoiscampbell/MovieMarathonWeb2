import PropTypes from 'prop-types'
import React from 'react'
import CircularProgress from "material-ui/CircularProgress"

import styles from './loading.scss'

export default class Loading extends React.Component {

    static propTypes = {
        text: PropTypes.string.isRequired
    }

    render() {
        return (
            <div>
                <CircularProgress/>
                <span className={styles.text}>
                    {this.props.text}
                </span>
            </div>
        )
    }
}