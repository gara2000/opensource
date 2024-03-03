import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PROC_URL } from '../shared/constants/urls';

@Injectable({
  providedIn: 'root'
})
export class JobService {

  constructor(private http: HttpClient) { }

  createJob(fileContent: string, name: string){
    const info = {name: name, data: fileContent}
    const stringInfo = JSON.stringify(info);
    return this.http.post(PROC_URL, {info: stringInfo});
  }
}
