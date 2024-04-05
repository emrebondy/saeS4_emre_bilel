import { Component, OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { JoueurService } from '../service/joueur.service';
import { Joueur } from '../ObjectDto/Joueur';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-inscription-joueur',
  standalone: true,
  imports: [FormsModule, RouterLink, RouterOutlet, NgFor, NgIf],
  templateUrl: './inscription_joueur.component.html'
})

export class InscriptionPersonneComponent {
  data: Joueur = {_id: 0, age: 0, email : '', niveau: '', nom: '', prenom: '', pseudo: ''};

  constructor(private joueurService :JoueurService) { }

  insert_one() {
    this.joueurService.joueur_insert_one(this.data).subscribe(data => { this.data = data });
  }

}