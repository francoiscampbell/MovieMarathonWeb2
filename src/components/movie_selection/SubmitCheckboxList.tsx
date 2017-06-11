import * as Immutable from 'immutable'
import * as React from 'react'

import {Movie} from '../../data_model/Movie'


export class ListItem<K, V> {
    constructor(public readonly key: K, public readonly value: V) {
    }
}

interface SubmitCheckboxListProps {
    items: Immutable.Iterable<string, ListItem<Movie, string>>
    onSubmit: (selectedMovies: Immutable.Map<string, Movie>) => void
    sort: boolean
}

export default function SubmitCheckboxList({items, onSubmit, sort}: SubmitCheckboxListProps) {
    const sortedItems = sort ? items.sortBy(item => item.value) : items
    const _items = sortedItems.map(item => {
        return {
            item,
            selected: false
        }
    })

    const _onSubmit = () => {
        onSubmit(_items
            .filter(item => item.selected)
            .map(item => item.item.key)
            .toMap()
        )
    }

    const onCheckboxChange = (index, checked) => {
        _items.get(index).selected = checked
    }

    const elements = sortedItems.map((item, index) => {
        return (
            <li>
                <ListItemCheckbox
                    index={index}
                    onChange={onCheckboxChange}
                />
                {item.value || item.toString()}
            </li>
        )
    })

    return (
        <div>
            <ul>
                {elements}
            </ul>
            <button
                onClick={_onSubmit}
            >
                Submit
            </button>
        </div>
    )
}

interface ListItemCheckboxProps {
    index: number | string
    onChange: (number, boolean) => void
}

function ListItemCheckbox({index, onChange}: ListItemCheckboxProps) {
    return <input type="checkbox" onChange={event => onChange(index, event.target.checked)}/>
}