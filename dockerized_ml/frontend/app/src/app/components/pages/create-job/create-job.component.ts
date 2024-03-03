import { Component } from '@angular/core';
import { JobService } from '../../../services/job.service';

@Component({
  selector: 'app-create-job',
  templateUrl: './create-job.component.html',
  styleUrl: './create-job.component.css'
})
export class CreateJobComponent {

    constructor (private jobService: JobService) {}

    fileContent: string = "";
    
  onFileSelected(event: any){
    const file: File = event.target.files[0];
    if (file){
      const reader = new FileReader();
      reader.readAsText(file, "UTF-8");
      reader.onload = (evt) => {
        this.fileContent = evt.target?.result as string;
      };
      reader.onerror = (err) => {
        console.error("Error reading file:", err);
      }
    }
  }

    submit(job: any){
      this.jobService.createJob(this.fileContent, job.form.controls.name.value)
        .subscribe(res => {
          console.log("Job created successfully", res);
        }, error => {
          console.log("Error creating the job:", error)
        });
    }
}
