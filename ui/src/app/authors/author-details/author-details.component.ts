import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {AuthorService} from '../author.service';

@Component({
  selector: 'app-author-details',
  templateUrl: './author-details.component.html',
  styleUrls: ['./author-details.component.css']
})
export class AuthorDetailsComponent implements OnInit {
  author: object = {};

  constructor(private route: ActivatedRoute, private authorService: AuthorService) {
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.authorService.getAuthor(params.id).subscribe((response: any) => {
        this.author = response;
      });
    });
  }

}
