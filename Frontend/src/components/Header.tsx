import * as React from 'react'

export interface HeaderProps {
    description: string
    titleText: string
}

export interface HeaderState {

}

export default class Header extends React.Component<HeaderProps, HeaderState> {
    render() {
        return (
            <div>
                <h1>{this.props.titleText}</h1>
                <p>{this.props.description}</p>
            </div>
        )
    }
}