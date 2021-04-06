import {Component, OnInit} from '@angular/core';
import {ArticleService} from './article.service';
import {PageEvent} from '@angular/material/paginator';

@Component({
  selector: 'app-articles',
  templateUrl: './articles.component.html',
  styleUrls: ['./articles.component.css']
})
export class ArticlesComponent implements OnInit {
  articles: object[] = [];
  topics: object[] = [];

  totalItems = 0;
  pageSize = 25;
  currentPage = 0;

  pageSizeOptions: number[] = [10, 25, 50];
  // MatPaginator Output
  pageEvent: PageEvent;

  topic = 'All';

  constructor(private articleService: ArticleService) {
  }


  ngOnInit() {
    this.fetchData();

    this.articleService.getTopics().subscribe((response: any) => {
      this.topics = response.results;
    });
  }

  fetchData() {
    let filterTopic = this.topic;
    if (this.topic === 'All') {
      filterTopic = null;
    }
    const offset = this.currentPage * this.pageSize;
    this.articleService.fetchArticles(offset, this.pageSize, filterTopic).subscribe((response: any) => {
      this.articles = response.results;
      this.totalItems = response.count;
    });
  }

  public handlePagination(e: PageEvent) {
    this.currentPage = e.pageIndex;
    this.pageSize = e.pageSize;
    console.log(e);
    this.fetchData();
    return e;
  }

}
