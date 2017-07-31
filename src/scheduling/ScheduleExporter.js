import Immutable from 'immutable'
import FileSaver from 'file-saver'
import moment from 'moment'
import uuid from 'uuid'

const ICAL_DT_FORMAT = 'YYYYMMDDTHHmm00'

export function makeCalendar(schedule) {
    const theatreName = schedule.getIn(['theatre', 'name'])
    const movies = schedule.get('movies')

    const events = movies.map(m => {
        const title = m.get('title')
        const startTime = m.get('showtime')
        const endTime = startTime.clone().add(m.get('runTime'))
        return makeEvent(title, startTime, endTime, theatreName)
    }).join('\n')
    const calendar = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'CALSCALE:GREGORIAN',
        'PRODID:-//Francois Campbell//moviemarathon.ca',
        events,
        'END:VCALENDAR'
    ]
    return Immutable.List(calendar).join('\n')
}

function makeEvent(title, startTime, endTime, theatreName) {
    const startTimeUtc = moment.utc(startTime)
    const endTimeUtc = moment.utc(endTime)
    //noinspection TypeScriptUnresolvedFunction
    const eventData = [
        `BEGIN:VEVENT`,
        `UID:${uuid.v1()}`,
        `DTSTAMP:${moment.utc().format(ICAL_DT_FORMAT)}Z`,
        `DTSTART:${startTimeUtc.format(ICAL_DT_FORMAT)}Z`,
        `DTEND:${endTimeUtc.format(ICAL_DT_FORMAT)}Z`,
        `SUMMARY:${title}`,
        `LOCATION:${theatreName}`,
        `END:VEVENT`,
    ]
    return Immutable.List(eventData).join('\n')
}

export function saveCalendar(calendar) {
    const blob = new Blob([calendar], {type: 'text/calendar', endings: 'native'})
    FileSaver.saveAs(blob, 'moviemarathon.ics')
}