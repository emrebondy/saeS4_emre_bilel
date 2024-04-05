import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { TournoisService } from '../service/tournois.service';
import { InscriptionT } from '../ObjectDto/inscriptionTournoi';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-inscriptionau-tournois',
  standalone: true,
  imports: [FormsModule, CommonModule, NgFor, NgIf, RouterLink, RouterOutlet],
  templateUrl: './inscription_au_tournoi.component.html'
})

export class InscriptionAuTournoisComponent {
  data: InscriptionT = {
    nom_tournoi: "",
    pseudo: "",
  };

  constructor(private tournoisService: TournoisService) { }

  insert_one() {
    this.tournoisService.tournoi_inscription_joueur(this.data).subscribe(data => { this.data = data });
  }

}
