import * as React from 'react'

interface SubmitCheckboxListProps<T> {
    items: T[]
    onSubmit: (Array) => void
}

interface SubmitCheckboxListState<T> {
}

export default class SubmitCheckboxList<T> extends React.Component<SubmitCheckboxListProps<T>, SubmitCheckboxListState<T>> {
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
                    {item}
                </li>
            )
        })

        return (
            <div>
                <ul>
                    {elements}
                </ul>
                <button
                    onClick={() => this.props.onSubmit(this.items.filter(item => item.selected))}
                >
                    Submit
                </button>
            </div>
        )
    }

    onCheckboxChange = (index, checked) => {
        this.items[index].selected = checked
    }
}

function ListItemCheckbox({index, onChange}) {
    return (
        <input type="checkbox" onChange={event => onChange(index, event.target.checked)}/>
    )
}