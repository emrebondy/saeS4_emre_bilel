import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ListeJoueurComponent } from './liste-joueur/liste-joueur.component';
import { ListeTournoisComponent } from './liste-tournois/liste-tournois.component';
import { DetailsJoueurComponent } from './detail_joueur/detail_joueur.component';
import { InscriptionPersonneComponent } from './inscription_joueur/inscription_joueur.component';
import { CreerTournoisComponent } from './creation_tournoi/creation_tournoi.component';
import { InscriptionAuTournoisComponent } from './inscription_au_tournoi/inscription_au_tournoi.component';
import { AjouterMatchAuTournoisComponent } from './ajouter_match_tournoi/ajouter_match_tournoi.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, ListeJoueurComponent, CommonModule,ListeTournoisComponent, DetailsJoueurComponent, InscriptionPersonneComponent, CreerTournoisComponent, InscriptionAuTournoisComponent, AjouterMatchAuTournoisComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'tournoiPingPongAngular';
}
