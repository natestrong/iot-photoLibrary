import {Component, OnInit} from '@angular/core';
import {AngularFirestore} from '@angular/fire/firestore';
import {Observable} from 'rxjs';
import {PhotoService} from "./photo.service";

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.css']
})
export class AppComponent implements OnInit {
  items: Observable<any[]>;
  currentSessionCount: number = null
  helloMessage: string = ''

  constructor(db: AngularFirestore, private photoService: PhotoService) {
    this.items = db.collection('currentSession').valueChanges();
  }

  ngOnInit(): void {
    this.photoService.piCommandHandler('initializeSession')
  }

  public onButton() {
    console.log('pushed')
    this.photoService.piCommandHandler('currentSessionCount')
      .subscribe(data => {
          this.currentSessionCount = data['Message']
          console.log(data)
        }
      )
  }
}
