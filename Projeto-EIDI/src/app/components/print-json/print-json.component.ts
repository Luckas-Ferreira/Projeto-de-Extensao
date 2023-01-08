import { Component } from '@angular/core';
import { Curso } from 'src/app/Curso';
import { BackEndService } from 'src/app/services/back-end.service';
@Component({
  selector: 'app-print-json',
  templateUrl: './print-json.component.html',
  styleUrls: ['./print-json.component.css']
})
export class PrintJsonComponent {
  Curso: Curso[] = []
  /*Cursos: Curso[] = [
      {"id": 3, "name": "Tom", "type": "Dog", "age": 11},
      {"id": 4, "name": "Bob", "type": "Horse", "age": 2},
  ]; */

 

  /*
  constructor(private backend: BackEndService){
    this.getAll();
  }
  getAll(){
    this.backend.getAll().subscribe((Curso) => (this.Curso = Curso))
  }
  */

}