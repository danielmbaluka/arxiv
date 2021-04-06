import {Component, OnInit} from '@angular/core';
import {AuthService} from './auth/auth.service';
import {MatDialog} from '@angular/material/dialog';
import {LoginComponent} from './auth/login/login.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(public authService: AuthService, public dialog: MatDialog) {
  }

  ngOnInit(): void {
  }

  onLogin($event: MouseEvent) {
    $event.preventDefault();

    const dialogRef = this.dialog.open(LoginComponent, {
      width: '400px',
      data: {}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
    });
  }

  onLogout() {
    this.authService.logout();
  }
}
