import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { TournoisService } from '../service/tournois.service';
import { Tournois } from '../ObjectDto/Tournois';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-creer-tournois',
  standalone: true,
  imports: [FormsModule, CommonModule, NgFor, NgIf, RouterLink, RouterOutlet],
  templateUrl: './creation_tournoi.component.html'
})

export class CreerTournoisComponent {
  data: Tournois = {
    _id: 0,
    nom: '',
    date: '',
    duree: 0,
    lieu: '',
    list_joueur_dto: [],
    list_match: [],
    pwd : ''
  };

  constructor(private tournoisService: TournoisService) { }

  insert_one() {
    this.tournoisService.tournois_insert_one(this.data).subscribe(data => { this.data = data });
  }

}
