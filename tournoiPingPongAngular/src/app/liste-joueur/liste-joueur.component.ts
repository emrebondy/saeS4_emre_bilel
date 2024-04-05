import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { Joueur } from '../ObjectDto/Joueur';
import { JoueurService } from '../service/joueur.service';

@Component({
    selector: 'app-liste-joueur',
    standalone: true,
    imports: [RouterLink, CommonModule, RouterOutlet, NgIf, NgFor],
    templateUrl: './liste-joueur.component.html'
})
export class ListeJoueurComponent {
    data: Joueur[] = [];
  
    constructor(private joueurService :JoueurService) { }
  
    ngOnInit(): void {
      this.find_all();
    }
  
    find_all() {
      this.joueurService.joueur_get_all().subscribe(data => { this.data = data });
    }
  }