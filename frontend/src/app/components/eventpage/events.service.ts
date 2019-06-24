import { Injectable } from "@angular/core";
import {HttpClient} from '@angular/common/http';

import {Observable} from 'rxjs'
import {Event} from './event'

@Injectable()
export class EventService {
    constructor(private http: HttpClient){}

    getEvents(): Observable<Event[]>{
        return this.http.get<Event[]>('v1/api/events')
    }

    addEvents(event: Event): Observable<Event> {
        return this.http.post<Event>('v1/api/events', event)
    }

    deleteEvent(id: number): Observable<{}> {
        const url = `v1/api/events/${id}`
        return this.http.delete(url)
    }

    updateEvent(event: Event): Observable<Event>{
        const url = `v1/api/event/${event._id}`
        return this.http.put<Event>(url, event)
    }
}