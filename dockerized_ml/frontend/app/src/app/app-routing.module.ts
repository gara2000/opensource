import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateJobComponent } from './components/pages/create-job/create-job.component';
import { HomeComponent } from './components/pages/home/home.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'new_job', component: CreateJobComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
