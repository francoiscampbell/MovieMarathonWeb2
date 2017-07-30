import * as Immutable from "immutable"
import * as FileSaver from 'file-saver'
import * as moment from "moment"
import * as uuid from "uuid"

import {Schedule} from "../data_model/Movie"

const ICAL_DT_FORMAT = 'YYYYMMDDTHHmm00'

export function makeCalendar(schedule: Schedule) {
    const theatreName = schedule.getIn(['theatre', 'name'])
    const movies = schedule.get('movies').toList()

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
    return Immutable.List<string>(calendar).join('\n')
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
    return Immutable.List<string>(eventData).join('\n')
}

export function saveCalendar(calendar: string) {
    const blob = new Blob([calendar], {type: 'text/calendar', endings: 'native'})
    //noinspection TypeScriptUnresolvedFunction
    FileSaver.saveAs(blob, 'moviemarathon.ics')
}