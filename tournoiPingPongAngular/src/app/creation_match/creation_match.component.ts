import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { MatchService } from '../service/match.service';
import { Match } from '../ObjectDto/Match';
import { NgIf, NgFor } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-creer-match',
  standalone: true,
  imports: [FormsModule, CommonModule, NgFor, NgIf, RouterLink, RouterOutlet],
  templateUrl: './creation_match.component.html'
})

export class CreerMatchComponent {
  data: Match = {
    _id: 0,
    joueur1: "",
    joueur2: ""
  };

  constructor(private matchService: MatchService) { }

  insert_one() {
    this.matchService.match_insert_one(this.data).subscribe(data => { this.data = data });
  }

}
