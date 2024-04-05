import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { JoueurService } from '../service/joueur.service';
import { Joueur } from '../ObjectDto/Joueur';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';

@Component({
  standalone: true,
  imports: [CommonModule, NgFor, NgIf, RouterLink, RouterOutlet],
  selector: 'app-details-joueur',
  templateUrl: './detail_joueur.component.html'
})
export class DetailsJoueurComponent implements OnInit {
  joueur: Joueur | null = null;
  pseudo: string = "";

  constructor(private joueurService: JoueurService, private route: ActivatedRoute) { }

  find_one() {
    this.joueurService.joueur_get_one(this.pseudo).subscribe(
    data => {
      this.joueur = data;
    }
    );
  }

  ngOnInit(): void {
      this.route.params.subscribe(params => {
        this.pseudo = params['pseudo'];
        this.find_one();
      });

  }
}
