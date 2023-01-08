import { Component } from '@angular/core';
import { JsonService } from 'src/app/services/json.service';
import { Curso } from 'src/app/Curso';
import { environments } from 'src/environments/environments';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  allCurso: Curso[] = []
  cursos: Curso[]  = []
  disciplinas: Curso['Disciplinas'] = []
  
  constructor(private jsonService: JsonService){}

  ngOnInit(): void {
    this.jsonService.getUpload().subscribe((json) => {
      const data = json
      this.allCurso = data
      this.cursos = data

      console.log(data)
    });
  };
};
