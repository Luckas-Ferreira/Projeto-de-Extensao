import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrintJsonComponent } from './print-json.component';

describe('PrintJsonComponent', () => {
  let component: PrintJsonComponent;
  let fixture: ComponentFixture<PrintJsonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PrintJsonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PrintJsonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
