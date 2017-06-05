import * as React from 'react'

export class ListItem {
    constructor(public readonly key: any, public readonly value: any) {
    }
}

interface SubmitCheckboxListProps {
    items: ListItem[]
    onSubmit: (Array) => void
}

interface SubmitCheckboxListState {
}

export default class SubmitCheckboxList extends React.Component<SubmitCheckboxListProps, SubmitCheckboxListState> {
    items = this.props.items.map(item => {
        return {
            item,
            selected: false
        }
    })

    render() {
        const elements = this.props.items.map((item, index) => {
            return (
                <li>
                    <ListItemCheckbox
                        index={index}
                        onChange={this.onCheckboxChange}
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
                    onClick={this.onSubmit}
                >
                    Submit
                </button>
            </div>
        )
    }

    onCheckboxChange = (index, checked) => {
        this.items[index].selected = checked
    }

    onSubmit = () => {
        this.props.onSubmit(
            this.items
                .filter(item => item.selected)
                .map(item => item.item.key)
        )
    }
}

function ListItemCheckbox({index, onChange}) {
    return <input type="checkbox" onChange={event => onChange(index, event.target.checked)}/>
}