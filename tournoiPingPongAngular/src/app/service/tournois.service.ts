import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

import { Tournois } from '../ObjectDto/Tournois';

@Injectable({
  providedIn: 'root'
})
export class TournoisService {

  constructor( private http: HttpClient ) {  }

  rechercher_list_tournoi(): Observable<Tournois[]> {
    return this.http.get<Tournois[]>('http://127.0.0.1:5000/tournois/afficher/list/') ;
  }

  //tournois_get_one(_id: String): Observable<Tournois[]> {
    //return this.http.get<Tournois[]>('/api/tournois/get_one/' + _id );
  //}

  //tournois_insert_one(tournois :Tournois): Observable<Tournois> {
    //return this.http.post<Tournois>('/api/tournois/post_one', tournois);
  //}

}
