import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { InscriptionT } from '../ObjectDto/inscriptionTournoi';
import { AjouterMatch } from '../ObjectDto/ajouterMatch';
import { Tournois } from '../ObjectDto/Tournois';

@Injectable({
  providedIn: 'root'
})
export class TournoisService {

  constructor( private http: HttpClient ) {  }

  rechercher_list_tournoi(): Observable<Tournois[]> {
    return this.http.get<Tournois[]>('http://127.0.0.1:5000/tournois/afficher/list/') ;
  }

  tournois_insert_one(tournois :Tournois): Observable<Tournois> {
    return this.http.post<Tournois>('http://127.0.0.1:5000/tournois/ajouter/', tournois);
  }

  tournoi_inscription_joueur(inscriptionTournoi: InscriptionT): Observable<any> {
    return this.http.put<Tournois>('http://127.0.0.1:5000/tournois/inscrire/', inscriptionTournoi);
  }

  tournoi_ajouter_match(ajouterMatch: AjouterMatch): Observable<any> {
    return this.http.put<Tournois>('http://127.0.0.1:5000/tournois/ajouter_match/', ajouterMatch);
  }

}
