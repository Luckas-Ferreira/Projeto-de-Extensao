import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PrintJsonComponent } from './components/print-json/print-json.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { HomeComponent } from './components/pages/home/home.component';
import { AboutComponent } from './components/pages/about/about.component';
import { UploadComponent } from './components/pages/upload/upload.component';

import { EchartsxModule } from 'echarts-for-angular';
import { EchartsGrafosComponent } from './components/echarts-grafos/echarts-grafos.component';

@NgModule({
  declarations: [
    AppComponent,
    PrintJsonComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    AboutComponent,
    UploadComponent,
    EchartsGrafosComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule, 
    ReactiveFormsModule,
    EchartsxModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
