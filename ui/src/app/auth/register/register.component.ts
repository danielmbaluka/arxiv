import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {ToastrService} from 'ngx-toastr';
import {AuthService} from '../auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  signUpForm: FormGroup = new FormGroup({
    username: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
    password2: new FormControl('', Validators.required)
  });


  constructor(private authService: AuthService, private toastr: ToastrService, private router: Router) {
  }

  ngOnInit(): void {
  }

  register() {
    const user = this.signUpForm.value;
    if (user.password !== user.password2) {
      this.toastr.error('Passwords do not match');
      return;
    }

    this.authService.register(user).subscribe((response: any) => {
      // Registration was successful, log the user in
      const loginUser = {
        username: user.username,
        password: user.password
      };
      this.authService.login(loginUser).subscribe((resp: any) => {
        const profile = {
          token: resp.access,
          username: user.username
        };

        this.authService.setUser(profile);
        this.toastr.success('Registration was successful');

        this.router.navigateByUrl('/');
      });
    }, error => {
      if (error.error && error.error.error) {
        this.toastr.error(error.error.error, 'Failed');
      } else {
        this.toastr.error('An error occurred');
      }
    });
  }
}
