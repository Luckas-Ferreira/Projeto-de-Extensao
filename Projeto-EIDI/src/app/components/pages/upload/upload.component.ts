import { Component} from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { BackEndService } from 'src/app/services/back-end.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  uploadForm!: FormGroup

  constructor(
    private backEndService: BackEndService,
    private router: Router){}

  async onFileSelected(event: any){
    const File = event.target.files[0]

    this.uploadForm.patchValue({pdf: File})

    const formData = new FormData()
    formData.append("pdf", File)

    //enviando para o service
    await this.backEndService.createUpload(formData).subscribe();
  } 

  ngOnInit(): void{
    this.uploadForm = new FormGroup({
      file: new FormControl('', [Validators.required]),
    })
  }

  get file(){
    return this.uploadForm.get('file')!;
  }

  submit(){
    if (this.uploadForm.invalid){
      return;
    }else{
      //this.router.navigate(['/']);
      console.log("Arquivo enviado", this.uploadForm.value)
    }

  

  
  }
}

