import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {ConfigService} from './config.service';

export class ApiService {

  constructor(protected http: HttpClient) {
  }

  fetchList(uri: string): Observable<any> {
    return this.http.get(`${ConfigService.API_ENDPOINT + uri}`);
  }

  fetchOne(uri: string): Observable<any> {
    return this.http.get(`${ConfigService.API_ENDPOINT + uri}`);
  }

  post(uri: string, payload: object): Observable<any> {
    return this.http.post(`${ConfigService.API_ENDPOINT + uri}`, payload, ConfigService.UN_AUTHENTICATED_HTTP_OPTIONS);
  }
}
