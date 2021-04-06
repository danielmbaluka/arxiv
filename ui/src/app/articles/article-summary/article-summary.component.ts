import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {AuthService} from '../../auth/auth.service';
import {ToastrService} from 'ngx-toastr';
import {ArticleService} from '../article.service';

@Component({
  selector: 'app-article-summary',
  templateUrl: './article-summary.component.html',
  styleUrls: ['./article-summary.component.css']
})
export class ArticleSummaryComponent implements OnInit, OnChanges {

  @Input() article: object = {};
  @Input() showFullArticle = true;

  constructor(private authService: AuthService, private articleService: ArticleService, private toastr: ToastrService) {
  }

  ngOnInit() {
  }

  ngOnChanges(changes: SimpleChanges): void {
    this.article = changes.article.currentValue;
    if (changes.showFullArticle) {
      this.showFullArticle = changes.showFullArticle.currentValue;
    }

  }

  onFavourite(id: number) {
    if (!this.authService.isLoggedIn()) {
      this.toastr.error('You must be logged use this functionality');
    } else {
      this.articleService.favoriteArticle({article: id}).subscribe((response: any) => {
        this.toastr.success('Request was successful');
        window.location.reload();
      });
    }
  }
}
