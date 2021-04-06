import {Injectable} from '@angular/core';
import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest
} from '@angular/common/http';
import {Observable} from 'rxjs';
import {AuthService} from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class TokenAuthInterceptor implements HttpInterceptor {
  constructor(
    private authService: AuthService
  ) {
  }

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    if (
      request.url.includes('auth/token/') ||
      request.url.includes('auth/signup')
    ) {
      // do not add any authentication headers
    } else {
      if (this.authService.isLoggedIn()) {
        request = request.clone({
          setHeaders: {
            Authorization: `Bearer ${this.authService.getAuthToken()}`
          }
        });
      }

    }

    return next.handle(request);
  }
}
