import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EchartsGrafosComponent } from './echarts-grafos.component';

describe('EchartsGrafosComponent', () => {
  let component: EchartsGrafosComponent;
  let fixture: ComponentFixture<EchartsGrafosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EchartsGrafosComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EchartsGrafosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
