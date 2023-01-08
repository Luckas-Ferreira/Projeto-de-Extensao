import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Curso } from '../Curso';

import { environments } from 'src/environments/environments';

@Injectable({
  providedIn: 'root'
})
export class BackEndService {
  //private baseApiUrl = 'https://robertogram.com.br/api.php?method=PDF2Json'
  private baseApiUrl = environments.baseApiUrl
  
  constructor(private http: HttpClient) { }
  
  createUpload(formData: FormData): Observable<FormData> {
    return this.http.post<FormData>(this.baseApiUrl, formData);
  }
}
