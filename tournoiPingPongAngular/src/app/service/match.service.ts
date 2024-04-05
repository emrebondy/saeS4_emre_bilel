import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Match } from '../ObjectDto/Match';

@Injectable({
    providedIn: 'root'
  })
  export class MatchService {
  
    constructor( private http: HttpClient ) {  }
  
    match_insert_one(match :Match): Observable<Match> {
      return this.http.post<Match>('http://127.0.0.1:5000/matchs/', match);
    }
  
  }