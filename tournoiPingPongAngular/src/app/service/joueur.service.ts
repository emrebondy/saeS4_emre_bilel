import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

import { Joueur } from '../ObjectDto/Joueur';

@Injectable({
  providedIn: 'root'
})
export class JoueurService {

  constructor(private http: HttpClient) { }

  joueur_get_all(): Observable<Joueur[]> {
    return this.http.get<Joueur[]>('http://127.0.0.1:5000/joueurs/');
  }

  joueur_get_one(pseudo :string): Observable<Joueur> {
    return this.http.get<Joueur>('http://127.0.0.1:5000/joueurs/' + pseudo);
  }

  joueur_insert_one(Joueur :Joueur): Observable<Joueur> {
    return this.http.post<Joueur>('http://127.0.0.1:5000/joueurs/', Joueur);
  }
}
