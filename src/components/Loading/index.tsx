import * as React from "react"
import CircularProgress from "material-ui/CircularProgress"

import * as styles from './loading.scss'

interface LoadingProps {
    text: string
}

export default class Loading extends React.Component<LoadingProps, any> {
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