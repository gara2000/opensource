import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PROC_URL } from '../shared/constants/urls';

@Injectable({
  providedIn: 'root'
})
export class FileService {

  constructor(private http: HttpClient) { }

  uploadFile(fileContent: string){
    return this.http.post(PROC_URL, {content: fileContent});
  }
}