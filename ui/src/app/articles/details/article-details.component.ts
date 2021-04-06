import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ArticleService} from '../article.service';

@Component({
  selector: 'app-article-details',
  templateUrl: './article-details.component.html',
  styleUrls: ['./article-details.component.css']
})
export class ArticleDetailsComponent implements OnInit {
  article: object = {
    title: '',
    summary: ''
  };

  constructor(private route: ActivatedRoute, private articleService: ArticleService) {
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.articleService.getArticle(params.id).subscribe((response: any) => {
        this.article = response;
      });
    });
  }

}
