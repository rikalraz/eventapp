import { Component, OnInit } from '@angular/core';
import {Event} from './event';
import {EventService} from './events.service';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-eventpage',
  templateUrl: './eventpage.component.html',
  styleUrls: ['./eventpage.component.css'],
  providers: [EventService]
})

export class EventpageComponent implements OnInit {
  events: Event[]
  editEvent: Event

  constructor(private eventService: EventService, private http: HttpClient) {}

  ngOnInit() {
    this.getEvents()
  }

  getEvents():void{
    this.eventService.getEvents().subscribe(events => (this.events = events))
  }

  add(data):void{
    let createevent = this.eventService.addEvents(data).subscribe(() => this.getEvents())


  }

  delete(event: Event): void {
    this.events = this.events.filter(h =>h !== event)
    this.eventService
      .deleteEvent(event._id)
      .subscribe(() => console.log('Event Deleted'))
  }

  edit(event) {
    console.log('_______####################==========');
    this.editEvent = event
  }

  update() {
    if(this.editEvent){
      this.eventService.updateEvent(this.editEvent).subscribe(() => {
        this.getEvents()
      })
      this.editEvent = undefined
    }
  }
}
