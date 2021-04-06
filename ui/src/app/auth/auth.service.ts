import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {JwtHelperService} from '@auth0/angular-jwt';
import {ConfigService} from '../common/config.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  helper = new JwtHelperService();
  LOGIN_URI = 'auth/token/';
  REGISTER_API = 'auth/signup/';

  constructor(
    private http: HttpClient
  ) {
  }

  login(user: object) {
    return this.http.post(
      ConfigService.API_ENDPOINT + this.LOGIN_URI,
      user,
      ConfigService.UN_AUTHENTICATED_HTTP_OPTIONS
    );
  }

  register(user: object) {
    return this.http.post(
      ConfigService.API_ENDPOINT + this.REGISTER_API,
      user,
      ConfigService.UN_AUTHENTICATED_HTTP_OPTIONS
    );
  }

  setUser(user: object) {
    localStorage.setItem('user', JSON.stringify(user));
  }

  isLoggedIn(): boolean {
    const user = localStorage.getItem('user');
    if (user == null) {
      return false;
    }

    if (this.helper.isTokenExpired(JSON.parse(user).token)) {
      this.logout();
      return false;
    }
    return true;
  }

  logout() {
    localStorage.removeItem('user');
  }

  getAuthToken() {
    const loggedInUser = JSON.parse(localStorage.getItem('user'));
    if (loggedInUser != null) {
      return loggedInUser.token;
    }
    return null;
  }


  getUser() {
    return JSON.parse(localStorage.getItem('user')) || {};
  }



}

