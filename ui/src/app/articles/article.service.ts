import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ApiService} from '../common/api.service';

@Injectable({
  providedIn: 'root'
})
export class ArticleService extends ApiService {

  ARTICLES_URI = 'articles/';
  TOPICS_URI = 'articles/topics/';
  FAVORITE_URI = 'articles/favorite/';

  constructor(protected http: HttpClient) {
    super(http);
  }

  fetchArticles(offset: number, limit: number, topic: string) {
    let url = `${this.ARTICLES_URI}?limit=${limit}&offset=${offset}`;
    if (topic) {
      url = `${url}&topic=${topic}`;
    }
    return super.fetchList(url);
  }

  getArticle(id: number) {
    return super.fetchOne(`${this.ARTICLES_URI + id}/`);
  }

  getTopics() {
    return super.fetchList(`${this.TOPICS_URI}`);
  }

  favoriteArticle(article: object) {
    return super.post(`${this.FAVORITE_URI}`, article);
  }
}
