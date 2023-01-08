import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Curso } from '../Curso';

@Injectable({
  providedIn: 'root'
})
export class JsonService {

  private baseApiUrl = 'http://localhost:3000/Json'
  
  constructor(private http: HttpClient) { }

  getUpload(): Observable<Curso[]> {
    return this.http.get<Curso[]>(this.baseApiUrl)
  }
}
