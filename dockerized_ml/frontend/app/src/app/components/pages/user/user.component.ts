import { Component } from '@angular/core';
import { User } from '../../../shared/models/User';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrl: './user.component.css'
})

export class UserComponent {
  users: User[] = [];
}
