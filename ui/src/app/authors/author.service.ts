import {Injectable} from '@angular/core';
import {ApiService} from '../common/api.service';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthorService extends ApiService {

  AUTHORS_URI = 'authors/';

  constructor(protected http: HttpClient) {
    super(http);
  }

  fetchAuthors(offset: number, limit: number) {
    return super.fetchList(`${this.AUTHORS_URI}?limit=${limit}&offset=${offset}`);
  }

  getAuthor(id: number) {
    return super.fetchOne(`${this.AUTHORS_URI + id}/`);
  }
}
