import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ListeJoueurComponent } from './liste-joueur/liste-joueur.component';
import { ListeTournoisComponent } from './liste-tournois/liste-tournois.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, ListeJoueurComponent, CommonModule,ListeTournoisComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'tournoiPingPongAngular';
}
