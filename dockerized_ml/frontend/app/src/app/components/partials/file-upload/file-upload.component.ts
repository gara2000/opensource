import { Component } from '@angular/core';
import { FileService } from '../../../services/file.service';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrl: './file-upload.component.css'
})
export class FileUploadComponent {

  constructor(private fileService: FileService) { }

  onFileSelected(event: any){
    const file: File = event.target.files[0];
    if (file){
      const reader = new FileReader();
      reader.readAsText(file, "UTF-8");
      reader.onload = (evt) => {
        const fileCotent: string = evt.target?.result as string;
        console.log(fileCotent);

        this.fileService.uploadFile(fileCotent).subscribe(res => {
          console.log("File uploaded successfully", res);
        }, error => {
          console.log("Error uploading file:", error);
        });
      };
      reader.onerror = (err) => {
        console.error("Error reading file:", err);
      }
    }
  }
}
