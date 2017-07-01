import * as Immutable from "immutable"
import * as React from "react"
import {FormEvent} from "react"

import Checkbox from "material-ui/Checkbox"
//noinspection TypeScriptCheckImport
import {ListItem} from "material-ui/List"
import RaisedButton from "material-ui/RaisedButton"

import * as styles from './submitcheckboxlist.scss'

interface SubmitCheckboxListProps {
    items: Immutable.List<any>
    onSubmit: (selectedIndices: Immutable.List<number>) => void
    sort: boolean
}

export default function SubmitCheckboxList({items, onSubmit}: SubmitCheckboxListProps) {
    let selected = items.map(_ => false).toMap()

    const handleFormSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        onSubmit(selected
            .filter(item => item)
            .keySeq()
            .toList()
        )
    }

    const onCheckboxChange = (index, checked) => {
        selected = selected.set(index, checked)
    }

    const listItems = items.map((item, index) => {
        return (
            <ListItemCheckbox
                index={index}
                key={index}
                label={item}
                onChange={onCheckboxChange}/>
        )
    })

    return (
        <form onSubmit={handleFormSubmit}>
            {listItems}
            <RaisedButton
                className={styles.submitbutton}
                fullWidth={true}
                label="Submit"
                type="submit"
            />
        </form>
    )
}

interface ListItemCheckboxProps {
    index: number | string
    label: string
    onChange: (number, boolean) => void
}

function ListItemCheckbox({index, label, onChange}: ListItemCheckboxProps) {
    return <Checkbox
        label={label}
        onCheck={event => onChange(index, event.target.checked)}
    />
}