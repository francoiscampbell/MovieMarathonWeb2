import * as React from "react"

export interface HeaderProps {
    description: string
    titleText: string
}

export default function Header({description, titleText}: HeaderProps) {
    return (
        <div>
            <h1>{titleText}</h1>
            <p>{description}</p>
        </div>
    )
}