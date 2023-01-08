import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environments } from 'src/environments/environments';
import { Curso } from '../Curso';

@Injectable({
  providedIn: 'root'
})
export class JsonService {

  private baseApiUrl = environments.baseApiUrl
  
  constructor(private http: HttpClient) { }

  getUpload(): Observable<Curso[]> {
    return this.http.get<Curso[]>(this.baseApiUrl)
  }
}
