import { Routes } from '@angular/router';
import { ListeJoueurComponent } from './liste-joueur/liste-joueur.component';
import { ListeTournoisComponent } from './liste-tournois/liste-tournois.component';

export const routes: Routes = [
    {path: 'liste-personnes', component: ListeJoueurComponent },
    {path: 'liste-tournois', component: ListeTournoisComponent },
];  
