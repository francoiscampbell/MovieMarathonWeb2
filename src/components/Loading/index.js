import PropTypes from 'prop-types'
import CircularProgress from "material-ui/CircularProgress"
import React from 'react'
import styled from 'styled-components'


const LoadingText = styled.span`
    line-height: 40px;
    padding-left: 16px;
    vertical-align: bottom;
`

export default class Loading extends React.Component {

    static propTypes = {
        children: PropTypes.string.isRequired
    }

    render() {
        return (
            <div>
                <CircularProgress/>
                <LoadingText>
                    {this.props.children}
                </LoadingText>
            </div>
        )
    }
}