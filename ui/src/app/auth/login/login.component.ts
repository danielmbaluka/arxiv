import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
import {AuthService} from '../auth.service';
import {ToastrService} from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user = {
    username: '',
    password: ''
  };

  constructor(
    public dialogRef: MatDialogRef<LoginComponent>,
    @Inject(MAT_DIALOG_DATA) public data: object,
    private authService: AuthService,
    private toastr: ToastrService) {
  }

  ngOnInit(): void {
  }

  onCancel() {
    this.dialogRef.close();
  }

  onLogin() {
    if (this.user.username.trim().length <= 0) {
      this.toastr.error('Username cannot be empty');
      return;
    } else if (this.user.password.trim().length <= 0) {
      this.toastr.error('Password cannot be empty');
      return;
    }
    this.authService.login(this.user).subscribe((response: any) => {

      const profile = {
        token: response.access,
        username: this.user.username
      };

      this.authService.setUser(profile);
      this.toastr.success('Login was successful');
      this.dialogRef.close();
    }, error => {
      if (error.error && error.error.detail) {
        this.toastr.error(error.error.detail, 'Login failed!');
      } else {
        this.toastr.error('Login failed');
      }
    });
  }
}
