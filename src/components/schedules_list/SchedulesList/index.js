import {connect} from 'react-redux'
import {createStructuredSelector} from 'reselect'
import PropTypes from 'prop-types'
import React from 'react'
import Immutable from 'immutable'
import humanizeDuration from 'humanize-duration'
import RaisedButton from 'material-ui/RaisedButton'
import styled from 'styled-components'
import Timeline from 'react-visjs-timeline'

import {
    makeCalendar,
    saveCalendar
} from 'scheduling/ScheduleExporter'
import {selectors as moviesSelectors} from 'flux/ducks/movies'


const Button = styled(RaisedButton)`
  margin-top: 32px;
`

const tooltopLineClassName = 'tooltip_line'

export class UnconnectedSchedulesList extends React.PureComponent {
    static propTypes = {
        schedules: PropTypes.instanceOf(Immutable.List).isRequired
    }

    state = {
        schedulesToShow: this.props.schedules.take(10).toList()
    }

    render() {
        const hasSchedules = this.props.schedules.size > 0
        const headerText = hasSchedules ?
            `Showing ${this.state.schedulesToShow.size} of ${this.props.schedules.size} schedules:` :
            `Could not find any schedules for the selected movies`
        const timeline = hasSchedules ? (
            <Timeline
                groups={this.getGroups()}
                items={this.getItems()}
                options={this.getOptions()}
            />
        ) : null
        const hasMoreSchedules = this.props.schedules.size > this.state.schedulesToShow.size
        const showMoreButton = hasMoreSchedules ? (
            <Button
                fullWidth={true}
                label="Show More"
                onClick={this.onShowMore}
            />
        ) : null

        const exportButton = (
            <Button
                fullWidth={true}
                label="Export Schedule"
                primary={true}
                type="submit"
            />
        )

        return (
            <div>
                <h1>{headerText}</h1>
                <form onSubmit={this.exportSchedule}>
                    {timeline}
                    {showMoreButton}
                    {exportButton}
                </form>
            </div>
        )
    }

    getOptions() {
        return {
            format: {
                minorLabels: {
                    minute: 'h:mma',
                    hour: 'ha'
                }
            },
            groupOrder: 'id',
            orientation: 'both',
            showCurrentTime: false,
            showMajorLabels: true,
            stack: false,
            tooltip: {
                followMouse: true,
                overflowMethod: 'cap'
            },
            type: 'range',
            verticalScroll: true,
            zoomKey: 'ctrlKey'
        }
    }

    getItems() {
        return this.state.schedulesToShow.flatMap((schedule, scheduleIndex) => {
            return schedule.get('movies').map((movie, movieIndex) => {
                const startTime = movie.get('showtime')
                const runTime = movie.get('runTime')
                const endTime = startTime.clone().add(runTime)
                const delay = schedule.getIn(['delays', movieIndex])
                const delayHtml = delay ?
                    `<div class="${tooltopLineClassName}">Delay until next movie: ${humanizeDuration(delay)}</div>` :
                    ''

                const title = movie.get('title')
                const theatre = schedule.getIn(['theatre', 'name'])

                const tooltip = `
                    <div>
                        <div class="${classNameclassName}"><h3>${title}</h3></div>
                        <div class="${tooltopLineClassName}"><h4>${theatre}</h4></div>
                        <div class="${tooltopLineClassName}">Start time: ${startTime.format('dddd MMMM D YYYY, h:mm a')}</div> 
                        <div class="${tooltopLineClassName}">Run time: ${humanizeDuration(runTime)}</div> 
                        <div class="${tooltopLineClassName}">End time: ${endTime.format('dddd MMMM D YYYY, h:mm a')}</div> 
                        ${delayHtml}
                    </div>
                `
                return {
                    content: title,
                    end: endTime,
                    group: scheduleIndex + 1,
                    start: startTime,
                    title: tooltip
                }
            })
        }).toJS()
    }

    getGroups() {
        return this.state.schedulesToShow.map((schedule, index) => {
            const id = index + 1
            return {
                id,
                content: `<input type="radio" name="scheduleChoice" id="scheduleChoice-${id}">`
            }
        }).toJS()
    }

    onShowMore = () => {
        const newNumSchedulesToShow = this.state.schedulesToShow.size + 10
        const schedulesToShow = this.props.schedules.take(newNumSchedulesToShow).toList()
        this.setState({schedulesToShow})
    }

    exportSchedule = (event) => {
        event.preventDefault()

        const selectedIndex = Immutable.List(event.currentTarget.elements)
            .findIndex(e => e.checked)
        const schedule = this.state.schedulesToShow.get(selectedIndex)

        const calendar = makeCalendar(schedule)
        console.log(calendar)
        saveCalendar(calendar)
    }
}

const mapStateToProps = createStructuredSelector({
    schedules: moviesSelectors.schedulesSelector
})

export default connect(mapStateToProps)(UnconnectedSchedulesList)