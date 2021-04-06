import {Component, OnInit} from '@angular/core';
import {AuthorService} from './author.service';
import { PageEvent } from '@angular/material/paginator';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})
export class AuthorsComponent implements OnInit {
  authors: object[] = [];
  totalItems = 0;
  pageSize = 25;
  currentPage = 0;

  pageSizeOptions: number[] = [10, 25, 50];
  // MatPaginator Output
  pageEvent: PageEvent;

  constructor(private authService: AuthorService) {
  }

  ngOnInit() {
    this.fetchData();
  }

  fetchData() {
    const offset = this.currentPage * this.pageSize;
    this.authService.fetchAuthors(offset, this.pageSize).subscribe((response: any) => {
      this.authors = response.results;
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
