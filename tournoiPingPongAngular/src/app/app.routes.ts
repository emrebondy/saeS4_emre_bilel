import { Routes } from '@angular/router';
import { ListeJoueurComponent } from './liste-joueur/liste-joueur.component';
import { ListeTournoisComponent } from './liste-tournois/liste-tournois.component';
import { DetailsJoueurComponent } from './detail_joueur/detail_joueur.component';
import { InscriptionPersonneComponent } from './inscription_joueur/inscription_joueur.component';
import { CreerTournoisComponent } from './creation_tournoi/creation_tournoi.component';
import { CreerMatchComponent } from './creation_match/creation_match.component';
import { InscriptionAuTournoisComponent } from './inscription_au_tournoi/inscription_au_tournoi.component';
import { AjouterMatchAuTournoisComponent } from './ajouter_match_tournoi/ajouter_match_tournoi.component';

export const routes: Routes = [
    {path: 'liste-personnes', component: ListeJoueurComponent },
    {path: 'liste-tournois', component: ListeTournoisComponent },
    {path: 'detail_joueur/:pseudo', component: DetailsJoueurComponent },
    {path: 'inscription_joueur', component: InscriptionPersonneComponent },
    {path: 'creation_tournoi', component: CreerTournoisComponent },
    {path: 'creation_match', component: CreerMatchComponent },
    {path: 'inscription_au_tournoi', component: InscriptionAuTournoisComponent },
    {path: 'ajouter_match_au_tournoi', component: AjouterMatchAuTournoisComponent },

];  
