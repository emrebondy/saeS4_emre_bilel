import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { TournoisService } from '../service/tournois.service';
import { AjouterMatch } from '../ObjectDto/ajouterMatch';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-ajoutermatch-tournois',
  standalone: true,
  imports: [FormsModule, CommonModule, NgFor, NgIf, RouterLink, RouterOutlet],
  templateUrl: './ajouter_match_tournoi.component.html'
})

export class AjouterMatchAuTournoisComponent {
  data: AjouterMatch = {
    nom_tournoi: "",
    match_id: 0,
  };

  constructor(private tournoisService: TournoisService) { }

  insert_one() {
    this.tournoisService.tournoi_ajouter_match(this.data).subscribe(data => { this.data = data });
  }

}
